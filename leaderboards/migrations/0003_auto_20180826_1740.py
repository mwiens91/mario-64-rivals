# Generated by Django 2.1 on 2018-08-26 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0002_create_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryrecord',
            name='time',
            field=models.DurationField(help_text='The time elapsed for the record. Specify the number of seconds or use hh:mm:ss format.'),
        ),
        migrations.AlterField(
            model_name='sevenstarcourserecord',
            name='time',
            field=models.DurationField(help_text='The time elapsed for the record. Specify the number of seconds or use hh:mm:ss format.'),
        ),
        migrations.AlterField(
            model_name='sixstarcourserecord',
            name='time',
            field=models.DurationField(help_text='The time elapsed for the record. Specify the number of seconds or use hh:mm:ss format.'),
        ),
    ]
