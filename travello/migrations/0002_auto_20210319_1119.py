# Generated by Django 2.0.3 on 2021-03-19 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='img',
            field=models.ImageField(upload_to='pics'),
        ),
    ]
