# Generated by Django 3.2.14 on 2022-07-25 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='service_type',
            field=models.CharField(choices=[('Photographer', 'Photographer'), ('Venue', 'Venue')], max_length=100),
        ),
    ]