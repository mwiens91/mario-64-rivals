# Generated by Django 2.1 on 2018-08-27 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0006_auto_20180827_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_number',
            field=models.PositiveSmallIntegerField(help_text='The course number.', primary_key=True, serialize=False),
        ),
    ]
