from django.db import models
from ckeditor.fields import RichTextField


class Service(models.Model):
    """Модель услуги"""
    name = models.CharField('Название услуги', max_length=200)
    description = RichTextField('Описание')
    price_per_m2 = models.DecimalField('Цена за м²', max_digits=10, decimal_places=2)
    order = models.IntegerField('Порядок сортировки', default=0)

    # Характеристики услуги (для списка)
    includes_measure = models.BooleanField('Обмерный план', default=False)
    includes_layout = models.BooleanField('Разработка планировки', default=False)
    includes_installation = models.BooleanField('Монтаж', default=False)
    includes_plumbing = models.BooleanField('Сантехника', default=False)
    includes_3d_layout = models.BooleanField('Объемная планировка', default=False)
    includes_collage = models.BooleanField('Коллаж', default=False)
    includes_electric = models.BooleanField('Электрика', default=False)
    includes_floors = models.BooleanField('План полов', default=False)
    includes_ceilings = models.BooleanField('План потолков', default=False)
    includes_materials = models.BooleanField('Отделочные материалы', default=False)
    includes_walls = models.BooleanField('Развертки стен', default=False)
    includes_3d = models.BooleanField('3D визуализация', default=False)

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['order']

    def __str__(self):
        return self.name

    def get_features_list(self):
        """Возвращает список характеристик для отображения"""
        features = []
        if self.includes_measure:
            features.append('Обмерный план')
        if self.includes_layout:
            features.append('Разработка планировки')
        if self.includes_installation:
            features.append('Монтаж')
        if self.includes_plumbing:
            features.append('Сантехника')
        if self.includes_3d_layout:
            features.append('Объемная планировка')
        if self.includes_collage:
            features.append('Коллаж каждой комнаты')
        if self.includes_electric:
            features.append('Электрика')
        if self.includes_floors:
            features.append('План полов')
        if self.includes_ceilings:
            features.append('План потолков')
        if self.includes_materials:
            features.append('Отделочные материалы с подсчетом')
        if self.includes_walls:
            features.append('Развертки стен')
        if self.includes_3d:
            features.append('3D визуализация')
        return features
