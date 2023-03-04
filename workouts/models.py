from django.db import models

from users.models import CustomUser
from exercises.models import Exercise

class Workout(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='workouts')
    exercises = models.ManyToManyField(Exercise, related_name='workouts')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Workout")
        verbose_name_plural = ("Workouts")
