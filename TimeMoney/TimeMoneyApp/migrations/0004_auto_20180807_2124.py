# Generated by Django 2.1 on 2018-08-07 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TimeMoneyApp', '0003_timeevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timeevent',
            name='event_start',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]