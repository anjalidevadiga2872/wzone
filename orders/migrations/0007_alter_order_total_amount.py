# Generated by Django 3.2.14 on 2022-07-24 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20220724_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total_amount',
            field=models.CharField(default=0, max_length=100),
        ),
    ]