# Generated by Django 5.0.2 on 2024-03-04 16:44

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lecture', '0002_alter_lectureplacefile_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('date', models.DateField()),
                ('lecture', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='lecture.lecture')),
            ],
            options={
                'db_table': 'tbl_date',
            },
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('time', models.TimeField()),
                ('date', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='selleaf.date')),
            ],
            options={
                'db_table': 'tbl_time',
            },
        ),
    ]