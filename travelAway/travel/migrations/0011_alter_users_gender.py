# Generated by Django 4.1.7 on 2023-03-08 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0010_remove_users_departure_users_departuredate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='gender',
            field=models.IntegerField(choices=[('male', 'Male'), ('female', 'Female')]),
        ),
    ]
