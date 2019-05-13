from django.db import models

class Page(models.Model):
    parent = models.ForeignKey(
        verbose_name = '親ページ',
        to = 'self',
        related_name = 'myparent',
        null = True,
        blank = True,
        on_delete = models.SET_NULL
    )
    page_url = models.URLField(
        verbose_name = "ページURL", 
        max_length=128, 
    )
    page_html = models.TextField(
        verbose_name = 'html'
    )

    code = models.CharField(
        verbose_name = 'コード',
        max_length = 100,
    )
    comment = models.CharField(
        verbose_name = '補足',
        max_length = 255,
        null = True,
        blank = True
    )
    company_name = models.CharField(
        verbose_name = '会社名',
        max_length = 100
    )
    phone_number = models.CharField(
        verbose_name = '電話番号',
        max_length = 50
    )
    is_callable = models.BooleanField(
        verbose_name = '電話可能',
        default = False
    )
    
