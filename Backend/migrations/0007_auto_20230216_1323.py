# Generated by Django 3.2.1 on 2023-02-16 05:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0006_auto_20230216_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='file',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_contest', to='Backend.file'),
        ),
        migrations.DeleteModel(
            name='ContestDiscussion',
        ),
    ]
