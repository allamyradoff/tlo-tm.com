# Generated by Django 4.1 on 2022-08-15 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tlo_ru', '0005_about_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='link',
            field=models.FileField(blank=True, max_length=254, null=True, upload_to='price_list', verbose_name='Файл для скачки'),
        ),
    ]