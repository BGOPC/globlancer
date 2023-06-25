from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view()),
    path("freelancers/", views.FreeLancersListView.as_view(), name="FreeLancersList"),
    path("freelancer/<str:username>", views.FreeLancerView.as_view(), name="FreeLancerList"),

]
