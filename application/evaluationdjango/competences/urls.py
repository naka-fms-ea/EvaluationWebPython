from django.urls import path
from . import views, apps
from django.contrib.auth.views import LoginView, LogoutView


app_name = "competences"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("deconnection/", LogoutView.as_view(next_page="competences:index"), name="deconnection"),
    path("connection/", LoginView.as_view(template_name="competences/connection.html", next_page="competences:index"), name="connection"),
]