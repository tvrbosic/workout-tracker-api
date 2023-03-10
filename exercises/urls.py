from django.urls import path

from .views import CategoryView, ExerciseView

urlpatterns = [
    path('exercise/', ExerciseView.as_view(), name='exercises'),
    path('category/', CategoryView.as_view(), name='categories'),

]


