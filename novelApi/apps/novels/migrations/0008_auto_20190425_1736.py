# Generated by Django 2.2 on 2019-04-25 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('novels', '0007_auto_20190425_1523'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chapter',
            old_name='last_update_time',
            new_name='update_time',
        ),
    ]
