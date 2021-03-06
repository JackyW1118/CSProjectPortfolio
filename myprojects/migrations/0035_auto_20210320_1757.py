# Generated by Django 3.1.5 on 2021-03-21 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myprojects', '0034_auto_20210314_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='project',
            name='key_features',
        ),
        migrations.AddField(
            model_name='project',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]
