from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Project, ProjectCategory


class ProjectListView(ListView):
    """Список всех проектов"""
    model = Project
    template_name = 'projects/project_list.html'
    context_object_name = 'projects'
    paginate_by = 9  # Показывать по 9 проектов на странице

    def get_queryset(self):
        queryset = super().get_queryset()
        # Фильтрация по категории, если указана
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProjectCategory.objects.all()
        # Добавляем выбранную категорию для подсветки в меню
        context['current_category'] = self.request.GET.get('category', '')
        return context


class ProjectDetailView(DetailView):
    """Детальная страница проекта"""
    model = Project
    template_name = 'projects/project_detail.html'
    context_object_name = 'project'

    # Добавьте эту строку, чтобы искать по slug, а не по id
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['related_projects'] = Project.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:3]
        return context

