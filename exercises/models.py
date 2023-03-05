from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    muscle = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=50)
    instructions = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to='images')

    def __str__(self):
        return f"{self.name}, Type: {self.type}, Muscle: {self.muscle}, Difficulty: {self.difficulty}"

    class Meta:
        verbose_name = ("Exercise")
        verbose_name_plural = ("Exercises")