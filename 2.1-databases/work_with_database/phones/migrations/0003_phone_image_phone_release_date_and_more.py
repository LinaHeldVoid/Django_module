# Generated by Django 4.2.4 on 2023-09-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0002_alter_phone_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='phone',
            name='release_date',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.CharField(default='', max_length=5),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.CharField(default='', max_length=50),
        ),
    ]
