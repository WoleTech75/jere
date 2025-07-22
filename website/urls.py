from django.urls import  path
from . import views
from .views import SuccessView, ContactView

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),

    path("contact", ContactView.as_view(), name="contact"),

   path("service", views.service, name="service"),

   path("success/", SuccessView.as_view(), name="success"),
]