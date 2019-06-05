import logging
import os
from django.utils import timezone
from django.core.management.base import BaseCommand
from django.template.loader import get_template
from datetime import datetime, timedelta
from ...models import *
from django.conf import settings
from django.db.models import Max
import sys, re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from time import sleep
import re

def trim_jika(jikastr):
    no_comma = re.sub(',', '', jikastr)
    return int(re.sub('百万円', '000000', no_comma))

def run():
    #ベースページのURL
    base_url = "https://minkabu.jp/stock/"
    
    for page in CompanyHomePage.objects.all():
        url = base_url + page.code

        #ページのHTMLソースを取得
        html = requests.get(url)

        #取得したHTMLをパース
        soup = BeautifulSoup(html.content, "html.parser")

        if len(soup.find_all(string="URLが間違っているか、ページが削除された可能性があります。")) > 0:
            continue
        jika_table = soup.find('table', class_ = "md_table tlno simple md_table_vertical")
        jika_sogaku = jika_table.find_all('td')[1].getText()
        page.market_cap = trim_jika(jika_sogaku)
        page.save()

# BaseCommandを継承して作成
class Command(BaseCommand):
    # python manage.py help count_entryで表示されるメッセージ
    help = 'リンク先ページのクロール'

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        run()
