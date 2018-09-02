"""Models to represent competition elements."""

import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    """Custom user model.

    Add attributes here as necessary; for example, a user avatar.
    """
    pass


class Category(models.Model):
    """A non-course category. For example, 70 stars."""
    name = models.CharField(
        max_length=150,
        help_text="The name of the category.",)
    description = models.TextField(
        help_text="The descriptions and rules of the category.")
    preview_image = models.ImageField(
        default="https://via.placeholder.com/320x224",
        upload_to='categories/',
        help_text="Preview image for the category.",)

    class Meta:
        # Use proper plural in admin site
        verbose_name_plural = "categories"

    def __str__(self):
        """String representation of a category."""
        return self.name

    def get_top_record(self):
        """Gets the record for the category.

        Returns None if no record exists.
        """
        return self.categoryrecord_set.first()

    def get_record_count(self):
        """Gets the number of records submitted."""
        return self.categoryrecord_set.count()

    def get_records(self):
        """Gets a queryset of all records."""
        return self.categoryrecord_set.all()

    def get_unique_records(self):
        """Gets a queryset of each user's best record."""
        include = self.categoryrecord_set.order_by(
            'user', 'time').distinct('user')
        include_ids = include.values_list('id')
        return self.categoryrecord_set.filter(id__in=include_ids)


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
        verbose_name="video URL",
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


class Event(models.Model):
    """An event to show on the home page."""
    datetime = models.DateTimeField(
        auto_now_add=True,
        help_text="The date and time the event occured.",)
    text = models.TextField(help_text="The text of the event.")
    image = models.ImageField(
        default="https://via.placeholder.com/320x224",
        upload_to='events/',
        help_text="Image for the event.",)

    class Meta:
        ordering = ['-datetime']

    def __str__(self):
        """String representation of an event."""
        return self.text


@receiver(post_save, sender=SixStarCourseRecord)
def check_to_create_six_star_course_record_event(instance, created, **kwargs):
    """Create an event if a best record was set."""
    # Check if this is the best record
    if created and instance == instance.course.get_top_six_star_record():
        Event.objects.create(
            text="{username} achieved the top six star record with {time} on {course_name}".format(
                username=instance.user.username,
                time=instance.display_time(),
                course_name=instance.course.name,),
            image=instance.course.preview_image,)


@receiver(post_save, sender=SevenStarCourseRecord)
def check_to_create_seven_star_course_record_event(instance, created, **kwargs):
    """Create an event if a best record was set."""
    # Check if this is the best record
    if created and instance == instance.course.get_top_seven_star_record():
        Event.objects.create(
            text="{username} achieved the top seven star record with {time} on {course_name}".format(
                username=instance.user.username,
                time=instance.display_time(),
                course_name=instance.course.name,),
            image=instance.course.preview_image,)


@receiver(post_save, sender=CategoryRecord)
def check_to_create_category_record_event(instance, created, **kwargs):
    """Create an event if a best record was set."""
    # Check if this is the best record
    if created and instance == instance.category.get_top_record():
        Event.objects.create(
            text="{username} achieved the top record with {time} for the {category_name} category".format(
                username=instance.user.username,
                time=instance.display_time(),
                category_name=instance.category.name,),
            image=instance.category.preview_image,)
