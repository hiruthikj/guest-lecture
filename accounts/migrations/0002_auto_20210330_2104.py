# Generated by Django 3.1.7 on 2021-03-30 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='user_type',
            field=models.CharField(choices=[('STUD', 'Student'), ('FCLT', 'Faculty'), ('CIR', 'CIR Faculty'), ('GUEST', 'Guest Lecturer'), ('OTHER', 'External Students')], max_length=10, verbose_name='User Type'),
        ),
    ]
