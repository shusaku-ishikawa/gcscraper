from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField
from .models import *
from django.core.exceptions import ObjectDoesNotExist


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('pk', 'name', 'display_order', 'memo')


class PageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CompanyHomePage
        fields = ('pk', 'page_url', 'page_html', 'code', 'comment', 'company_name', 'market_cap', 'phone_number', 'is_callable', 'display_order')

class PageGroupSerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only = True, many = False)
    page = PageSerializer(read_only = True, many = False)
    class Meta:
        model = PageGroup
        fields = ('pk', 'group', 'page')