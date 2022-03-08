from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.MainPage.as_view()),
]
