# Generated by Django 3.2.1 on 2023-02-07 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0043_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tags',
            field=models.CharField(default='', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='题解', max_length=64, null=True),
        ),
    ]
