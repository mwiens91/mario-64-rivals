"""Contains tests for the leaderboards app."""

import datetime
from django.test import TestCase
from .models import (
    User,
    Category,
    Course,
    CategoryRecord,
    SixStarCourseRecord,
    SevenStarCourseRecord,
)


class ModelTests(TestCase):
    """Test that models instantiate correctly.

    Note that events are created automatically when records are created.
    """
    def test_model_instantiation(self):
        """Make sure models instantiate without errors."""
        # Create a user
        user = User.objects.create(
            username='AzureDiamond',
            password='hunter2',)

        # Create a course
        course = Course.objects.create(
            name="course name",
            course_number=69,
            preview_image="fake_media_location",)

        # Create a category
        category = Category.objects.create(
            name="category name",
            description="description",
            preview_image="fake_media_location",)

        # Create a category record
        CategoryRecord.objects.create(
            user=user,
            category=category,
            time=datetime.timedelta(seconds=420),
            date=datetime.datetime.now(),
            video_url="fakeurl.com",)

        # Create a six star course record
        SixStarCourseRecord.objects.create(
            user=user,
            course=course,
            time=datetime.timedelta(seconds=420),
            date=datetime.datetime.now(),
            video_url="fakeurl.com",)

        # Create a seven star course record
        SevenStarCourseRecord.objects.create(
            user=user,
            course=course,
            time=datetime.timedelta(seconds=420),
            date=datetime.datetime.now(),
            video_url="fakeurl.com",)
