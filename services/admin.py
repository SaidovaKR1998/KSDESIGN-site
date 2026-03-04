from django.contrib import admin
from .models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_m2', 'order')
    list_editable = ('order',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'description', 'price_per_m2', 'order')
        }),
        ('Что входит в услугу', {
            'fields': (
                'includes_measure', 'includes_layout', 'includes_installation',
                'includes_plumbing', 'includes_3d_layout', 'includes_collage',
                'includes_electric', 'includes_floors', 'includes_ceilings',
                'includes_materials', 'includes_walls', 'includes_3d'
            )
        }),
    )
