# Generated by Django 2.1 on 2018-09-01 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0016_auto_20180901_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(default='https://via.placeholder.com/320x224', help_text='Image for the event.', upload_to='events/'),
        ),
    ]
