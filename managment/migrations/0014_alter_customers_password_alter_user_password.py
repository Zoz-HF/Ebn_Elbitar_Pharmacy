# Generated by Django 4.2.2 on 2023-06-18 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0013_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customers',
            name='password',
            field=models.CharField(editable=False, max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
    ]