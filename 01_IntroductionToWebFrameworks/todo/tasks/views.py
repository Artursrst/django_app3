from django.http import HttpResponse
import random
from django.views import View




class ToDoView(View):

    def get(self, request, *args, **kwargs):

        tasks = ['task1', 'task2', 'task3', 'task4', 'task5', 'task6', 'task7', 'task8', 'task9', 'task10']
        tasks_to_do = random.sample(tasks, k=10)

        return HttpResponse('<ul>'
                            '<li>{}</li>'
                            '<li>{}</li>'
                            '<li>{}</li>'
                            '<li>{}</li>'
                            '<li>{}</li>'
                            '</ul>'.format(tasks_to_do[0],
                                           tasks_to_do[1],
                                           tasks_to_do[2],
                                           tasks_to_do[3],
                                           tasks_to_do[4]))
