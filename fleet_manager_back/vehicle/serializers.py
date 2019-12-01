from rest_framework import serializers
from .models import (
    VehicleInsuranceCompany,
    VehicleSummary,
    Vehicle,
    VehicleClient,
    VehicleBodyType,
    VehicleCompanyCode,
    VehicleConventionType,
    VehicleCostCenter,
    VehicleCountry,
    VehicleCounty,
    VehicleCurrencyCodes,
    VehicleDeductability,
    VehicleFuelType,
    VehicleGearBox,
    VehicleInPull,
    VehicleLocationCode,
    VehicleMakeCode,
    VehicleModelCode,
    VehicleReturnedWorkshop,
    VehicleStatus,
    VehicleType,
    VehicleTyre,
    VehicleBasic,
    VehicleDiary,
    VehicleInsuranceCompany,
    VehicleAllocation,
    VehicleAssets,
    VehicleNotes,
    VehicleRepair,
    RepairSupply,
    RepairDescription,
    RepairWorkshop,
    RepairReason,
    RepairJobStatus,
    RepairPaperworkStatus,
    RepairEstimationCost,
    RepairInvoiceDetails,
    RepairInvoicedTo,
    RepairRecievedBy,
    RepairInvoiceRecieved,
    RepairInvoicePaid,
    RepairRecharge,
    RepairServiceHistory,
    VehicleAccident,
    AccidentType,
    TypeOfLossClaim,
    AccidentStatus,
    LiabilityFlag,
    BrokersName,
    PartyToBlame,
    AccidentDescription,
    ClaimFormRecieved,
    ClaimPoliceAbstract,
    DriverLicenseRecieved,
    ClaimRepairEstimate,
    ClaimInspectionReport,
    AccidentBasic,
    Driver,
    Relationship,
    OtherVehicleInvolved,
    CostCenter,
    Weather,
    RoadType,
    RoadConditions,
    DamageToVehicle,
    VehicleBroken,
    DoorsLocked,
    EntryGained,
    VehicleRecovered,
    AccidentDetails,
    ThirdPartiesInvolved,
    AccidentVor,
    WriteOff,
    AccidentCosts,
)


class AccidentCostsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentCosts
        fields = "__all__"


class WriteOffSerializer(serializers.ModelSerializer):
    class Meta:
        model = WriteOff
        fields = "__all__"


class AccidentVorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentVor
        fields = "__all__"


class ThirdPartiesInvolvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdPartiesInvolved
        fields = "__all__"


class AccidentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentDetails
        fields = "__all__"


class VehicleRecoveredSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleRecovered
        fields = "__all__"


class EntryGainedSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntryGained
        fields = "__all__"


class DoorsLockedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoorsLocked
        fields = "__all__"


class VehicleBrokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBroken
        fields = "__all__"


class DamageToVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DamageToVehicle
        fields = "__all__"


class RoadConditionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadConditions
        fields = "__all__"


class RoadTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadType
        fields = "__all__"


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = "__all__"


class CostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CostCenter
        fields = "__all__"


class OtherVehicleInvolvedSerializer(serializers.ModelSerializer):
    class Meta:
        model = OtherVehicleInvolved
        fields = "__all__"


class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = "__all__"


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class AccidentBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentBasic
        fields = "__all__"


class ClaimInspectionReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimInspectionReport
        fields = "__all__"


class ClaimRepairEstimateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimRepairEstimate
        fields = "__all__"


class DriverLicenseRecievedSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverLicenseRecieved
        fields = "__all__"


class ClaimPoliceAbstractSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimPoliceAbstract
        fields = "__all__"


class ClaimFormRecievedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClaimFormRecieved
        fields = "__all__"


class AccidentDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentDescription
        fields = "__all__"


class PartyToBlameSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartyToBlame
        fields = "__all__"


class BrokersNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrokersName
        fields = "__all__"


class LiabilityFlagSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiabilityFlag
        fields = "__all__"


class AccidentStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentStatus
        fields = "__all__"


class AccidentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccidentType
        fields = "__all__"


class TypeOfLossClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfLossClaim
        fields = "__all__"


class VehicleAccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleAccident
        fields = "__all__"


class RepairServiceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairServiceHistory
        fields = "__all__"


class RepairRechargeSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairRecharge
        fields = "__all__"


class RepairInvoicePaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairInvoicePaid
        fields = "__all__"


class RepairInvoiceRecievedSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairInvoiceRecieved
        fields = "__all__"


class RepairRecievedBySerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairRecievedBy
        fields = "__all__"


class RepairInvoicedToSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairInvoicedTo
        fields = "__all__"


class RepairInvoiceDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairInvoiceDetails
        fields = "__all__"


class RepairEstimationCostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairEstimationCost
        fields = "__all__"


class RepairPaperworkStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairPaperworkStatus
        fields = "__all__"


class RepairJobStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairJobStatus
        fields = "__all__"


class RepairReasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairReason
        fields = "__all__"


class RepairWorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairWorkshop
        fields = "__all__"


class RepairDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairDescription
        fields = "__all__"


class RepairSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = RepairSupply
        fields = "__all__"


class VehicleRepairSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleRepair
        fields = "__all__"


class VehicleNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleNotes
        fields = "__all__"


class VehicleAssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleAssets
        fields = "__all__"


class VehicleAllocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleAllocation
        fields = "__all__"


class VehicleInsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInsuranceCompany
        fields = "__all__"


class VehicleDiarySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDiary
        fields = "__all__"


class VehicleCompanyCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCompanyCode
        fields = "__all__"


class VehicleBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBasic
        fields = "__all__"


class VehicleSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleSummary
        fields = "__all__"


class VehicleInsuranceCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInsuranceCompany
        fields = "__all__"


class VehicleTyreSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleTyre
        fields = "__all__"


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = "__all__"


class VehicleStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleStatus
        fields = "__all__"


class VehicleReturnedWorkshopSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleReturnedWorkshop
        fields = "__all__"


class VehicleModelCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleModelCode
        fields = "__all__"


class VehicleMakeCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleMakeCode
        fields = "__all__"


class VehicleLocationCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleLocationCode
        fields = "__all__"


class VehicleInPullSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleInPull
        fields = "__all__"


class VehicleGearBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleGearBox
        fields = "__all__"


class VehicleFuelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleFuelType
        fields = "__all__"


class VehicleDeductabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDeductability
        fields = "__all__"


class VehicleCurrencyCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCurrencyCodes
        fields = "__all__"


class VehicleCountySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCounty
        fields = "__all__"


class VehicleCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCountry
        fields = "__all__"


class VehicleCostCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCostCenter
        fields = "__all__"


class VehicleConventionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleConventionType
        fields = "__all__"


class VehicleCompanyCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleCompanyCode
        fields = "__all__"


class VehicleBodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleBodyType
        fields = "__all__"


class VehicleClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleClient
        fields = "__all__"


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = "__all__"
