from django.urls import path

from .views import WorkoutsView

urlpatterns = [
    path('workouts/', WorkoutsView.as_view(), name='workouts'),
]


