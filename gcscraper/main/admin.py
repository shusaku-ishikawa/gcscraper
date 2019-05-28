from django.contrib import admin
from .models import *
from django.contrib.admin.views.main import ChangeList
from django.contrib.admin.utils import quote
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _



class MyCompanyHomePageAdmin(admin.ModelAdmin):
    list_display = ( 'page_url', 'page_html',  'code', 'comment', 'company_name', 'phone_number', 'is_callable')

class MyLinkPageAdmin(admin.ModelAdmin):
    list_display = ('parent', 'page_url', 'page_html')

class MyGroupAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(CompanyHomePage, MyCompanyHomePageAdmin)
admin.site.register(LinkPage, MyLinkPageAdmin)
admin.site.register(Group, MyGroupAdmin)

