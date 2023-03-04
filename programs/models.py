from django.db import models
from users.models import CustomUser
from workouts.models import Workout

class Program(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='programs')
    workouts = models.ManyToManyField(Workout, related_name='programs')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Program")
        verbose_name_plural = ("Programs")