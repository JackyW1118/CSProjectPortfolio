# Generated by Django 3.1.5 on 2021-03-27 01:40

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0037_auto_20210326_1736'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myinformation',
            name='home_page_hero_text',
        ),
        migrations.AlterField(
            model_name='myinformation',
            name='about_page_description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
