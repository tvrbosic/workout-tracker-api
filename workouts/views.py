from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Workout
from .serializers import WorkoutSerializer

class WorkoutView(generics.ListAPIView, generics.CreateAPIView):
    serializer_class = WorkoutSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        Return a list of all Workouts for the currently authenticated user.
        """
        user = self.request.user
        return Workout.objects.filter(user=user.id)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid(raise_exception=True):
            # Valid data
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)

        # Invalid data
        return Response(message=serializer.errors, status=status.HTTP_400_BAD_REQUEST)