# Generated by Django 3.2.1 on 2023-01-27 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0002_problem'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='output_example',
            field=models.TextField(blank=True, default='', max_length=32768),
        ),
    ]