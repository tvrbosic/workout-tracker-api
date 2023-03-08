from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Workout
from .serializers import WorkoutSerializer

class WorkoutsView(generics.ListAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a list of all Workouts for the currently authenticated user.
        """
        user = self.request.user
        return Workout.objects.filter(user=user.id)
