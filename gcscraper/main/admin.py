from django.contrib import admin
from .models import *
from django.contrib.admin.views.main import ChangeList
from django.contrib.admin.utils import quote
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.utils.translation import ugettext_lazy as _



class MyPageAdmin(admin.ModelAdmin):
    list_display = ('page_url', 'page_html',  'code', 'comment', 'company_name', 'phone_number', 'is_callable')

admin.site.register(Page, MyPageAdmin)

