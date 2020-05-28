

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import filters, permissions
from django_filters.rest_framework.backends import DjangoFilterBackend

from GoodDeedsGraduate import settings
from rest_framework import viewsets, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import CustomUser
from .serializer import UserSerializer, SignUpUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [f.name for f in CustomUser._meta.get_fields()]
    permission_classes = [permissions.IsAuthenticated]


class TokenObtainPairWithIdSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super(TokenObtainPairWithIdSerializer, self).validate(attrs)
        data.update({'userId': self.user.id})
        return data


class TokenObtainPairViewWithId(TokenObtainPairView):
    serializer_class = TokenObtainPairWithIdSerializer



@api_view(['POST'])
@permission_classes([AllowAny])
def create_auth(request):
    serialized = SignUpUserSerializer(data=request.POST)
    if serialized.is_valid():
        CustomUser.objects.create_user(email=serialized.data["email"],
                                       password=serialized.data["password"],
                                       first_name=serialized.data["first_name"],
                                       last_name=serialized.data["last_name"]
                                       )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)
