# Generated by Django 4.2.4 on 2023-09-08 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]
