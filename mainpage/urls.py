from django.urls import path, include
from mainpage.views import HomeView


urlpatterns = [
    path('', HomeView.as_view()),
]
