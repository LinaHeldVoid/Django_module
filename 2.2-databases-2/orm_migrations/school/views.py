from django.shortcuts import render

from .models import Student


def students_list(request):
    ordering = 'group'
    object_list = Student.objects.order_by(ordering)
    template = 'school/students_list.html'
    context = {
        'students': object_list
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = 'group'

    return render(request, template, context)
