"""Register models with the admin site."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User,
    Category,
    Course,
    CategoryRecord,
    CourseRecord,
)


# Register custom user model
admin.site.register(User, UserAdmin)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Display specific fields for admin page."""
    list_display = ('name',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    """Display specific fields for admin page."""
    list_display = ('course_number', 'name',)


@admin.register(CategoryRecord)
class CategoryRecordAdmin(admin.ModelAdmin):
    """Display specific fields for admin page."""
    list_display = ('user', 'category', 'date', 'time', )


@admin.register(CourseRecord)
class CourseRecordAdmin(admin.ModelAdmin):
    """Display specific fields for admin page."""
    list_display = ('user', 'course', 'date', 'time', )
