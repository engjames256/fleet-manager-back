from django.db import models
class AccidentCosts(models.Model):
    accident_costs_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.accident_costs_name
class WriteOff(models.Model):
    write_off_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.write_off_name
class AccidentVor(models.Model):
    accident_vor_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.accident_vor_name
class ThirdPartiesInvolved(models.Model):
    third_parties_involved_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.third_parties_involved_name
class AccidentDetails(models.Model):
    accident_details_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.accident_details_name
class VehicleRecovered(models.Model):
    vehicle_recovered_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_recovered_name
class EntryGained(models.Model):
    entry_gained_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.entry_gained_name

class DoorsLocked(models.Model):
    doors_locked_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.doors_locked_name
class VehicleBroken(models.Model):
    vehicle_broken_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.vehicle_broken_name
class DamageToVehicle(models.Model):
    damage_to_vehicle_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.damage_to_vehicle_name
class RoadConditions(models.Model):
    road_conditions_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.road_conditions_name
class RoadType(models.Model):
    road_type_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.road_type_name
class Weather(models.Model):
    weather_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.weather_name
class CostCenter(models.Model):
    cost_center_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cost_center_name
class OtherVehicleInvolved(models.Model):
    other_vehicle_involved_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.other_vehicle_involved_name
class Relationship(models.Model):
    relationship_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.relationship_name
class Driver(models.Model):
    driver_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.driver_name
class AccidentBasic(models.Model):
    accident_basic_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.accident_basic_name

class ClaimInspectionReport(models.Model):
    claim_inspection_report_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.claim_inspection_report_name

class ClaimRepairEstimate(models.Model):
    claim_repair_estimate_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.claim_repair_estimate_name

class DriverLicenseRecieved(models.Model):
    driver_license_recieved_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.driver_license_recieved_name

class ClaimPoliceAbstract(models.Model):
    claim_police_abstract_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.claim_police_abstract_name

class ClaimFormRecieved(models.Model):
    claim_form_recieved_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.claim_form_recieved_name

class AccidentDescription(models.Model):
    accident_description_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.accident_description_name

class CompanyCode(models.Model):
    company_code_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_code_name

class PartyToBlame(models.Model):
    party_to_blame_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.party_to_blame_name

class BrokersName(models.Model):
    brokers_name_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.brokers_name_name

class LiabilityFlag(models.Model):
    liability_flag_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.liability_flag_name

class AccidentStatus(models.Model):
    accident_status_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.accident_status_name

class TypeOfLossClaim(models.Model):
    type_of_loss_claim_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type_of_loss_claim_name

class AccidentType(models.Model):
    accident_type_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.accident_type_name

class RepairServiceHistory(models.Model):
    repair_recharge_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repair_recharge_name

class RepairRecharge(models.Model):
    repair_recharge_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repair_recharge_name

class RepairInvoicePaid(models.Model):
    repair_invoice_paid_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repair_invoice_paid_name

class RepairInvoiceRecieved(models.Model):
    repair_invoice_recieved_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.repair_invoice_recieved_name

class RepairRecievedBy(models.Model):
    repair_recieved_by_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repair_recieved_by_name

class RepairInvoicedTo(models.Model):
    repair_invoiced_to_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repair_invoiced_to_name

class RepairInvoiceDetails(models.Model):
    repair_invoice_details_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repair_job_status_name

class RepairEstimationCost(models.Model):
    repair_estimation_cost_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repair_estimation_cost_name

class RepairPaperworkStatus(models.Model):
    repair_paperwork_status_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repair_paperwork_status_name

class RepairJobStatus(models.Model):
    repair_job_status_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repair_job_status_name

class RepairReason(models.Model):
    repair_reason_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repair_reason_name

class RepairWorkshop(models.Model):
    repair_workshop_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repair_workshop_name

class RepairDescription(models.Model):
    repair_description_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repair_description_name

class RepairSupply(models.Model):
    repair_supply_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.repair_supply_name

class VehicleInsuranceCompany(models.Model):
    insurance_company_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.insurance_company_name

class VehicleTyre(models.Model):
    tyre_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.tyre_name

class VehicleType(models.Model):
    type_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type_name

class VehicleStatus(models.Model):
    status_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_name

class VehicleReturnedWorkshop(models.Model):
    returned_workshop_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.returned_workshop_name

class VehicleModelCode(models.Model):
    model_code_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.model_code_name

class VehicleMakeCode(models.Model):
    make_code_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.make_code_name

class VehicleLocationCode(models.Model):
    location_code_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location_code_name

class VehicleInPull(models.Model):
    in_pull_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.in_pull_name

class VehicleGearBox(models.Model):
    gear_box_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gear_box_name

class VehicleFuelType(models.Model):
    fuel_type_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fuel_type_name

class VehicleDeductability(models.Model):
    deductability_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.deductability_name

class VehicleCurrencyCodes(models.Model):
    currency_codes_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.currency_codes_name

class VehicleCounty(models.Model):
    county_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.county_name

class VehicleCountry(models.Model):
    country_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.country_name

class VehicleCostCenter(models.Model):
    cost_center_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.cost_center_name

class VehicleConventionType(models.Model):
    convention_type_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.convention_type_name

class VehicleCompanyCode(models.Model):
    company_code_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_code_name

class VehicleBodyType(models.Model):
    body_type_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body_type_name

class VehicleClient(models.Model):
    client_name = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name

class Vehicle(models.Model):
    registration_no = models.CharField(max_length=60)
    extra_registration_no = models.CharField(max_length=60)
    year = models.CharField(max_length=60)
    fleet_number = models.CharField(max_length=60)
    date_registered = models.DateTimeField(auto_now_add=True)
    date_returned_to_workshop = models.DateTimeField(auto_now_add=True)
    vehicle_tyre = models.ForeignKey(VehicleTyre, on_delete=models.CASCADE)
    vehicle_body_type = models.ForeignKey(VehicleBodyType, on_delete=models.CASCADE)
    vehicle_client = models.ForeignKey(VehicleClient, on_delete=models.CASCADE)
    vehicle_company_code = models.ForeignKey(
        VehicleCompanyCode, on_delete=models.CASCADE
    )
    vehicle_convention_type = models.ForeignKey(
        VehicleConventionType, on_delete=models.CASCADE
    )
    vehicle_cost_center = models.ForeignKey(VehicleCostCenter, on_delete=models.CASCADE)
    vehicle_fuel_type = models.ForeignKey(VehicleFuelType, on_delete=models.CASCADE)
    vehicle_make_code = models.ForeignKey(VehicleMakeCode, on_delete=models.CASCADE)
    vehicle_model_code = models.ForeignKey(VehicleModelCode, on_delete=models.CASCADE)
    vehicle_returned_workshop = models.ForeignKey(
        VehicleReturnedWorkshop, on_delete=models.CASCADE
    )
    vehicle_status = models.ForeignKey(VehicleStatus, on_delete=models.CASCADE)
    vehicle_county = models.ForeignKey(VehicleCounty, on_delete=models.CASCADE)
    vehicle_location_code = models.ForeignKey(
        VehicleLocationCode, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.registration_no

class VehicleSummary(models.Model):
    estimated_odometer = models.CharField(max_length=250)
    location_code_name = models.ForeignKey(
        VehicleLocationCode, on_delete=models.CASCADE
    )
    vehicle_country = models.ForeignKey(VehicleCountry, on_delete=models.CASCADE)
    next_service = models.CharField(max_length=60)
    next_inspection = models.CharField(max_length=60)
    vehicle_currency_codes = models.ForeignKey(
        VehicleCurrencyCodes, on_delete=models.CASCADE
    )
    in_pull_name = models.ForeignKey(VehicleInPull, on_delete=models.CASCADE)
    l_per_km = models.CharField(max_length=60)
    cost_per_km = models.CharField(max_length=60)
    total_cost = models.CharField(max_length=60)
    number_of_remining_tyres = models.CharField(max_length=60)
    cumilative_balance = models.CharField(max_length=60)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class VehicleBasic(models.Model):
    exterior_color = models.CharField(max_length=60)
    vehicle_gear_box = models.ForeignKey(VehicleGearBox, on_delete=models.CASCADE)
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
    vehicle_deductability = models.ForeignKey(
        VehicleDeductability, on_delete=models.CASCADE
    )
    gross_vehicle_weight = models.CharField(max_length=60)
    winter_tyres = models.CharField(max_length=60)
    winter_tyres_location = models.CharField(max_length=60)
    tank_size = models.CharField(max_length=60)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class VehicleDiary(models.Model):
    waranty = models.CharField(max_length=60)
    waranty_distance = models.CharField(max_length=60)
    vehicle_insurance_company = models.ForeignKey(
        VehicleInsuranceCompany, on_delete=models.CASCADE
    )
    insurance_expiry = models.CharField(max_length=60)
    insurance_commencement = models.CharField(max_length=60)
    insurance_certificate = models.CharField(max_length=60)
    motor_insurance_policy_no = models.CharField(max_length=60)
    mid_on = models.CharField(max_length=60)
    mid_off = models.CharField(max_length=60)
    insurance_certificate = models.CharField(max_length=60)
    service_date = models.CharField(max_length=60)
    last_service_type = models.CharField(max_length=60)
    service_schedule = models.CharField(max_length=60)
    service_interval_weeks = models.CharField(max_length=60)
    service_interval_kms = models.CharField(max_length=60)
    inspection_date = models.CharField(max_length=60)
    inspection_type = models.CharField(max_length=60)
    inspection_interval_weeks = models.CharField(max_length=60)
    inspection_interval_distance = models.CharField(max_length=60)
    inspection_certificate_no = models.CharField(max_length=60)
    distance_per_year = models.CharField(max_length=60)
    distance_per_day = models.CharField(max_length=60)
    age_years = models.CharField(max_length=60)
    age_days = models.CharField(max_length=60)
    deviation = models.CharField(max_length=60)
    deviation_perc = models.CharField(max_length=60)
    odometer = models.CharField(max_length=60)
    current_odo_date = models.CharField(max_length=60)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class VehicleRepair(models.Model):
    job_authorization_no = models.CharField(max_length=60)
    repair_supply = models.ForeignKey(RepairSupply, on_delete=models.CASCADE)
    created_by = models.CharField(max_length=60)
    registration_no = models.CharField(max_length=60)
    sales_outlet = models.CharField(max_length=60)
    insurance_company = models.CharField(max_length=60)
    alias_plate_number = models.CharField(max_length=60)
    sap_account_number = models.CharField(max_length=60)
    cumilative_balance = models.CharField(max_length=60)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class RepairDescription(models.Model):
    repair_workshop = models.ForeignKey(RepairWorkshop, on_delete=models.CASCADE)
    division_client = models.CharField(max_length=60)
    repair_reason = models.ForeignKey(RepairReason, on_delete=models.CASCADE)
    service_type = models.CharField(max_length=60)
    job_date = models.CharField(max_length=60)
    job_end_date = models.CharField(max_length=60)
    odometer_in = models.CharField(max_length=60)
    odometer_out = models.CharField(max_length=60)
    days_off_road = models.CharField(max_length=60)
    cost_center = models.CharField(max_length=60)
    service_advice = models.CharField(max_length=60)
    repair_job_status = models.ForeignKey(RepairJobStatus, on_delete=models.CASCADE)
    repair_paperwork_status = models.ForeignKey(
        RepairPaperworkStatus, on_delete=models.CASCADE
    )
    cost_parts = models.CharField(max_length=60)
    cost_labour = models.CharField(max_length=60)
    cost_total_net = models.CharField(max_length=60)
    comments = models.CharField(max_length=60)
    repair_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class RepairEstimationCost(models.Model):
    actual_labour_cost = models.CharField(max_length=60)
    actual_parts_cost = models.CharField(max_length=60)
    actual_tax_cost = models.CharField(max_length=60)
    estimated_hours = models.CharField(max_length=60)
    actual_total_gross = models.CharField(max_length=60)
    actual_total_net = models.CharField(max_length=60)
    repair_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class RepairInvoiceDetails(models.Model):
    repair_invoiced_to = models.ForeignKey(RepairInvoicedTo, on_delete=models.CASCADE)
    invoice_date = models.CharField(max_length=60)
    invoice_no = models.CharField(max_length=60)
    repair_recieved_by = models.ForeignKey(RepairRecievedBy, on_delete=models.CASCADE)
    repair_invoiced_recieved = models.ForeignKey(
        RepairInvoiceRecieved, on_delete=models.CASCADE
    )
    invoice_recieved_date = models.CharField(max_length=60)
    repair_invoiced_paid = models.ForeignKey(
        RepairInvoicePaid, on_delete=models.CASCADE
    )
    invoice_parts = models.CharField(max_length=60)
    invoice_labour = models.CharField(max_length=60)
    total_invoice = models.CharField(max_length=60)
    repair_recharge = models.ForeignKey(RepairRecharge, on_delete=models.CASCADE)
    invoice_comment = models.CharField(max_length=60)
    total_tax = models.CharField(max_length=60)
    location_code = models.CharField(max_length=60)
    total_gross = models.CharField(max_length=60)
    repair_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class RepairServiceHistory(models.Model):
    job_authorization_no = models.CharField(max_length=60)
    workshop = models.CharField(max_length=60)
    job_status = models.CharField(max_length=60)
    registration_no = models.CharField(max_length=60)
    extra_registration_no = models.CharField(max_length=60)
    model_code = models.CharField(max_length=60)
    division_code = models.CharField(max_length=60)
    cost_center = models.CharField(max_length=60)
    odometer_in = models.CharField(max_length=60)
    reason = models.CharField(max_length=60)
    job_date= models.CharField(max_length=60)
    job_end_date = models.CharField(max_length=60)
    invoice = models.CharField(max_length=60)
    total_invoice = models.CharField(max_length=60)
    comments = models.CharField(max_length=60)
    repair_paperwork_status = models.CharField(max_length=60)
    created_by = models.CharField(max_length=60)
    cost_labour = models.CharField(max_length=60)
    created_by = models.CharField(max_length=60)
    date = models.CharField(max_length=60)
    changed_by = models.CharField(max_length=60)
    date = models.CharField(max_length=60)
    repair_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class VehicleAccident(models.Model):
    accident_ref = models.CharField(max_length=60)
    date = models.CharField(max_length=60)
    claim_handler = models.CharField(max_length=60)
    created_by = models.CharField(max_length=60)
    accident_type = models.ForeignKey(AccidentType, on_delete=models.CASCADE)
    accident_report_from_recieved = models.CharField(max_length=60)
    date_claim_completed = models.CharField(max_length=60)
    type_of_loss_claim = models.ForeignKey(TypeOfLossClaim, on_delete=models.CASCADE)
    date_insurers_notified = models.CharField(max_length=60)
    accident_status = models.ForeignKey(AccidentStatus, on_delete=models.CASCADE)
    insurance_reference = models.CharField(max_length=60)
    liability_flag = models.ForeignKey(LiabilityFlag, on_delete=models.CASCADE)
    brokers_name = models.ForeignKey(BrokersName, on_delete=models.CASCADE)
    broker_reference = models.CharField(max_length=60)
    party_to_blame = models.ForeignKey(PartyToBlame, on_delete=models.CASCADE)
    company_code = models.ForeignKey(CompanyCode, on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class AccidentDescription(models.Model):
    claim_form_recieved = models.ForeignKey(ClaimFormRecieved, on_delete=models.CASCADE)
    claim_police_abstract = models.ForeignKey(ClaimPoliceAbstract, on_delete=models.CASCADE)
    driver_license_recieved = models.ForeignKey(DriverLicenseRecieved, on_delete=models.CASCADE)
    claim_repair_estimate = models.ForeignKey(ClaimRepairEstimate, on_delete=models.CASCADE)
    claim_inspection_report = models.ForeignKey(ClaimInspectionReport, on_delete=models.CASCADE)
    accident_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class AccidentBasic(models.Model):
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    driver_name= models.CharField(max_length=60)
    date_of_birth = models.CharField(max_length=60)
    relationship = models.ForeignKey(Relationship, on_delete=models.CASCADE)
    force_number = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=60)
    other_vehicle_involved = models.ForeignKey(OtherVehicleInvolved, on_delete=models.CASCADE)
    cost_center = models.ForeignKey(CostCenter, on_delete=models.CASCADE)
    registration_no = models.CharField(max_length=60)
    extra_registration_no = models.CharField(max_length=60)
    make_code = models.CharField(max_length=60)
    model_code = models.CharField(max_length=60)
    client_division = models.CharField(max_length=60)
    engiene_cc = models.CharField(max_length=60)
    fuel_type = models.CharField(max_length=60)
    insurance_company = models.CharField(max_length=60)
    owner = models.CharField(max_length=60)
    pending_convictions = models.CharField(max_length=60)
    towing_company = models.CharField(max_length=60)
    towing_from = models.CharField(max_length=60)
    towing_to = models.CharField(max_length=60)
    contact_person = models.CharField(max_length=60)
    phone_number = models.CharField(max_length=60)
    towing_date = models.CharField(max_length=60)
    your_vehicle_light = models.CharField(max_length=60)
    your_vehicle_signaling = models.CharField(max_length=60)
    other_vehicle_light = models.CharField(max_length=60)
    other_vehicle_signaling = models.CharField(max_length=60)
    accident_date = models.CharField(max_length=60)
    exact_time_of_incident = models.CharField(max_length=60)
    exact_time_of_accident = models.CharField(max_length=60)
    comment = models.CharField(max_length=60)
    incident_time_range = models.CharField(max_length=60)
    weather= models.ForeignKey(Weather, on_delete=models.CASCADE)
    road_type= models.ForeignKey(RoadType, on_delete=models.CASCADE)
    road_conditions= models.ForeignKey(RoadConditions, on_delete=models.CASCADE)
    use_of_vehicle_at_time_of_incident = models.CharField(max_length=60)
    current_location_of_vehicle = models.CharField(max_length=60)
    damage_to_vehicle= models.ForeignKey(DamageToVehicle, on_delete=models.CASCADE)
    vehicle_defect_damage = models.CharField(max_length=60)
    vehicle_broken= models.ForeignKey(VehicleBroken, on_delete=models.CASCADE)
    doors_locked= models.ForeignKey(DoorsLocked, on_delete=models.CASCADE)
    entry_gained= models.ForeignKey(EntryGained, on_delete=models.CASCADE)
    vehicle_recovered= models.ForeignKey(VehicleRecovered, on_delete=models.CASCADE)
    accident_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class AccidentDetails(models.Model):
    third_parties_involved= models.ForeignKey(ThirdPartiesInvolved, on_delete=models.CASCADE)
    accident_ref = models.CharField(max_length=60)
    item_number = models.CharField(max_length=60)
    accident_date = models.CharField(max_length=60)
    name = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    Telephone = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    tp_insur_comp = models.CharField(max_length=60)
    tp_insur_comp_address = models.CharField(max_length=60)
    tp_insur_comp_telephone = models.CharField(max_length=60)
    tp_policy = models.CharField(max_length=60)
    tp_dem_desc = models.CharField(max_length=60)
    tp_veh = models.CharField(max_length=60)
    exterior_color = models.CharField(max_length=60)
    third_party_registration_no = models.CharField(max_length=60)
    accident_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class AccidentVor(models.Model):
    write_off= models.ForeignKey(WriteOff, on_delete=models.CASCADE)
    accident_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)


class AccidentCosts(models.Model):
    estimated_accident_damage = models.CharField(max_length=60)
    estimated_towing_costs = models.CharField(max_length=60)
    estimated_associated_costs = models.CharField(max_length=60)
    estimated_suplimentary_costs = models.CharField(max_length=60)
    estimated_wild_screen_glass_costs = models.CharField(max_length=60)
    estimated_total_costs = models.CharField(max_length=60)
    actual_accident_damage = models.CharField(max_length=60)
    actual_towing_costs = models.CharField(max_length=60) 
    actual_associated_costs = models.CharField(max_length=60)
    actual_suplimentary_costs = models.CharField(max_length=60)
    actual_wild_screen_glass_costs = models.CharField(max_length=60)
    actual_total_costs = models.CharField(max_length=60)
    accident_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
class VehicleAllocation(models.Model):
    driver_name = models.CharField(max_length=60)
    registratyion_no = models.CharField(max_length=60)
    changed_by = models.CharField(max_length=60)
    date = models.CharField(max_length=60)
    company_code = models.CharField(max_length=60)
    cost_center = models.CharField(max_length=60)
    start_date = models.CharField(max_length=60)
    odometer = models.CharField(max_length=60)
    end_date = models.CharField(max_length=60)
    end_odometer = models.CharField(max_length=60)
    lock = models.CharField(max_length=60)
    workshop = models.CharField(max_length=60)
    allocation_reason = models.CharField(max_length=60)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class VehicleAssets(models.Model):
    registration_no = models.CharField(max_length=60)
    extra_registration_no = models.CharField(max_length=60)
    asset_description = models.CharField(max_length=60)
    asset_type = models.CharField(max_length=60)
    asset_make = models.CharField(max_length=60)
    asset_model = models.CharField(max_length=60)
    asset_issue_date = models.CharField(max_length=60)
    asset_return_date = models.CharField(max_length=60)
    asset_serial = models.CharField(max_length=60)
    driver_name = models.CharField(max_length=60)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

class VehicleNotes(models.Model):
    date = models.CharField(max_length=60)
    contract_baloon_payment = models.CharField(max_length=60)
    notes = models.CharField(max_length=60)
    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

