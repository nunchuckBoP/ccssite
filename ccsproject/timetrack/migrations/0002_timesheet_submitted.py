# Generated by Django 4.2.7 on 2023-12-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetrack', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='timesheet',
            name='submitted',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Submitted'),
        ),
    ]
