# Generated by Django 4.2.7 on 2023-11-28 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(upload_to='blogs'),
        ),
    ]
