from django.shortcuts import render
from django.views import generic
from .models import *
from django.db.models import F
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseBadRequest, JsonResponse

class Top(LoginRequiredMixin, generic.TemplateView):
    template_name = 'main_top.html'

class PageList(LoginRequiredMixin, generic.ListView):
    model = Page
    template_name = 'main_page_list.html'
    def get_queryset(self):
        qs = Page.objects.all().order_by('display_order')
        return qs


class GroupList(LoginRequiredMixin, generic.ListView):
    model = Group
    template_name = 'main_group_list.html'

def delete_page(request):
    if request.user.is_anonymous or request.user.is_active == False:
        return JsonResponse({'error' : 'authentication failed'}, status=401)
    
    if request.method == 'POST':
        Page.objects.get(pk = request.POST.get('pk')).delete()
        return JsonResponse({'success': True})
     
def create_blank_page_row(request):
    if request.user.is_anonymous or request.user.is_active == False:
        return JsonResponse({'error' : 'authentication failed'}, status=401)

    if request.method == 'POST':
        new_page = Page()
        
        insert_at = request.POST.get('insert_at')
        after = Page.objects.get(pk = insert_at)
        new_page.display_order = after.display_order + 1
        # update following rows
        Page.objects.filter(display_order__gte = after.display_order + 1).update(display_order = F("display_order") + 1)
        new_page.save()
        return JsonResponse({'success': True, 'pk': new_page.pk})

def update_page_field(request):
    if request.user.is_anonymous or request.user.is_active == False:
        return JsonResponse({'error' : 'authentication failed'}, status=401)

    if request.method == 'POST':
        
        pk = request.POST.get('pk')
        field_name = request.POST.get('field_name')
        field_value = request.POST.get('field_value')
        if field_value in ('true', 'false'):
            field_value = field_value == 'true'
            print(field_value)

        target = Page.objects.get(pk = pk)
        setattr(target, field_name, field_value)
        target.save()
        return JsonResponse({'success': True})

def update_order(request):
    if request.user.is_anonymous or request.user.is_active == False:
        return JsonResponse({'error' : 'authentication failed'}, status=401)

    if request.method == 'POST':
        orderstr = request.POST.get('order_str')
        order_list = orderstr.split(',')
        for i in range(len(order_list)):
            Page.objects.filter(pk = order_list[i]).update(display_order = i + 1)

        return JsonResponse({'success': True})