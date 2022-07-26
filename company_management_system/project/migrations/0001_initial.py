# Generated by Django 4.0.5 on 2022-06-22 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
        ('account', '0005_profile_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('deploy_date', models.DateField()),
                ('status', models.CharField(choices=[('Developing', 'Developing'), ('Requirment Gathering', 'Requirment Gathering'), ('Testing', 'Testing'), ('validating', 'Validating')], default='Developing', max_length=50)),
                ('amount', models.PositiveIntegerField(default=0)),
                ('paid_amount', models.PositiveIntegerField(default=0)),
                ('remainig_work', models.CharField(max_length=500)),
                ('customerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Customer_name', to='customer.customer')),
                ('project_manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.profile')),
            ],
        ),
    ]
