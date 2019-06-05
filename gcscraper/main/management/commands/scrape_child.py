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

def run():
    #ベースページのURL
    for parent in CompanyHomePage.objects.all():
        #ベースページのHTMLソースを取得
       
        html = requests.get(parent.page_url)

        #取得したHTMLをパース
        soup = BeautifulSoup(html.content, "html.parser")

        all_links = soup.find_all('a')
        for link in all_links:
            
            # check if it's absolute path
            if re.match("^(http|https)://.*?$", link['href']):
                absolute_path = link['href']
            elif re.match("^javascript:.*", link['href']):
                break
            else:
                absolute_path = urljoin(parent.page_url, link['href'])
            print(absolute_path)
            exist = LinkPage.objects.filter(page_url = absolute_path)
            if len(exist) > 0:
                obj = exist[0]
            else:
                obj = LinkPage(page_url = absolute_path, parent = parent)
            try:
                page = requests.get(absolute_path).content
                page_parsed = BeautifulSoup(page, "html.parser")
                # scriptタグの除去
                for script in page_parsed.find_all('script', src=False):
                    script.decompose()
                body = page_parsed.find('body')
                if body != None:
                    obj.page_html = body.getText()
                obj.save()
            except Exception as e:
                print(str(e.args))
                obj.is_scrape_success = False
            finally:
                obj.save()
       
                

# BaseCommandを継承して作成
class Command(BaseCommand):
    # python manage.py help count_entryで表示されるメッセージ
    help = 'リンク先ページのクロール'

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        run()
