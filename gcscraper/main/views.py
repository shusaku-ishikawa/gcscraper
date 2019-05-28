from django.shortcuts import render
from django.views import generic
from .models import *
from django.db.models import F, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseBadRequest, JsonResponse
import operator
from .serializer import *
import json

class Top(LoginRequiredMixin, generic.TemplateView):
    
    template_name = 'main_top.html'
    def get_context_data(self, **kwargs):
        context = super(Top, self).get_context_data(**kwargs)
        group_search = self.request.GET.get('group_keywords')
        link_search = self.request.GET.get('link_keywords')
        if group_search:
            groups = Group.objects.all()
            q = group_search.split(' ')
            query = reduce(operator.and_, (Q(name__icontains = item) for item in q))
            return groups.filter(query)
            
        elif link_search:
            companies = CompanyHomePage.objects.all()
            satisfy = []
            for company in companies:
                
                q = link_search.split(' ')
                query = reduce(operator.or_, (Q(page_html__icontains = item) for item in q))
                satisfy_links = company.links.filter(query)
                if len(satisfy_links) > 0:
                    satisfy.push(company.pk)
            return CompanyHomePage.objects.filter(pk__in = satisfy)

class CompanyHomePageList(LoginRequiredMixin, generic.ListView):
    model = CompanyHomePage
    template_name = 'main_page_list.html'
    def get_queryset(self):
        qs = CompanyHomePage.objects.all().order_by('display_order')
        return qs


class GroupList(LoginRequiredMixin, generic.ListView):
    model = Group
    template_name = 'main_group_list.html'

def get_all_pages(request):
    if request.user.is_anonymous or request.user.is_active == False:
        return JsonResponse({'error' : 'authentication failed'}, status=401)
    
    if request.method == 'GET':
        qs = CompanyHomePage.objects.all()
        ret_json = PageSerializer(qs, many = True).data
        return JsonResponse(ret_json, safe = False)

def delete_page(request):
    if request.user.is_anonymous or request.user.is_active == False:
        return JsonResponse({'error' : 'authentication failed'}, status=401)
    
    if request.method == 'POST':
        CompanyHomePage.objects.get(pk = request.POST.get('pk')).delete()
        return JsonResponse({'success': True})
     
def create_blank_page_row(request):
    if request.user.is_anonymous or request.user.is_active == False:
        return JsonResponse({'error' : 'authentication failed'}, status=401)

    if request.method == 'POST':
        new_page = CompanyHomePage()
        
        insert_at = request.POST.get('insert_at')
        after = CompanyHomePage.objects.get(pk = insert_at)
        new_page.display_order = after.display_order + 1
        # update following rows
        CompanyHomePage.objects.filter(display_order__gte = after.display_order + 1).update(display_order = F("display_order") + 1)
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

        target = CompanyHomePage.objects.get(pk = pk)
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
            CompanyHomePage.objects.filter(pk = order_list[i]).update(display_order = i + 1)

        return JsonResponse({'success': True})

def add_to_group(request):
    if request.user.is_anonymous or request.user.is_active == False:
        return JsonResponse({'error' : 'authentication failed'}, status=401)
    
    if request.method == 'POST':
        group_id = request.POST.get('group_id')
        code = request.POST.get('code')
        if group_id == None or code == None:
            return JsonResponse({'error': True});
        
        try:
            group = Group.objects.get(pk = group_id)
            page = CompanyHomePage.objects.get(code = code)
        except Exception as e:
            print(str(e.args))
            return JsonResponse({'error': str(e.args)})
        
        exist = PageGroup.objects.filter(group = group, page = page)
        if len(exist) > 0:
            return JsonResponse({'error':True})
        pagegroup = PageGroup(group = group, page = page)
        pagegroup.save()

        data = PageSerializer(page, many = False).data
        return JsonResponse(data)
        
        
def delete_from_group(request):
    if request.user.is_anonymous or request.user.is_active == False:
        return JsonResponse({'error' : 'authentication failed'}, status=401)
    
    if request.method == 'POST':
        group_id = request.POST.get('group_id')
        code = request.POST.get('code')
        if group_id == None or code == None:
            print('no parma')
            return JsonResponse({'error': True});
        
        try:
            group = Group.objects.get(pk = group_id)
            page = CompanyHomePage.objects.get(code = code)
        except Exception as e:
            print(str(e.args))
            return JsonResponse({'error': str(e.args)})
        
        exist = PageGroup.objects.filter(group = group, page = page)
        if len(exist) == 0:
            print('no exist')
            return JsonResponse({'error':True})
        
        for rec in exist:
            rec.delete()

        return JsonResponse({'success': True})
        
        


