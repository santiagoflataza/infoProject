# Generated by Django 3.0 on 2020-09-30 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rubros', '0001_initial'),
        ('perfil', '0007_auto_20200929_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rubro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rubros.Rubro'),
        ),
    ]
