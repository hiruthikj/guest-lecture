# Generated by Django 3.1.7 on 2021-03-12 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0004_applications_time_registered'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='description',
            field=models.CharField(default='No description', max_length=100, verbose_name='Descrtiption'),
        ),
        migrations.AddField(
            model_name='event',
            name='summary',
            field=models.TextField(blank=True, null=True, verbose_name='Summary'),
        ),
    ]
