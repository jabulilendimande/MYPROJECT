# Generated by Django 5.2.3 on 2025-06-24 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='test_app',
            name='email',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='test_app',
            name='phone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
