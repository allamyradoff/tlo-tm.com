# Generated by Django 4.1 on 2022-08-13 06:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tlo_ru', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='contact_us',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tlo_ru.productcontactus', verbose_name='Контакты'),
        ),
    ]
