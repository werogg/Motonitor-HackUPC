from django.urls import path

from predictor.views import PredictorView

urlpatterns = [
    path('', PredictorView.as_view())
]
