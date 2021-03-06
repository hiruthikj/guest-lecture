# Generated by Django 3.1.7 on 2021-03-01 18:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_code', models.CharField(max_length=10, unique=True, verbose_name='Department Code')),
                ('dept_name', models.CharField(max_length=50, verbose_name='Department Name')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=200, verbose_name='Event Name')),
                ('start_date', models.DateTimeField(blank=True, null=True, verbose_name='Start Date')),
                ('end_date', models.DateTimeField(blank=True, null=True, verbose_name='End Date')),
                ('max_seats', models.PositiveIntegerField(blank=True, null=True, verbose_name='Maximum Seats')),
                ('place', models.CharField(max_length=200, verbose_name='Location')),
                ('status', models.CharField(choices=[('ON', 'On-Schedule'), ('COMP', 'Completed'), ('X', 'Cancelled'), ('TNTV', 'Tentative')], default='ON', max_length=20, verbose_name='Status')),
                ('type', models.CharField(choices=[('CIR', 'CIR'), ('DEPT', 'Department'), ('OTHER', 'Other')], default='CIR', max_length=20, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_no', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Registration Number')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Account')),
                ('dept_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lecture.department', verbose_name='Department')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Account')),
                ('dept_fk', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='lecture.department', verbose_name='Department')),
            ],
        ),
        migrations.CreateModel(
            name='ExternalUsers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Account')),
            ],
        ),
        migrations.CreateModel(
            name='CIRFaculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Account')),
            ],
        ),
    ]
