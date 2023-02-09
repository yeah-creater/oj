# Generated by Django 3.2.1 on 2023-02-08 12:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0044_auto_20230207_1915'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_comments', to='Backend.file')),
            ],
        ),
    ]
