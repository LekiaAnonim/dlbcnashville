# Generated by Django 5.0.3 on 2024-04-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_event_rename_time_from_worshipservice_start_time_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='display_on_home_page',
            field=models.BooleanField(default=True),
        ),
    ]