# Generated by Django 4.2.7 on 2023-11-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_home_choose'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_choose',
            name='image',
            field=models.ImageField(upload_to='home_choose'),
        ),
    ]