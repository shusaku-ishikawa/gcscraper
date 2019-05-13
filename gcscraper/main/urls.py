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
]

