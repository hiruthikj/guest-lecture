# Generated by Django 3.1.2 on 2021-05-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0011_auto_20210404_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='allow_ext',
            field=models.BooleanField(default=False, verbose_name='Allow External Users'),
        ),
    ]
