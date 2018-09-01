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

    def get_six_star_record_count(self):
        """Gets the number of six star records submitted."""
        return self.sixstarcourserecord_set.count()

    def get_seven_star_record_count(self):
        """Gets the number of six star records submitted."""
        return self.sevenstarcourserecord_set.count()

    def get_six_star_records(self):
        """Gets a queryset of all six star records."""
        return self.sixstarcourserecord_set.all()

    def get_seven_star_records(self):
        """Gets a queryset of all seven star records."""
        return self.sevenstarcourserecord_set.all()

    def get_unique_six_star_records(self):
        """Gets a queryset of each user's best six star record."""
        include = self.sixstarcourserecord_set.order_by(
            'user', 'time').distinct('user')
        include_ids = include.values_list('id')
        return self.sixstarcourserecord_set.filter(id__in=include_ids)

    def get_unique_seven_star_records(self):
        """Gets a queryset of each user's best seven star record."""
        include = self.sevenstarcourserecord_set.order_by(
            'user', 'time').distinct('user')
        include_ids = include.values_list('id')
        return self.sevenstarcourserecord_set.filter(id__in=include_ids)


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

    def display_time(self):
        """Displays time in a guaranteed sortable format.

        Note that the time field is represented as a datetime.timedelta
        object.

        If then number of hours is more than 9, we want this to return
        9:59:59 (which, by the way, is a time interval that has no
        place in Mario 64 speedrunning; but better to be careful).
        """
        minutes, seconds = divmod(
            self.time.seconds + self.time.days * 86400,
            60)
        hours, minutes = divmod(minutes, 60)

        # Set time to 99:60 if necessary
        if hours > 9:
            hours = 9
            minutes = 59
            seconds = 59

        return '{:01d}:{:02d}:{:02d}'.format(hours, minutes, seconds)


class CategoryRecord(AbstractRecord):
    """A record for a category."""
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        help_text="The category for this record.",)

    class Meta:
        ordering = ['category__id', 'time', 'date']


class SixStarCourseRecord(AbstractRecord):
    """A record for getting six-stars on a course."""
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        help_text="The course for this record.",)

    class Meta:
        ordering = ['course__course_number', 'time', 'date']


class SevenStarCourseRecord(AbstractRecord):
    """A record for getting six-stars on a course."""
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        help_text="The course for this record.",)

    class Meta:
        ordering = ['course__course_number', 'time', 'date']
