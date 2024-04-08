# Generated by Django 5.0.3 on 2024-04-07 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0018_remove_about_ministries_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iamnew',
            name='caption_title',
            field=models.CharField(blank=True, help_text='Write a short inspiring heading', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='iamnew',
            name='first_section_title',
            field=models.CharField(blank=True, help_text='Write a short inspiring heading', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='iamnew',
            name='second_section_title',
            field=models.CharField(blank=True, help_text='Write a short inspiring heading', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='iamnew',
            name='third_section_title',
            field=models.CharField(blank=True, help_text='Write a short inspiring heading', max_length=1000, null=True),
        ),
    ]
