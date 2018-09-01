"""Views for leaderboards."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    FormView,
    ListView,
    TemplateView,
)
from .forms import UserEditForm
from .models import Category, Course


class Home(TemplateView):
    """A view for the homepage."""
    template_name = "leaderboards/home.html"


class ProfileEdit(LoginRequiredMixin, FormView):
    """A view to change a user's info."""
    template_name = "leaderboards/account_settings_edit_profile.html"
    form_class = UserEditForm
    success_url = reverse_lazy("account-edit-profile")

    def form_valid(self, form):
        """Set the user's username."""
        self.request.user.username = form.cleaned_data["username"]
        self.request.user.save()

        return super().form_valid(form)


class About(TemplateView):
    """A view for the about page."""
    template_name = "leaderboards/about.html"


class CategoryList(ListView):
    """A view for listing courses."""
    model = Category
    template_name = "leaderboards/category_list.html"


class CategoryDetailLeaderboard(DetailView):
    """A view for viewing category leaderboards."""
    model = Category
    template_name = "leaderboards/category_detail_leaderboard.html"


class CategoryDetailRecords(DetailView):
    """A view for viewing category records."""
    model = Category
    template_name = "leaderboards/category_detail_records.html"


class CourseList(ListView):
    """A view for listing courses."""
    model = Course
    template_name = "leaderboards/course_list.html"


class CourseDetailSixStarLeaderboard(DetailView):
    """A view for viewing six star leaderboards."""
    model = Course
    template_name = "leaderboards/course_detail_six_star_leaderboard.html"
    pk_url_kwarg = "course_number"


class CourseDetailSevenStarLeaderboard(DetailView):
    """A view for viewing seven star leaderboards."""
    model = Course
    template_name = "leaderboards/course_detail_seven_star_leaderboard.html"
    pk_url_kwarg = "course_number"


class CourseDetailSixStarRecords(DetailView):
    """A view for viewing all six star records."""
    model = Course
    template_name = "leaderboards/course_detail_six_star_records.html"
    pk_url_kwarg = "course_number"


class CourseDetailSevenStarRecords(DetailView):
    """A view for viewing all seven star records."""
    model = Course
    template_name = "leaderboards/course_detail_seven_star_records.html"
    pk_url_kwarg = "course_number"
