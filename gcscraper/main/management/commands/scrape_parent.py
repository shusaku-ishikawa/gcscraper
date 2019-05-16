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


def run():
    #ベースページのURL
    baseurl = 'https://baseconnect.in/companies/category/79525d9e-2fec-4e30-b088-b29d596ecaa7'

    #ベースページのHTMLソースを取得
    html = requests.get(baseurl)

    #取得したHTMLをパース
    soup = BeautifulSoup(html.content, "html.parser")

    #ベースページの中のリンクのリストを取得
    searches_result_list = soup.find_all("div", {"class": "searches__result__list"})
    for result in searches_result_list:
        
        sleep(0.5)
        # 会社名
        detail_page_link = result.find('h4', { "class": 'searches__result__list__header__title'}).find('a')
        print(detail_page_link.getText())

        full_url_to_detail_page = urljoin(baseurl, detail_page_link['href'])
        try:
            company_page_content = requests.get(full_url_to_detail_page).content
            parsed = BeautifulSoup(company_page_content, 'html.parser')
            # 基本情報
            # basic_info = parsed.find_all('dl', {'class': 'cf'})
            # for info in basic_info:
            #     print(info.find('dt').getText())
            #     print(info.find('dd').getText())
            
            # 法人番号
            company_code_node = parsed.find('div', {'class': 'node__header__number cf'}).find('p')
            company_code_node.find('span').decompose()
            company_code = company_code_node.getText()

            # HP
            hp_links = parsed.find('div', { 'class': 'node__box node__contact'}).find_all('a')
            for link in hp_links:
                if link.getText() == '会社サイト':
                    print('hp:' + link['href'])
                    exist = Page.objects.filter(page_url = link['href'])
                    if len(exist) > 0:
                        page = exist[0]
                    else:
                        page = Page(page_url = link['href'])
            page.code = company_code
            page.company_name = detail_page_link.getText()
            
            # scriptタグの除去
            for script in parsed.find_all('script', src=False):
                script.decompose()

            page.page_html = parsed.find('body').getText()
        except:
            page.page_html = '取得失敗'
        
            
        page.display_order = (Page.objects.all().aggregate(Max('display_order'))['display_order__max'] or 0) + 1
        page.save()
        
# BaseCommandを継承して作成
class Command(BaseCommand):
    # python manage.py help count_entryで表示されるメッセージ
    help = '残り日数を１減らします。'

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        run()
