# Generated by Django 4.0.3 on 2022-04-10 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.TextField(default='', null='True'),
            preserve_default='True',
        ),
    ]
