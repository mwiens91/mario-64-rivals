"""Forms for leaderboards."""

from django import forms
from .models import User


class UsernameEditForm(forms.ModelForm):
    """A form to edit a user's username."""
    class Meta:
        model = User
        fields = ('username',)
