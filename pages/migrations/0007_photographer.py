# Generated by Django 3.2.14 on 2022-07-21 06:51

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20220721_0526'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photographer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('services', multiselectfield.db.fields.MultiSelectField(choices=[('Wedding Photography', 'Wedding Photography'), ('Portrait Photography', 'Portrait Photography'), ('Event Photography', 'Event Photography')], max_length=255)),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%y/%m/%d/')),
                ('facebook_link', models.URLField(max_length=255)),
                ('twitter_link', models.URLField(max_length=255)),
                ('linkedin_link', models.URLField(max_length=255)),
                ('price', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]