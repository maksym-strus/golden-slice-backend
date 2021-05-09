# Generated by Django 3.1.7 on 2021-05-08 16:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('graphic', '0002_remove_graphic_number_of_points'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graphic',
            old_name='end_point',
            new_name='number_of_points',
        ),
        migrations.AddField(
            model_name='graphic',
            name='step',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
