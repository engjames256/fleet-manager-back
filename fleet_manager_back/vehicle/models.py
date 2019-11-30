from django.db import models
from vehicle_tyre.models import VehicleTyre
from vehicle_body_type.models import VehicleBodyType
from vehicle_client.models import VehicleClient
from vehicle_company_code.models import VehicleCompanyCode
from vehicle_convention_type.models import VehicleConventionType
from vehicle_cost_center.models import VehicleCostCenter
from vehicle_country.models import VehicleCountry
from vehicle_fuel_type.models import VehicleFuelType
from vehicle_make_code.models import VehicleMakeCode
from vehicle_model_code.models import VehicleModelCode
from vehicle_returned_workshop.models import VehicleReturnedWorkshop
from vehicle_status.models import VehicleStatus
from vehicle_county.models import VehicleCounty
from vehicle_location_code.models import VehicleLocationCode
from vehicle_currency_codes.models import VehicleCurrencyCodes
from vehicle_deductability.models import VehicleDeductability
from vehicle_gear_box.models import VehicleGearBox

# Create your models here.


class Vehicle(models.Model):
    registration_no = models.CharField(max_length=60)
    extra_registration_no = models.CharField(max_length=60)
    cost_per_km = models.CharField(max_length=60)
    cumilative_balance = models.CharField(max_length=60)
    number_of_remining_tyres = models.CharField(max_length=60)
    l_per_km = models.CharField(max_length=60)
    next_inspection = models.CharField(max_length=60)
    total_cost = models.CharField(max_length=60)
    next_service = models.CharField(max_length=60)
    estimated_odometer = models.CharField(max_length=60)
    year = models.CharField(max_length=60)
    fleet_number = models.CharField(max_length=60)
    exterior_color = models.CharField(max_length=60)
    ecoscore = models.CharField(max_length=60)
    interior_color = models.CharField(max_length=60)
    number_of_doors = models.CharField(max_length=60)
    co2km = models.CharField(max_length=60)
    key_number = models.CharField(max_length=60)
    chassis_number = models.CharField(max_length=60)
    fiscal_hp = models.CharField(max_length=60)
    engiene_number = models.CharField(max_length=60)
    engiene_cc = models.CharField(max_length=60)
    distance_to_work = models.CharField(max_length=60)
    vehicle_phone_number = models.CharField(max_length=60)
    bhp = models.CharField(max_length=60)
    gross_vehicle_weight = models.CharField(max_length=60)
    winter_tyres = models.CharField(max_length=60)
    winter_tyres_location = models.CharField(max_length=60)
    tank_size = models.CharField(max_length=60)
    date_registered = models.DateTimeField(auto_now_add=True)
    date_returned_to_workshop = models.DateTimeField(auto_now_add=True)
    vehicle_tyre = models.ForeignKey(VehicleTyre, on_delete=models.CASCADE)
    vehicle_body_type = models.ForeignKey(VehicleBodyType, on_delete=models.CASCADE)
    vehicle_client = models.ForeignKey(VehicleClient, on_delete=models.CASCADE)
    vehicle_company_code = models.ForeignKey(VehicleCompanyCode, on_delete=models.CASCADE)
    vehicle_convention_type = models.ForeignKey(VehicleConventionType, on_delete=models.CASCADE)
    vehicle_cost_center = models.ForeignKey(VehicleCostCenter, on_delete=models.CASCADE)
    vehicle_country = models.ForeignKey(VehicleCountry, on_delete=models.CASCADE)
    vehicle_fuel_type= models.ForeignKey(VehicleFuelType, on_delete=models.CASCADE)
    vehicle_make_code= models.ForeignKey(VehicleMakeCode, on_delete=models.CASCADE)
    vehicle_model_code= models.ForeignKey(VehicleModelCode, on_delete=models.CASCADE)
    vehicle_returned_workshop= models.ForeignKey(VehicleReturnedWorkshop, on_delete=models.CASCADE)
    vehicle_status= models.ForeignKey(VehicleStatus, on_delete=models.CASCADE)
    vehicle_county= models.ForeignKey(VehicleCounty, on_delete=models.CASCADE)
    vehicle_location_code= models.ForeignKey(VehicleLocationCode, on_delete=models.CASCADE)
    vehicle_currency_codes= models.ForeignKey(VehicleCurrencyCodes, on_delete=models.CASCADE)
    vehicle_deductability= models.ForeignKey(VehicleDeductability, on_delete=models.CASCADE)
    vehicle_gear_box= models.ForeignKey(VehicleGearBox, on_delete=models.CASCADE)

    def __str__(self):
        return self.registration_no