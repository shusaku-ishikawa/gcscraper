# Generated by Django 2.1.5 on 2019-06-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20190605_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='linkpage',
            name='is_scrape_success',
            field=models.BooleanField(default=True, verbose_name='取得成功'),
        ),
        migrations.AlterField(
            model_name='companyhomepage',
            name='market_cap',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='時価総額'),
        ),
    ]
