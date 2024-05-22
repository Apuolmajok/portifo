from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("portifo/upload/", views.upload, name="upload"),
    path("portifo/login/", views.login_u, name="login"),
    path("portifo/download/<int:id>/", views.download, name="download")
]