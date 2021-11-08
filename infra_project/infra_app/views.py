from django.http import HttpResponse


def index(request):
    return HttpResponse('У меня здорово получилось!')


def second_page(request):
    return HttpResponse('А это вторая страница!')
