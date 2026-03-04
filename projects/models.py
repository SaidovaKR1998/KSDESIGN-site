from django.db import models
from django.utils.text import slugify
from django.utils.crypto import get_random_string

class ProjectCategory(models.Model):
    """Категория проекта (квартира, кафе, офис)"""
    name = models.CharField('Название', max_length=100)

    class Meta:
        verbose_name = 'Категория проекта'
        verbose_name_plural = 'Категории проектов'

    def __str__(self):
        return self.name


class Project(models.Model):
    """Модель проекта"""
    title = models.CharField('Название проекта', max_length=200)
    slug = models.SlugField('URL', max_length=200, unique=True, blank=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL,
                                 null=True, verbose_name='Категория')
    description = models.TextField('Описание')
    area = models.IntegerField('Площадь, м²', null=True, blank=True)
    year = models.IntegerField('Год реализации', null=True, blank=True)
    main_image = models.ImageField('Главное фото', upload_to='projects/')
    pdf_file = models.FileField('PDF-файл с проектом', upload_to='projects/pdfs/',
                                null=True, blank=True)
    is_featured = models.BooleanField('Показывать на главной', default=False)
    created_at = models.DateTimeField('Дата добавления', auto_now_add=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Если slug не указан, создаем из названия
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            # Проверяем, существует ли уже такой slug
            counter = 1
            while Project.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)


class ProjectImage(models.Model):
    """Дополнительные изображения проекта"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='images', verbose_name='Проект')
    image = models.ImageField('Изображение', upload_to='projects/gallery/')
    is_main = models.BooleanField('Главное фото', default=False)

    class Meta:
        verbose_name = 'Изображение проекта'
        verbose_name_plural = 'Изображения проектов'
