# Generated by Django 3.2.1 on 2023-02-01 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0012_remove_problem_test_case'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProblemLimit',
        ),
        migrations.DeleteModel(
            name='ProblemSource',
        ),
    ]
