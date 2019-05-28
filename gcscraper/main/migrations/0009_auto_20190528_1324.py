# Generated by Django 2.1.5 on 2019-05-28 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20190528_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pages', to='main.Group', verbose_name='グループ')),
            ],
        ),
        migrations.RemoveField(
            model_name='companyhomepage',
            name='group',
        ),
        migrations.AddField(
            model_name='pagegroup',
            name='page',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groups', to='main.CompanyHomePage'),
        ),
    ]