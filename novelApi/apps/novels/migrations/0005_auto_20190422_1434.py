# Generated by Django 2.2 on 2019-04-22 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0004_auto_20190422_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novel',
            name='cover',
            field=models.URLField(blank=True, default='https://qiniu.tuscanyyy.top/cover.jpg', help_text='封面', null=True, verbose_name='封面'),
        ),
    ]
