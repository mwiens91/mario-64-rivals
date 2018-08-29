"""Models to represent competition elements."""

import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model."""
    # Probably want an image avatar per user here
    pass


class Category(models.Model):
    """A non-course category. For example, 70 stars."""
    name = models.CharField(
        max_length=150,
        help_text="The name of the category.",)
    description = models.TextField(
        help_text="The descriptions and rules of the category.")
    #preview_image = models.ImageField(
    #    #upload_to=fillmein,
    #    help_text="Preview image for the category.",)

    class Meta:
        # Use proper plural in admin site
        verbose_name_plural = "categories"

    def __str__(self):
        """String representation of a category."""
        return self.name

    # Add a bunch of methods here to get stats


class Course(models.Model):
    """A Mario 64 course."""
    name = models.CharField(
        max_length=150,
        help_text="The name of the course.",)
    course_number = models.PositiveSmallIntegerField(
        primary_key=True,
        help_text="The course number.",)
    preview_image = models.ImageField(
        default="https://via.placeholder.com/320x224",
        upload_to='courses/',
        help_text="Preview image for the course.",)

    class Meta:
        ordering = ['course_number']

    def __str__(self):
        """String representation of a course."""
        return self.name

    def get_top_six_star_record(self):
        """Gets the best six star record for the course.

        Returns None if no record exists.
        """
        return self.sixstarcourserecord_set.first()

    def get_top_seven_star_record(self):
        """Gets the best seven star record for the course.

        Returns None if no record exists.
        """
        return self.sevenstarcourserecord_set.first()


class AbstractRecord(models.Model):
    """Base model for a category or course record."""
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        help_text="The user making the record.")
    time = models.DurationField(
        help_text=(
            "The time elapsed for the record. "
            "Specify the number of seconds or use "
            "hh:mm:ss format."),)
    date = models.DateField(
        default=datetime.date.today,
        help_text="The date the record was made.",)
    video_url = models.URLField(
        help_text="A link to a recording of the record.")

    class Meta:
        # Don't create a database table for this
        abstract = True

    def __str__(self):
        """String representation of a record."""
        return "%s on %s: %s" % (self.user, self.date, self.time)


class CategoryRecord(AbstractRecord):
    """A record for a category."""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        help_text="The category for this record.",)

    class Meta:
        ordering = ['category__id', 'time']


class SixStarCourseRecord(AbstractRecord):
    """A record for getting six-stars on a course."""
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        help_text="The course for this record.",)

    class Meta:
        ordering = ['course__course_number', 'time']


class SevenStarCourseRecord(AbstractRecord):
    """A record for getting six-stars on a course."""
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        help_text="The course for this record.",)

    class Meta:
        ordering = ['course__course_number', 'time']
