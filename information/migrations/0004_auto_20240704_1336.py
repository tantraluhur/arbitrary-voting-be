# Generated by Django 3.2.20 on 2024-07-04 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('information', '0003_autonext_autonextsimulation_timelimit_timelimitsimulation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='nama',
            field=models.CharField(max_length=120, unique=True),
        ),
        migrations.AlterField(
            model_name='categorysimulation',
            name='nama',
            field=models.CharField(max_length=120, unique=True),
        ),
    ]
