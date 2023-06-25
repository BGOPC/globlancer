from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView, FormView, CreateView

from .forms import *
from .models import *


# Create your views here.

class UserFieldAccessMixin(LoginRequiredMixin):
    field_required = 'is_employer'

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        if not getattr(user, self.field_required, False):
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class HomeView(TemplateView):
    template_name = "freelancer/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user if str(self.request.user) != "AnonymousUser" else None


class FreeLancersListView(ListView):
    model = FreeLancer
    template_name = "freelancer/freelancers_page.html"
    context_object_name = "freelancers"
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user if str(self.request.user) != "AnonymousUser" else None
        return context


class FreeLancerView(TemplateView):
    template_name = "freelancer/freelancer_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user if self.request.user.is_authenticated else None
        freelancer_username = kwargs.get("username", "")
        freelancer = get_object_or_404(FreeLancer, username=freelancer_username)
        context['freelancer'] = freelancer
        return context


class ApplyView(FormView, LoginRequiredMixin):
    form_class = ApplyForm
    template_name = 'freelancer/apply_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user if self.request.user.is_authenticated else None
        return context


class NewProjectView(CreateView, LoginRequiredMixin, UserFieldAccessMixin):
    model = Project
    form_class = NewProjectForm
    template_name = "freelancer/new_project_page.html"

    def form_valid(self, form):
        user = self.request.user
        employer = Employer.objects.get(username=user.username)
        form.instance.employer = employer
        return super().form_valid(form)


class ProjectDetailView(TemplateView):
    template_name = "freelancer/project_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user if self.request.user.is_authenticated else None
        project_id = kwargs.get("projectID", -1)
        project = get_object_or_404(Project, pk=project_id)
        context['project'] = project
        return context


class ProjectsListView(ListView):
    model = Project
    template_name = "freelancer/projects_page.html"
    paginate_by = 50

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user if self.request.user.is_authenticated else None
        return context


class AboutView(TemplateView):
    template_name = "freelancer/about_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user if self.request.user.is_authenticated else None
        return context


class ContactView(TemplateView):
    template_name = "freelancer/contact_us.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user if self.request.user.is_authenticated else None
        return context
