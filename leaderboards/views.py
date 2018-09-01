"""Views for leaderboards."""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    DetailView,
    FormView,
    ListView,
    TemplateView,
)
from .forms import (
    UserEditForm,
    CategoryRecordCreateForm,
    SixStarCourseRecordCreateForm,
    SevenStarCourseRecordCreateForm,
)
from .models import (
    Category,
    Course,
    CategoryRecord,
    SixStarCourseRecord,
    SevenStarCourseRecord,
    Event,
)


class Home(ListView):
    """A view for the homepage.

    Displays paginated events.
    """
    model = Event
    paginate_by = 20
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


class RecordSubmitHome(LoginRequiredMixin, TemplateView):
    """A view for the about page."""
    template_name = "leaderboards/submit_record_home.html"


class RecordSubmitSixStarCourseRecord(LoginRequiredMixin, FormView):
    """A view to submit six star course records."""
    template_name = "leaderboards/submit_record_six_star_course_record.html"
    form_class = SixStarCourseRecordCreateForm
    success_url = reverse_lazy("record-submit-home")

    def form_valid(self, form):
        """Create the record."""
        SixStarCourseRecord.objects.create(
            user=self.request.user,
            time=form.cleaned_data["time"],
            date=form.cleaned_data["date"],
            video_url=form.cleaned_data["video_url"],
            course=form.cleaned_data["course"],
        )

        return super().form_valid(form)


class RecordSubmitSevenStarCourseRecord(LoginRequiredMixin, FormView):
    """A view to submit seven star course records."""
    template_name = "leaderboards/submit_record_seven_star_course_record.html"
    form_class = SevenStarCourseRecordCreateForm
    success_url = reverse_lazy("record-submit-home")

    def form_valid(self, form):
        """Create the record."""
        SevenStarCourseRecord.objects.create(
            user=self.request.user,
            time=form.cleaned_data["time"],
            date=form.cleaned_data["date"],
            video_url=form.cleaned_data["video_url"],
            course=form.cleaned_data["course"],
        )

        return super().form_valid(form)


class RecordSubmitCategoryRecord(LoginRequiredMixin, FormView):
    """A view to submit category records."""
    template_name = "leaderboards/submit_record_category_record.html"
    form_class = CategoryRecordCreateForm
    success_url = reverse_lazy("record-submit-home")

    def form_valid(self, form):
        """Create the record."""
        CategoryRecord.objects.create(
            user=self.request.user,
            time=form.cleaned_data["time"],
            date=form.cleaned_data["date"],
            video_url=form.cleaned_data["video_url"],
            category=form.cleaned_data["category"],
        )

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
