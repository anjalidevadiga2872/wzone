# Generated by Django 3.2.14 on 2022-08-04 14:16

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='service',
            name='other_details',
            field=ckeditor.fields.RichTextField(),
        ),
    ]