from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework import permissions
import logging
from rest_framework.permissions import BasePermission
# Create your views here.
from works.models import Works
from works.serializer import WorksSerializer
from rest_framework.authtoken.models import Token
from users.models import CustomUser

logger = logging.getLogger(__name__)


class CustomerPermission(BasePermission):

    def has_permission(self, request, view):
        user = request.user
        type = CustomUser.objects.get(id=user.id).type
        if request.method == "POST":
            return type == "ADM" or type == "CST"
        return user is not None


class LesonViewSet(viewsets.ModelViewSet):
    queryset = Works.objects.all().order_by('-id')
    serializer_class = WorksSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [f.name for f in Works._meta.get_fields()]
    permission_classes = [permissions.IsAuthenticated & CustomerPermission]