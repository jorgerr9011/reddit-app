# Generated by Django 4.0 on 2023-06-06 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_alter_customuser_password_alter_customuser_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
