# Generated by Django 4.2.4 on 2023-08-02 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Custom_User', '0002_customuser_address_customuser_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='pincode',
            field=models.IntegerField(),
        ),
    ]