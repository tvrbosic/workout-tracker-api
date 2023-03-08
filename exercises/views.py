from rest_framework import status, generics
from rest_framework.response import Response

from .models import Muscle, Category, Exercise
from .serializers import MuscleSerializer, CategorySerializer, ExerciseSerializer

class ExercisesView(generics.ListCreateAPIView):
    serializer_class = ExerciseSerializer

    # TODO

            