# Generated by Django 3.2.6 on 2022-06-23 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_slot_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slot',
            name='title',
        ),
    ]
