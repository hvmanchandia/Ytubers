# Generated by Django 3.1.5 on 2021-01-11 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0002_slider_field_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='slider',
            old_name='field_name',
            new_name='weblink',
        ),
    ]
