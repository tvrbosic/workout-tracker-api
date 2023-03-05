from rest_framework import generics

from .models import Workout
from .serializers import WorkoutSerializer

class WorkoutsView(generics.ListAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

    def get_queryset(self):
        return Workout.objects.all()
