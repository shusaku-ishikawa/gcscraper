from django.db import models

class Group(models.Model):
    name = models.CharField(
        verbose_name = '名前',
        max_length = 100,
        blank = True,
        default = ''
    )
    display_order = models.IntegerField(
        verbose_name = '表示順',
        default = 1,
    )
    memo = models.TextField(
        default = ""
    )


class CompanyHomePage(models.Model):


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
    company_name_kana = models.CharField(
        verbose_name = '読み方',
        max_length = 255,
        null = True,
        blank = True,
        default = ""
    )
    market_cap = models.BigIntegerField(
        verbose_name = '時価総額',
        blank = True,
        null = True,
        
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
    memo = models.TextField(
        verbose_name = 'メモ',
        default = ''
    )


class PageGroup(models.Model):
    class Meta:
        ordering = ['display_order']
    group = models.ForeignKey(
        to = Group,
        verbose_name = 'グループ',
        on_delete = models.CASCADE,
        related_name = 'pages',
    )

    page = models.ForeignKey(
        to = CompanyHomePage,
        null = True,
        on_delete = models.CASCADE,
        related_name = 'groups',
    )

    display_order = models.IntegerField(
        verbose_name = '表示順',
        default = 1
    )


class LinkPage(models.Model):
    parent = models.ForeignKey(
        to = CompanyHomePage,
        on_delete = models.CASCADE,
        verbose_name = '親ページ',
        related_name = 'links'
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
    is_scrape_success = models.BooleanField(
        verbose_name = '取得成功',
        default = True
    )