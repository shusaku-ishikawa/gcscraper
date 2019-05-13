from django.shortcuts import render
from django.views import generic
from .models import *

class Top(generic.TemplateView):
    template_name = 'main_top.html'

class PageList(generic.ListView):
    model = Page
    template_name = 'main_page_list.html'