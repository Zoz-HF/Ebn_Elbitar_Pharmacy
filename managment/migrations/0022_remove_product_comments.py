# Generated by Django 4.2.2 on 2023-06-21 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0021_alter_product_image_alter_product_image1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='comments',
        ),
    ]
