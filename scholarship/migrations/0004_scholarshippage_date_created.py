# Generated by Django 5.0.3 on 2024-04-20 13:07

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scholarship', '0003_scholarshipindexpage_academic_charge_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='scholarshippage',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
