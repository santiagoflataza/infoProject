# Generated by Django 3.0 on 2020-09-30 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_auto_20200929_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rubro',
            field=models.CharField(max_length=30),
        ),
    ]
