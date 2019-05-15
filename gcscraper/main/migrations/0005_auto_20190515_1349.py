# Generated by Django 2.1.5 on 2019-05-15 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190514_0922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='code',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='コード'),
        ),
        migrations.AlterField(
            model_name='page',
            name='company_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='会社名'),
        ),
        migrations.AlterField(
            model_name='page',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='main.Group', verbose_name='グループ'),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_html',
            field=models.TextField(blank=True, null=True, verbose_name='html'),
        ),
        migrations.AlterField(
            model_name='page',
            name='page_url',
            field=models.URLField(blank=True, max_length=128, null=True, verbose_name='ページURL'),
        ),
        migrations.AlterField(
            model_name='page',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, verbose_name='電話番号'),
        ),
    ]
