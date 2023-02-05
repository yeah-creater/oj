# Generated by Django 3.2.1 on 2023-02-03 03:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Backend', '0022_alter_submitrecord_time'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submitrecord',
            options={'ordering': ['-time']},
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forbidden', models.BooleanField(blank=True, default=False)),
                ('name', models.CharField(default='Oier', max_length=64)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
