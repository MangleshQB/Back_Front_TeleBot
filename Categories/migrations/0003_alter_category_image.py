# Generated by Django 4.2.4 on 2023-08-02 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Categories', '0002_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to='categories_images/'),
        ),
    ]
