# Generated by Django 4.2.10 on 2024-03-02 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tech_start', '0002_alter_location_opening_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='opening_hours',
            field=models.TimeField(default='00:00-23:59'),
        ),
    ]
