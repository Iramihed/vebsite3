from django.db import models
class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    decision = models.TextField('Решение')
    answer = models.CharField('Ответ', max_length=50)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name="Задача"
        verbose_name_plural="Задачи"
