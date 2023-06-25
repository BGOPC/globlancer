from django.views.generic import TemplateView


# Create your views here.
class HomeView(TemplateView):
    template_name = "freelancer/home_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user if str(self.request.user) != "AnonymousUser" else None
