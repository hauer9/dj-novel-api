# Generated by Django 2.2 on 2019-04-26 00:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0008_auto_20190425_1736'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operation', '0009_auto_20190422_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='更新时间', verbose_name='更新时间')),
                ('novel', models.ForeignKey(help_text='作品', on_delete=django.db.models.deletion.CASCADE, to='novels.Novel', verbose_name='作品')),
                ('user', models.ForeignKey(help_text='用户', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': '搜索记录',
                'verbose_name_plural': '搜索记录',
                'ordering': ['-update_time'],
            },
        ),
    ]
