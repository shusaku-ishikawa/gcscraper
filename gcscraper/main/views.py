from django.shortcuts import render
from django.views import generic
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin

class Top(LoginRequiredMixin, generic.TemplateView):
    template_name = 'main_top.html'

class PageList(LoginRequiredMixin, generic.ListView):
    model = Page
    template_name = 'main_page_list.html'

class GroupList(LoginRequiredMixin, generic.ListView):
    model = Group
    template_name = 'main_group_list.html'