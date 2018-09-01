"""Forms for leaderboards."""

from django import forms
from .models import (
    User,
    CategoryRecord,
    SixStarCourseRecord,
    SevenStarCourseRecord,
)


class UserEditForm(forms.ModelForm):
    """A form to edit a user's username."""
    class Meta:
        model = User
        fields = ('username',)


class CategoryRecordCreateForm(forms.ModelForm):
    """A form to create a category record."""
    class Meta:
        model = CategoryRecord
        fields = ('category', 'time', 'date', 'video_url')


class SixStarCourseRecordCreateForm(forms.ModelForm):
    """A form to create a six-star course record."""
    class Meta:
        model = SixStarCourseRecord
        fields = ('course', 'time', 'date', 'video_url')


class SevenStarCourseRecordCreateForm(forms.ModelForm):
    """A form to create a seven-star course record."""
    class Meta:
        model = SevenStarCourseRecord
        fields = ('course', 'time', 'date', 'video_url')
