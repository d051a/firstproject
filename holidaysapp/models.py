from django.db import models

# Create your models here.

class Holiday (models.Model):
    title = models.CharField(
    max_length=150,
    verbose_name='Название праздника'
    )
    date = models.DateField(
    verbose_name='Дата праздника'
    )
    full_description = models.TextField(
    verbose_name='Полное описание'
    )

    class Meta:
        verbose_name = "Праздник"
        verbose_name_plural = "Празники"

    def __str__(self):
        return self.title
