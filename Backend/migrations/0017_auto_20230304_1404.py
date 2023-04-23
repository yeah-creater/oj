# Generated by Django 3.2.1 on 2023-03-04 06:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0016_alter_notification_notification_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notification',
            options={'ordering': ['-time']},
        ),
        migrations.AddField(
            model_name='commentlike',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='filelike',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='problem',
            name='data_range',
            field=models.TextField(blank=True, default='', max_length=32768),
        ),
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.TextField(blank=True, default='', max_length=262144),
        ),
        migrations.AlterField(
            model_name='problem',
            name='input_example',
            field=models.TextField(blank=True, default='', max_length=32768),
        ),
        migrations.AlterField(
            model_name='problem',
            name='input_format',
            field=models.TextField(blank=True, default='', max_length=131072),
        ),
        migrations.AlterField(
            model_name='problem',
            name='output_example',
            field=models.TextField(blank=True, default='', max_length=32768),
        ),
        migrations.AlterField(
            model_name='problem',
            name='output_format',
            field=models.TextField(blank=True, default='', max_length=131072),
        ),
    ]
