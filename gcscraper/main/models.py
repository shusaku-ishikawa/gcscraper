from django.db import models

class Group(models.Model):
    name = models.CharField(
        verbose_name = '名前',
        max_length = 100
    )
    display_order = models.IntegerField(
        verbose_name = '表示順',
        default = 1,
    )
    
    
class Page(models.Model):
    parent = models.ForeignKey(
        verbose_name = '親ページ',
        to = 'self',
        related_name = 'children',
        null = True,
        blank = True,
        on_delete = models.SET_NULL
    )
    group = models.ForeignKey(
        to = Group,
        verbose_name = 'グループ',
        on_delete = models.CASCADE,
        related_name = 'pages',
        blank = True,
        null = True
    )
    page_url = models.URLField(
        verbose_name = "ページURL", 
        max_length=128, 
        blank = True,
        null = True,
        default = ""
    )
    page_html = models.TextField(
        verbose_name = 'html',
        blank = True,
        null = True,
        default = ""
    )

    code = models.CharField(
        verbose_name = 'コード',
        max_length = 100,
        blank = True,
        null = True,
        default = ""
    )
    comment = models.CharField(
        verbose_name = '補足',
        max_length = 255,
        null = True,
        blank = True,
        default = ""
    )
    company_name = models.CharField(
        verbose_name = '会社名',
        max_length = 100,
        blank = True,
        null = True,
        default = ""
    )
    phone_number = models.CharField(
        verbose_name = '電話番号',
        max_length = 50,
        blank = True,
        default = ""
    )
    is_callable = models.BooleanField(
        verbose_name = '電話可能',
        default = False
    )
    display_order = models.IntegerField(
        verbose_name = '表示順',
        default = 1
    )
    
