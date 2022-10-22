from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

c = [0]

class Advertisements(View):
    def get(self, request):
        advertisements = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура',
            'Ремонт техники'
        ]
        return render(request, 'advertisements/advertisements.html', {'advertisements':advertisements})

    def post(self, request):
        c[0] += 1
        text = 'Запрос на создание новой записи успешно выполнен, вы создали {} запросов'.format(str(c[0]))
        return render(request, 'advertisements/advertisements.html', {'text': text})

class Head(View):
    def get(self, request):
        categories = [
            'Личные вещи',
            'Транспорт',
            'Хобби',
            'Отдых'
        ]
        regions = [
            'Москва',
            'Московская область',
            'Республика Алтай',
            'Вологодская область'
        ]

        return render(request, 'advertisements/head.html', {'categories':categories, 'regions':regions})

class Contacts(TemplateView):

    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = 'ул. Новочеркасская д. 7 кв. 17'
        context['phone'] = '8-800-708-19-45'
        context['email'] = 'sales@company.com'

        return context

class About(TemplateView):

    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Бесплатные объявления'
        context['description'] = 'Бесплатные объявления в вашем городе'

        return context

