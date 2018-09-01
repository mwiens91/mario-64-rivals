# Generated by Django 2.1 on 2018-09-01 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0014_auto_20180901_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, help_text='The date and time the event occured.')),
                ('text', models.TextField(help_text='The text of the event.')),
            ],
        ),
    ]
