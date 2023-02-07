# Generated by Django 3.2.1 on 2023-02-07 11:13

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0042_alter_solution_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.BooleanField(default=True)),
                ('user_id', models.IntegerField(default=0)),
                ('title', models.CharField(default='题解', max_length=64)),
                ('tags', models.CharField(default='', max_length=128)),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('file', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_blog', to='Backend.file')),
            ],
            options={
                'ordering': ['-create_time'],
            },
        ),
    ]
