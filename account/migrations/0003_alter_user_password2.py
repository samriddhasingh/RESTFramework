# Generated by Django 4.2.3 on 2023-07-27 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_password2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password2',
            field=models.CharField(max_length=30, null=True),
        ),
    ]