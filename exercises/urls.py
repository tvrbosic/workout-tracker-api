from django.urls import path

from .views import ExercisesView

urlpatterns = [
    path('exercises/', ExercisesView.as_view(), name='exercises'),
]


