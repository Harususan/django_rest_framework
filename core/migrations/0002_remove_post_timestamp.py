# Generated by Django 4.0.4 on 2022-05-21 07:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='timestamp',
        ),
    ]
