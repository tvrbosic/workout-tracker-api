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
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes  = [IsAuthenticated]    