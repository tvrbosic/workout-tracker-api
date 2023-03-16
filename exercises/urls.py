from django.urls import path

from .views import MuscleView, CategoryView, DifficultyView, ExerciseView

urlpatterns = [
    path('muscle/', MuscleView.as_view(), name='muscles'),
    path('category/', CategoryView.as_view(), name='categories'),
    path('difficulty/', DifficultyView.as_view(), name='difficulties'),
    path('exercise/', ExerciseView.as_view(), name='exercises'),
]


