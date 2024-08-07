from datetime import timedelta

from django.db import models

from config import settings

NULLABLE = {"blank": True, "null": True}


class Habit(models.Model):
    owner = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="создатель привычки",
                              **NULLABLE, )
    place = models.CharField(max_length=120, verbose_name="Место выполнения привычки")
    time = models.DateTimeField(verbose_name="Дата и время страта выполнения привычки")
    action = models.CharField(max_length=235, verbose_name="Действие, которое требуется сделать")
    pleasant_habit_sign = models.BooleanField(verbose_name="Признак приятной привычки", default=False)
    related_habit = models.ForeignKey("self", on_delete=models.CASCADE, verbose_name="Связанная привычка",
                                      **NULLABLE)
    periodicity = models.SmallIntegerField(default=1, verbose_name="Периодичность выполнения привычки",
                                           help_text="Укажите периодичность от 1 до 7, "
                                                     "где 1 - один раз в неделю, а 7 - это каждый день.")
    reward = models.CharField(max_length=235, verbose_name="Награда за выполнение привычки", **NULLABLE)
    duration = models.DurationField(verbose_name="Продолжительность выполнения привычки",
                                    default=timedelta(seconds=120))
    is_published = models.BooleanField(verbose_name="Признак публичности", default=True)

    def __str__(self):
        return f"{self.owner} будет {self.action} в {self.time} в {self.place}"

    class Meta:
        verbose_name = "привычка"
        verbose_name_plural = "привычки"
