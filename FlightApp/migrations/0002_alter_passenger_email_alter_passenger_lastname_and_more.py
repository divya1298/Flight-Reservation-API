# Generated by Django 4.2.7 on 2023-12-01 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlightApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passenger',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='lastName',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='passenger',
            name='middleName',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]