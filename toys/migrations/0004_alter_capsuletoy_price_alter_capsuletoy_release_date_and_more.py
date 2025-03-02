# Generated by Django 5.1 on 2025-02-23 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toys', '0003_capsuletoy_description_alter_capsuletoy_release_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='capsuletoy',
            name='price',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='capsuletoy',
            name='release_date',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='capsuletoy',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
