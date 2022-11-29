from django.shortcuts import render
from django.views import View, generic
from .models import Advertisement, AuthorInformation, Headings


class AdvertisementsListView(generic.ListView):
    model = Advertisement
    template_name = 'advertisements/advertisements_list.html'
    context_object_name = 'adv'

class AdvertisementsDetailView(generic.DetailView):
    model = Advertisement
    template_name = 'advertisements/advertisements_detail.html'

