# Generated by Django 3.2.20 on 2023-07-22 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songpartaction',
            name='action_name',
        ),
        migrations.RemoveField(
            model_name='songpartaction',
            name='action_param',
        ),
        migrations.AddField(
            model_name='songpartaction',
            name='action_description',
            field=models.CharField(default=' ', max_length=256),
            preserve_default=False,
        ),
    ]
