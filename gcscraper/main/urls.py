from django.urls import path
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView  

app_name = 'main'
admin.site.site_title = 'ゲーム会社スクレーパー' 
admin.site.site_header = 'XXXX' 
admin.site.index_title = 'Menu'

urlpatterns = [
    path('', LoginView.as_view(template_name = 'admin/login.html'), name='login'),
    path('top/', views.Top.as_view(), name="top"),
    path('li/', views.CompanyHomePageList.as_view(), name="page_list"),
    path('g-li/', views.GroupList.as_view(), name="group_list"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('pages/', views.get_all_pages, name = 'get_all_pages'),
    path('add_new_page/', views.add_new_page, name="add_new_page"),
    path('delete_page/', views.delete_page, name="delete_page"),
    path('update_page_field/', views.update_page_field, name="update_page_field"),
    path('update_order/', views.update_order, name = 'update_order'),
    path('add_to_group/', views.add_to_group, name = 'add_to_group'),
    path('add_group_memo/', views.add_group_memo, name = 'add_group_memo'),
    path('update_group_memo/', views.update_group_memo, name = 'update_group_memo'),
    
    path('update_page_order/', views.update_group_order, name="update_group_order"),
    
    path('update_group_page_order/', views.update_group_page_order, name="update_group_page_order"),

    path('delete_from_group/', views.delete_from_group, name = 'delete_from_group'),
    path('add_new_group/', views.add_new_group, name = 'add_new_group'),
    path('update_group_field/', views.update_group_field, name = 'update_group_field'),
    path('delete_group/', views.delete_group, name = 'delete_group')
    
]

