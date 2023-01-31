# Generated by Django 3.2.1 on 2023-01-31 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0007_auto_20230130_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.TextField(blank=True, default='', max_length=262144),
        ),
        migrations.AlterField(
            model_name='problem',
            name='input_format',
            field=models.TextField(blank=True, default='', max_length=131072),
        ),
        migrations.AlterField(
            model_name='problem',
            name='output_format',
            field=models.TextField(blank=True, default='', max_length=131072),
        ),
    ]
