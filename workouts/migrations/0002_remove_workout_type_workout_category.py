# Generated by Django 4.1.7 on 2023-03-09 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_alter_exercise_difficulty_alter_exercise_force_and_more'),
        ('workouts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='type',
        ),
        migrations.AddField(
            model_name='workout',
            name='category',
            field=models.ForeignKey(default=19, on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='exercises.category'),
            preserve_default=False,
        ),
    ]
