# Generated by Django 2.2 on 2020-06-20 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_readnum'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='readed_num',
        ),
    ]
