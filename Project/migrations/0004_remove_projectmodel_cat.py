# Generated by Django 4.1.7 on 2023-03-28 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0003_projectcategorymodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmodel',
            name='cat',
        ),
    ]