# Generated by Django 4.2 on 2023-05-21 12:54

import ckeditor.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_remove_product_descrption_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content',
            field=ckeditor.fields.RichTextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
