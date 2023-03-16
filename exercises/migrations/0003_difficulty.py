# Generated by Django 4.1.7 on 2023-03-16 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0002_alter_exercise_difficulty_alter_exercise_force_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Difficulty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name': 'Difficulty',
                'verbose_name_plural': 'Difficulties',
            },
        ),
    ]
