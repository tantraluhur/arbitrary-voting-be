# Generated by Django 3.2.20 on 2024-06-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='district',
            field=models.BooleanField(default=False),
        ),
    ]