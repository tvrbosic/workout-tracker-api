from django.db import models

class Muscle(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = ("Muscle")
        verbose_name_plural = ("Muscles")


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")


class Exercise(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=25)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='exercises')
    primary_muscle = models.ForeignKey(Muscle, on_delete=models.PROTECT, related_name='exercises_pm')
    secondary_muscles = models.ManyToManyField(Muscle, related_name='exercises_sm', blank=True)
    force = models.CharField(max_length=25, blank=True, null=True)
    mechanics = models.CharField(max_length=25, blank=True, null=True)
    equipment = models.CharField(max_length=50, blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.name}, Category: {self.category}, Muscle: {self.primary_muscle}, Difficulty: {self.difficulty}"

    class Meta:
        verbose_name = ("Exercise")
        verbose_name_plural = ("Exercises")