# Generated by Django 2.2.3 on 2019-07-22 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ATA', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='direksi',
            name='no_telepon',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mentee',
            name='no_telepon',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='no_telepon',
            field=models.CharField(max_length=50),
        ),
    ]