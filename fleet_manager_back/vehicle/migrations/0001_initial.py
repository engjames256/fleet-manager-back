# Generated by Django 2.2.7 on 2019-11-30 06:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle_currency_codes', '0001_initial'),
        ('vehicle_status', '0001_initial'),
        ('vehicle_company_code', '0001_initial'),
        ('vehicle_cost_center', '0001_initial'),
        ('vehicle_model_code', '0001_initial'),
        ('vehicle_fuel_type', '0001_initial'),
        ('vehicle_convention_type', '0001_initial'),
        ('vehicle_client', '0001_initial'),
        ('vehicle_country', '0001_initial'),
        ('vehicle_county', '0001_initial'),
        ('vehicle_location_code', '0001_initial'),
        ('vehicle_tyre', '0001_initial'),
        ('vehicle_returned_workshop', '0001_initial'),
        ('vehicle_body_type', '0001_initial'),
        ('vehicle_make_code', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_no', models.CharField(max_length=60)),
                ('extra_registration_no', models.CharField(max_length=60)),
                ('cost_per_km', models.CharField(max_length=60)),
                ('cumilative_balance', models.CharField(max_length=60)),
                ('number_of_remining_tyres', models.CharField(max_length=60)),
                ('l_per_km', models.CharField(max_length=60)),
                ('next_inspection', models.CharField(max_length=60)),
                ('total_cost', models.CharField(max_length=60)),
                ('next_service', models.CharField(max_length=60)),
                ('estimated_odometer', models.CharField(max_length=60)),
                ('year', models.CharField(max_length=60)),
                ('fleet_number', models.CharField(max_length=60)),
                ('date_registered', models.DateTimeField(auto_now_add=True)),
                ('date_returned_to_workshop', models.DateTimeField(auto_now_add=True)),
                ('vehicle_body_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_body_type.VehicleBodyType')),
                ('vehicle_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_client.VehicleClient')),
                ('vehicle_company_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_company_code.VehicleCompanyCode')),
                ('vehicle_convention_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_convention_type.VehicleConventionType')),
                ('vehicle_cost_center', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_cost_center.VehicleCostCenter')),
                ('vehicle_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_country.VehicleCountry')),
                ('vehicle_county', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_county.VehicleCounty')),
                ('vehicle_currency_codes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_currency_codes.VehicleCurrencyCodes')),
                ('vehicle_fuel_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_fuel_type.VehicleFuelType')),
                ('vehicle_location_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_location_code.VehicleLocationCode')),
                ('vehicle_make_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_make_code.VehicleMakeCode')),
                ('vehicle_model_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_model_code.VehicleModelCode')),
                ('vehicle_returned_workshop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_returned_workshop.VehicleReturnedWorkshop')),
                ('vehicle_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_status.VehicleStatus')),
                ('vehicle_tyre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle_tyre.VehicleTyre')),
            ],
        ),
    ]
