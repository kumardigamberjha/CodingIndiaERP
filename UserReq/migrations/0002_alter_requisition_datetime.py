# Generated by Django 4.1.7 on 2023-07-22 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserReq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requisition',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]