# Generated by Django 5.0.3 on 2024-04-06 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarshippage',
            name='short_description',
            field=models.CharField(blank=True, help_text='Enter a text less than 250 words', max_length=1000, null=True),
        ),
    ]
