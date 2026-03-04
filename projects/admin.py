from django.contrib import admin
from .models import ProjectCategory, Project, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3

@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'area', 'year', 'is_featured', 'pdf_file')
    list_filter = ('category', 'is_featured', 'year')
    search_fields = ('title', 'description')
    inlines = [ProjectImageInline]
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'category', 'description', 'area', 'year')
        }),
        ('Медиафайлы', {
            'fields': ('main_image', 'pdf_file'),
            'description': 'Загрузите главное фото и PDF-файл с подробным описанием'
        }),
        ('Настройки отображения', {
            'fields': ('is_featured',)
        }),
    )
