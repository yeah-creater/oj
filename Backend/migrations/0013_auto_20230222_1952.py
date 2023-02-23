# Generated by Django 3.2.1 on 2023-02-22 11:52

from django.db import migrations
import simplepro.editor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0012_alter_problem_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='data_range',
            field=simplepro.editor.fields.MDTextField(blank=True, default='', max_length=32768),
        ),
        migrations.AlterField(
            model_name='problem',
            name='input_example',
            field=simplepro.editor.fields.MDTextField(blank=True, default='', max_length=32768),
        ),
        migrations.AlterField(
            model_name='problem',
            name='input_format',
            field=simplepro.editor.fields.MDTextField(blank=True, default='', max_length=131072),
        ),
        migrations.AlterField(
            model_name='problem',
            name='output_example',
            field=simplepro.editor.fields.MDTextField(blank=True, default='', max_length=32768),
        ),
        migrations.AlterField(
            model_name='problem',
            name='output_format',
            field=simplepro.editor.fields.MDTextField(blank=True, default='', max_length=131072),
        ),
    ]
