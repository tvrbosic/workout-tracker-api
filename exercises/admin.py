from django.contrib import admin

from .models import Muscle, Category, Difficulty, Exercise

admin.site.register(Muscle)
admin.site.register(Category)
admin.site.register(Difficulty)
admin.site.register(Exercise)
