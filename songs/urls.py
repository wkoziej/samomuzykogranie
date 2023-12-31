from django.urls import path

app_name = "songs"

from . import views

urlpatterns = [   
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="index"),
]