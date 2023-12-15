from django.shortcuts import render, HttpResponse
from .forms import UserForm
from .models import Person
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            return HttpResponse(f'Name: {name}')
        else:
            return HttpResponse(f'Данные не валидны')
        name = request.POST.get('name')
        return HttpResponse(f'Name: {name}')
    form = UserForm()
    return render(request, 'app/index.html', context={'form': form})


def getData(request):
    tom = Person.objects.get_or_create(name='Tom', age=12)
    mike = Person.objects.get_or_create(name='Mike', age=98)

    try:
        men = Person.objects.get(name='Tom')
    except ObjectDoesNotExist:
        return HttpResponse('Not Found')

    people = Person.objects.all()
    return render(request, 'app/data.html', context={'data': people})
