from rest_framework import serializers

from .models import Muscle, Category, Difficulty, Exercise


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class DifficultySerializer(serializers.ModelSerializer):
    class Meta:
        model = Difficulty
        fields = "__all__"


class ExerciseSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    primary_muscle = serializers.PrimaryKeyRelatedField(queryset=Muscle.objects.all())
    secondary_muscles = MuscleSerializer(many=True, read_only=True)
    

    class Meta:
        model = Exercise
        fields = "__all__"