from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import About, Statistic, Contact
from projects.models import Project
from services.models import Service
from stages.models import Stage
from .forms import ApplicationForm


class IndexView(TemplateView):
    """Главная страница"""
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем данные для главной
        context['about'] = About.objects.first()
        context['statistics'] = Statistic.objects.all()
        context['contacts'] = Contact.objects.first()
        context['featured_projects'] = Project.objects.filter(is_featured=True)[:6]
        context['services'] = Service.objects.all()
        context['stages'] = Stage.objects.all()[:6]
        context['form'] = ApplicationForm()

        return context

    def post(self, request, *args, **kwargs):
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
        return self.get(request, *args, **kwargs)


def success_view(request):
    """Страница успешной отправки"""
    return render(request, 'main/success.html')


from django.http import FileResponse
from django.shortcuts import get_object_or_404
import os
from django.conf import settings
from .models import BriefDownload


def download_brief(request):
    """Функция для скачивания брифа с отслеживанием"""
    # Сохраняем информацию о скачивании
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    BriefDownload.objects.create(ip_address=ip)

    # Путь к файлу
    file_path = os.path.join(settings.BASE_DIR, 'static', 'files', 'brief.pdf')

    # Отправляем файл
    response = FileResponse(open(file_path, 'rb'), as_attachment=True, filename='brief.pdf')
    return response
