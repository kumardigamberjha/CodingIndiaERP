# Generated by Django 4.1.7 on 2023-03-28 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Project', '0002_projectmodel_desc_projectmodel_finishdatetime_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectCategoryModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('subcat', models.CharField(max_length=100)),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]