from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("freelancers/", views.FreeLancersListView.as_view(), name="FreeLancersList"),
    path("freelancer/<str:username>", views.FreeLancerView.as_view(), name="FreeLancerList"),
    path("apply", views.ApplyView.as_view(), name="Apply"),
    path("new", views.NewProjectView.as_view(), name="NewProject"),
    path("project/<int:projectID>", views.ProjectDetailView.as_view(), name="Project"),
    path("projects/", views.ProjectsListView.as_view(), name="ProjectsList"),
    path("about/", views.AboutView.as_view(), name="About"),
    path("contact/", views.ContactView.as_view(), name="Contact"),
    path('switch-language/<str:lang_code>/', views.switch_language, name='switch_language'),
]
