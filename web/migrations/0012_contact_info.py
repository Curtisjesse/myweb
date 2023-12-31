# Generated by Django 4.2.7 on 2023-12-01 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_testimonials'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('Location', models.CharField(max_length=150)),
                ('number', models.IntegerField()),
                ('img', models.ImageField(upload_to='Contact_info')),
            ],
        ),
    ]
