# Generated by Django 4.2 on 2023-05-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_alter_whatsapp_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='descrption',
        ),
        migrations.AlterField(
            model_name='product',
            name='small_descrption',
            field=models.TextField(max_length=1000),
        ),
    ]
