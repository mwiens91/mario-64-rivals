import os
from django.db import migrations
from django.conf import settings
from django.core.files.images import ImageFile

COURSE_IMAGE_LOCATIONS = os.path.join(
    'default_course_images/'
)

def add_course_images(apps, schema_editor):
    Course = apps.get_model('leaderboards', 'Course')

    # Add image for each course
    for course in Course.objects.all():
        course.preview_image = os.path.join(
            COURSE_IMAGE_LOCATIONS,
            'courses_{}.png'.format(course.course_number))
        course.save()


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboards', '0009_auto_20180828_0519')
    ]

    operations = [
        migrations.RunPython(add_course_images),
    ]

