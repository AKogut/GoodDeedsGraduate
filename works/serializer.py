from django.shortcuts import render
from rest_framework import serializers

from users.models import CustomUser
from works.models import Works


class WorksSerializer(serializers.HyperlinkedModelSerializer):
    teacher_id = serializers.PrimaryKeyRelatedField(allow_null=True,
                                                    queryset=CustomUser.objects.all().filter(type__in=["ADM", "CST"]))

    class Meta:
        model = Works
        fields = ['id', 'title', 'description', 'price', 'customer_id']

