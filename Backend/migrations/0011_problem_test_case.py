# Generated by Django 3.2.1 on 2023-02-01 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0010_problemlimit_problemsource'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='test_case',
            field=models.FileField(max_length=64, null=True, upload_to='~/project/oj/'),
        ),
    ]