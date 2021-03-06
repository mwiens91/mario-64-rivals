# Generated by Django 2.1 on 2018-09-02 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0017_event_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='information_url',
            field=models.URLField(help_text='An optional information link for the event.', null=True, verbose_name='information URL'),
        ),
        migrations.AddField(
            model_name='event',
            name='video_url',
            field=models.URLField(help_text='An optional video link for the event.', null=True, verbose_name='video URL'),
        ),
    ]
