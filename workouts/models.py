from django.db import models

from users.models import CustomUser
from exercises.models import Exercise

class Workout(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='workouts')
    exercises = models.ManyToManyField(Exercise, related_name='workouts')

    def __str__(self):
        return f"{self.name}, Type: {self.type}, Created: {self.date_created}"

    class Meta:
        verbose_name = ("Workout")
        verbose_name_plural = ("Workouts")
