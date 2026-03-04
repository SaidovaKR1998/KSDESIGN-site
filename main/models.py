from django.db import models
from ckeditor.fields import RichTextField


class About(models.Model):
    """Модель для раздела 'Обо мне'"""
    title = models.CharField('Заголовок', max_length=200)
    content = RichTextField('Содержание')
    image = models.ImageField('Фото', upload_to='about/')

    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'

    def __str__(self):
        return self.title


class Statistic(models.Model):
    """Статистика (100+ проектов и т.д.)"""
    label = models.CharField('Название', max_length=100)
    value = models.CharField('Значение', max_length=50)
    icon = models.CharField('Иконка (FontAwesome)', max_length=50, blank=True)

    class Meta:
        verbose_name = 'Статистика'
        verbose_name_plural = 'Статистика'

    def __str__(self):
        return f"{self.value} {self.label}"


class Contact(models.Model):
    """Контактная информация"""
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email')

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.name


class Application(models.Model):
    """Заявки с сайта"""
    name = models.CharField('Имя', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    email = models.EmailField('Email')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    is_processed = models.BooleanField('Обработано', default=False)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f"{self.name} - {self.created_at}"


class BriefDownload(models.Model):
    """Модель для отслеживания скачиваний брифа"""
    downloaded_at = models.DateTimeField('Дата скачивания', auto_now_add=True)
    ip_address = models.GenericIPAddressField('IP адрес', null=True, blank=True)

    class Meta:
        verbose_name = 'Скачивание брифа'
        verbose_name_plural = 'Скачивания брифа'
