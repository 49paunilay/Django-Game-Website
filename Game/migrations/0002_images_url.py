# Generated by Django 3.1.1 on 2021-01-10 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='images',
            name='url',
            field=models.URLField(default='www.google.com'),
        ),
    ]
