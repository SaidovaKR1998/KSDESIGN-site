from django.db import models
from ckeditor.fields import RichTextField


class Stage(models.Model):
    """Модель этапа работы"""
    number = models.IntegerField('Номер этапа')
    title = models.CharField('Название этапа', max_length=200)
    description = RichTextField('Описание')
    icon = models.CharField('Иконка (FontAwesome)', max_length=50,
                            default='fa-solid fa-pen-ruler')
    order = models.IntegerField('Порядок сортировки', default=0)

    class Meta:
        verbose_name = 'Этап работы'
        verbose_name_plural = 'Этапы работы'
        ordering = ['order']

    def __str__(self):
        return f"Этап {self.number}: {self.title}"
