# Generated by Django 3.0.6 on 2020-05-28 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='name',
            field=models.CharField(default='Anonymous', max_length=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='surname',
            field=models.CharField(default='Anonymous', max_length=40),
        ),
    ]