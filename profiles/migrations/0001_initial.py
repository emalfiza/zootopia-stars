# Generated by Django 2.2.13 on 2020-06-28 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_street_address_1', models.CharField(max_length=60)),
                ('user_street_address_2', models.CharField(max_length=60)),
                ('user_city', models.CharField(max_length=40)),
                ('user_county', models.CharField(max_length=40)),
                ('user_country', models.CharField(max_length=40)),
                ('user_postcode', models.CharField(max_length=20)),
                ('user_phone_number', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
