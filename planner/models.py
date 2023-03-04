from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

from users.models import CustomUser
from workouts.models import Workout
from programs.models import Program


class CalendarEntries(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='calendar_entries')
    status = models.CharField(max_length=50, null=False, blank=False)
    
    # Generic Foreign Key Relationship
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return f"User: {self.user.id}, Event: {self.content_object.name}, Status: {self.status}"

    class Meta:
        verbose_name = ("CalendarEntry")
        verbose_name_plural = ("CalendarEntries")


class WorkoutEntry(models.Model):
    date = models.DateField(null=False, blank=False)
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE, related_name='workout_entries')

    def __str__(self):
        return f"User: {self.workout.user}, Event: {self.workout.name}, Date: {self.date}"

    class Meta:
        verbose_name = ("WorkoutEntry")
        verbose_name_plural = ("WorkoutEntries")


class ProgamEntry(models.Model):
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='program_entries')

    def __str__(self):
        return f"User: {self.program.user}, Event: {self.program.name}, Date: {self.date}"

    class Meta:
        verbose_name = ("ProgramEntry")
        verbose_name_plural = ("ProgramEntries")