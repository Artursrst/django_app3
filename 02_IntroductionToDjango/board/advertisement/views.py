from django.shortcuts import render
from django.http import HttpResponse

def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisement/advertisement_list.html', {})

def anxiety_detail(request, *args, **kwargs):
    return render(request, 'advertisement/anxiety_detail.html', {})

def russian_detail(request, *args, **kwargs):
    return render(request, 'advertisement/russian_detail.html', {})

def python_detail(request, *args, **kwargs):
    return render(request, 'advertisement/python_detail.html', {})

def SQL_detail(request, *args, **kwargs):
    return render(request, 'advertisement/SQL_detail.html', {})

def web_detail(request, *args, **kwargs):
    return render(request, 'advertisement/web_detail.html', {})