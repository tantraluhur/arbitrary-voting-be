# Generated by Django 3.2.20 on 2024-06-22 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inisial', models.CharField(max_length=1)),
                ('jenis_kelamin', models.CharField(choices=[('L', 'L'), ('P', 'P')], max_length=1)),
                ('usia', models.IntegerField()),
                ('partai_nasional', models.CharField(max_length=120)),
                ('partai_daerah', models.CharField(max_length=120)),
                ('bersedia', models.BooleanField(default=False)),
                ('start_date_simulation', models.DateTimeField(blank=True, null=True)),
                ('end_date_simulation', models.DateTimeField(blank=True, null=True)),
                ('information_check_simulation', models.TextField(blank=True, null=True)),
                ('information_check', models.TextField(blank=True, null=True)),
                ('start_date', models.DateTimeField(blank=True, null=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
