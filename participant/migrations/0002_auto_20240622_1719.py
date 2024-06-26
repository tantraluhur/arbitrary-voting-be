# Generated by Django 3.2.20 on 2024-06-22 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('participant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='final_answer',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='final_answer_simulation',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='bersedia',
            field=models.BooleanField(default=True),
        ),
    ]
