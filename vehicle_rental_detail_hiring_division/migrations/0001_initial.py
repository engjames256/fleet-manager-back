# Generated by Django 2.2.7 on 2019-11-30 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleRentalDetailHiringDivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_rental_detail_hiring_division', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
