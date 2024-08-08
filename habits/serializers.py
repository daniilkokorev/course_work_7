from rest_framework import serializers

from habits.models import Habit
from habits.validators import (
    HabitRewardValidator,
    TimeHabitValidator,
    PleasantHabitValidator,
    RewardValidator,
    FrequencyHabitValidator,
)
from users.serializers import UserSerializer


class HabitSerializer(serializers.ModelSerializer):
    """
    Сериализатор привычки.
    """
    user = UserSerializer(read_only=True)

    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            HabitRewardValidator("related_habit", "reward"),
            TimeHabitValidator("duration"),
            PleasantHabitValidator("related_habit", "pleasant_habit_sign"),
            RewardValidator("reward", "related_habit", "pleasant_habit_sign"),
            FrequencyHabitValidator("periodicity"),
        ]
