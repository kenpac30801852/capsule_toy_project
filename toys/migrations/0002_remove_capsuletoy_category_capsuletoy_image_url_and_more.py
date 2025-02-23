# Generated by Django 5.1 on 2025-02-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capsuletoy',
            name='category',
        ),
        migrations.AddField(
            model_name='capsuletoy',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='capsuletoy',
            name='manufacturer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='capsuletoy',
            name='release_date',
            field=models.CharField(max_length=255),
        ),
    ]
