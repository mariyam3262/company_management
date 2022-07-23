# Generated by Django 4.0.5 on 2022-06-29 07:38

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
        ('account', '0006_alter_profile_category_alter_profile_rewards'),
        ('attendance', '0002_attendance_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 6, 29, 13, 8, 0, 474481)),
        ),
        migrations.CreateModel(
            name='DailyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(default='Developer', max_length=30)),
                ('date', models.DateField(default=datetime.datetime(2022, 6, 29, 13, 8, 0, 475479))),
                ('performedTask_today', models.CharField(max_length=1000)),
                ('performedTask_next_day', models.CharField(blank=True, max_length=1000)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
                ('working_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
    ]
