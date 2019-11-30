# Generated by Django 2.2.7 on 2019-11-30 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0004_auto_20191130_1814'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleDiary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waranty', models.CharField(max_length=60)),
                ('waranty_distance', models.CharField(max_length=60)),
                ('insurance_expiry', models.CharField(max_length=60)),
                ('insurance_commencement', models.CharField(max_length=60)),
                ('motor_insurance_policy_no', models.CharField(max_length=60)),
                ('mid_on', models.CharField(max_length=60)),
                ('mid_off', models.CharField(max_length=60)),
                ('insurance_certificate', models.CharField(max_length=60)),
                ('service_date', models.CharField(max_length=60)),
                ('last_service_type', models.CharField(max_length=60)),
                ('service_schedule', models.CharField(max_length=60)),
                ('service_interval_weeks', models.CharField(max_length=60)),
                ('service_interval_kms', models.CharField(max_length=60)),
                ('inspection_date', models.CharField(max_length=60)),
                ('inspection_type', models.CharField(max_length=60)),
                ('inspection_interval_weeks', models.CharField(max_length=60)),
                ('inspection_interval_distance', models.CharField(max_length=60)),
                ('inspection_certificate_no', models.CharField(max_length=60)),
                ('distance_per_year', models.CharField(max_length=60)),
                ('distance_per_day', models.CharField(max_length=60)),
                ('age_years', models.CharField(max_length=60)),
                ('age_days', models.CharField(max_length=60)),
                ('deviation', models.CharField(max_length=60)),
                ('deviation_perc', models.CharField(max_length=60)),
                ('odometer', models.CharField(max_length=60)),
                ('current_odo_date', models.CharField(max_length=60)),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle')),
                ('vehicle_insurance_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.VehicleInsuranceCompany')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleAssets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_no', models.CharField(max_length=60)),
                ('extra_registration_no', models.CharField(max_length=60)),
                ('asset_description', models.CharField(max_length=60)),
                ('asset_type', models.CharField(max_length=60)),
                ('asset_make', models.CharField(max_length=60)),
                ('asset_model', models.CharField(max_length=60)),
                ('asset_issue_date', models.CharField(max_length=60)),
                ('asset_return_date', models.CharField(max_length=60)),
                ('asset_serial', models.CharField(max_length=60)),
                ('driver_name', models.CharField(max_length=60)),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='VehicleAllocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('driver_name', models.CharField(max_length=60)),
                ('registratyion_no', models.CharField(max_length=60)),
                ('changed_by', models.CharField(max_length=60)),
                ('date', models.CharField(max_length=60)),
                ('company_code', models.CharField(max_length=60)),
                ('cost_center', models.CharField(max_length=60)),
                ('start_date', models.CharField(max_length=60)),
                ('odometer', models.CharField(max_length=60)),
                ('end_date', models.CharField(max_length=60)),
                ('end_odometer', models.CharField(max_length=60)),
                ('lock', models.CharField(max_length=60)),
                ('workshop', models.CharField(max_length=60)),
                ('allocation_reason', models.CharField(max_length=60)),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.Vehicle')),
            ],
        ),
    ]
