# Generated by Django 3.1.5 on 2021-01-15 13:46

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0002_auto_20210115_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='descrption',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
