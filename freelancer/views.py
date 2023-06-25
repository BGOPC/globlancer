from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import *


# Create your views here.
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
        context['user'] = self.request.user if str(self.request.user) != "AnonymousUser" else None
        freelancer_username = kwargs.get("username", "")
        freelancer = get_object_or_404(FreeLancer, username=freelancer_username)
        context['freelancer'] = freelancer
        return context
