from django.db import models

from users.models import CustomUser

class Works(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    price = models.IntegerField(null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    customer_id = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE, related_name="customer")

    def __str__(self):
        return self.title
