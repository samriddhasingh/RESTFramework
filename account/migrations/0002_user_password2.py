# Generated by Django 4.2.3 on 2023-07-27 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password2',
            field=models.CharField(default=None, max_length=30),
        ),
    ]
