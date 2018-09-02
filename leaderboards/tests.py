"""Contains tests for the leaderboards app."""

import datetime
from django.test import Client, TestCase
from django.urls import reverse
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


class ViewTests(TestCase):
    """Test that views work properly.

    Nothing fancy here, just hit the main pages.
    """
    def test_non_auth_views(self):
        """Test that non-authorized views don't break."""
        # Set up a test client
        client = Client()

        # Refactor this if you want to include detail views
        url_names_to_hit = [
            'home',
            'about',
            'category-list',
            'course-list',
            'login',
        ]

        # Hit a bunch of views
        for url_name in url_names_to_hit:
            self.assertEqual(client.get(reverse(url_name)).status_code, 200)
