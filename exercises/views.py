from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Muscle, Category, Difficulty, Exercise
from .serializers import MuscleSerializer, CategorySerializer, DifficultySerializer, ExerciseSerializer

class MuscleView(generics.ListAPIView):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
    permission_classes  = [IsAuthenticated]


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes  = [IsAuthenticated]


class DifficultyView(generics.ListAPIView):
    queryset = Difficulty.objects.all()
    serializer_class = DifficultySerializer
    permission_classes  = [IsAuthenticated]


class ExerciseView(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer
    permission_classes  = [IsAuthenticated]

    def get_queryset(self):
        queryset = Exercise.objects.all()
        name = self.request.query_params.get('name')
        category = self.request.query_params.get('category')
        muscle = self.request.query_params.get('muscle')
        difficulty = self.request.query_params.get('difficulty')

        if name is not None:
            queryset = queryset.filter(name__icontains=name)
        if category is not None:
            queryset = queryset.filter(category=category)
        if muscle is not None:
            queryset = queryset.filter(primary_muscle=muscle)
        if difficulty is not None:
            queryset = queryset.filter(difficulty=difficulty)
        return queryset