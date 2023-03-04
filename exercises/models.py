from django.db import models

class Execise(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    type = models.CharField(max_length=50, null=False, blank=False)
    muscle = models.CharField(max_length=50, null=False, blank=False)
    difficulty = models.CharField(max_length=50, null=False, blank=False)
    instructions = models.TextField(blank=True, null=True)
    # image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ("Exercise")
        verbose_name_plural = ("Exercises")