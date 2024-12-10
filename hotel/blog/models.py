from django.db import models

class Booking(models.Model):
    id = models.AutoField(primary_key=True)  # Автоматический первичный ключ
    category = models.CharField(max_length=100, verbose_name="Категория номера")  # Категория, например, "Люкс"
    rooms = models.PositiveIntegerField(verbose_name="Количество комнат")  # Количество комнат
    date_in = models.DateField(verbose_name="Дата заезда")  # Планируемая дата заезда
    date_out = models.DateField(verbose_name="Дата выезда")  # Планируемая дата выезда
    date_in_fact = models.DateField(null=True, blank=True, verbose_name="Фактическая дата заезда")  # Фактическая дата заезда
    date_out_fact = models.DateField(null=True, blank=True, verbose_name="Фактическая дата выезда")  # Фактическая дата выезда
    bonus = models.TextField(null=True, blank=True, verbose_name="Комментарии")  # Дополнительная информация

    def __str__(self):
        return f"Бронирование #{self.id} ({self.category}, {self.rooms} комнаты)"

    class Meta:
        verbose_name = "Бронирование"
        verbose_name_plural = "Бронирования"
        ordering = ['-date_in']
