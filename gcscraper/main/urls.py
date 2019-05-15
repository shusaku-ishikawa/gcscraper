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
    path('li/', views.PageList.as_view(), name="page_list"),
    path('g-li/', views.GroupList.as_view(), name="group_list"),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('new_page/', views.create_blank_page_row, name="new_page"),
    path('delete_page/', views.delete_page, name="delete_page"),
    path('update_page/', views.update_page_field, name="update_page"),
    path('update_order/', views.update_order, name = 'update_order')
]

