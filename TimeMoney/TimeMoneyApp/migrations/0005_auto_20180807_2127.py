# Generated by Django 2.1 on 2018-08-07 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeMoneyApp', '0004_auto_20180807_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeevent',
            name='event_start',
            field=models.DateTimeField(),
        ),
    ]