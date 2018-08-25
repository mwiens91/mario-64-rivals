"""Models to represent competition elements."""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model."""
    pass


class Category(models.Model):
    """A non-course category. For example, 70 stars."""
    pass


class Course(models.Model):
    """A Mario 64 course."""
    name = models.CharField(
        max_length=150,
        help_text="The name of the course.",)
