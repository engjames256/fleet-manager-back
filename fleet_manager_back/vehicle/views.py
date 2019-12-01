from rest_framework import viewsets
from .models import (
    VehicleInsuranceCompany,
    Vehicle,
    VehicleClient,
    VehicleBodyType,
    VehicleConventionType,
    VehicleCostCenter,
    VehicleCompanyCode,
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
    VehicleSummary,
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
from .serializers import (
    VehicleInsuranceCompanySerializer,
    VehicleSerializer,
    VehicleClientSerializer,
    VehicleBodyTypeSerializer,
    VehicleCompanyCodeSerializer,
    VehicleConventionTypeSerializer,
    VehicleCostCenterSerializer,
    VehicleCountrySerializer,
    VehicleCountySerializer,
    VehicleCurrencyCodesSerializer,
    VehicleDeductabilitySerializer,
    VehicleFuelTypeSerializer,
    VehicleGearBoxSerializer,
    VehicleInPullSerializer,
    VehicleLocationCodeSerializer,
    VehicleMakeCodeSerializer,
    VehicleModelCodeSerializer,
    VehicleReturnedWorkshopSerializer,
    VehicleStatusSerializer,
    VehicleTypeSerializer,
    VehicleTyreSerializer,
    VehicleSummarySerializer,
    VehicleBasicSerializer,
    VehicleDiarySerializer,
    VehicleInsuranceCompanySerializer,
    VehicleAllocationSerializer,
    VehicleAssetsSerializer,
    VehicleNotesSerializer,
    VehicleRepairSerializer,
    RepairSupplySerializer,
    RepairDescriptionSerializer,
    RepairWorkshopSerializer,
    RepairReasonSerializer,
    RepairJobStatusSerializer,
    RepairPaperworkStatusSerializer,
    RepairEstimationCostSerializer,
    RepairInvoiceDetailsSerializer,
    RepairInvoicedToSerializer,
    RepairRecievedBySerializer,
    RepairInvoiceRecievedSerializer,
    RepairInvoicePaidSerializer,
    RepairRechargeSerializer,
    RepairServiceHistorySerializer,
    VehicleAccidentSerializer,
    AccidentTypeSerializer,
    TypeOfLossClaimSerializer,
    AccidentStatusSerializer,
    LiabilityFlagSerializer,
    BrokersNameSerializer,
    PartyToBlameSerializer,
    AccidentDescriptionSerializer,
    ClaimFormRecievedSerializer,
    ClaimPoliceAbstractSerializer,
    DriverLicenseRecievedSerializer,
    ClaimRepairEstimateSerializer,
    ClaimInspectionReportSerializer,
    AccidentBasicSerializer,
    DriverSerializer,
    RelationshipSerializer,
    OtherVehicleInvolvedSerializer,
    CostCenterSerializer,
    WeatherSerializer,
    RoadTypeSerializer,
    RoadConditionsSerializer,
    DamageToVehicleSerializer,
    VehicleBrokenSerializer,
    DoorsLockedSerializer,
    EntryGainedSerializer,
    VehicleRecoveredSerializer,
    AccidentDetailsSerializer,
    ThirdPartiesInvolvedSerializer,
    AccidentVorSerializer,
    WriteOffSerializer,
    AccidentCostsSerializer,
)
from rest_framework.permissions import IsAuthenticated


class AccidentCotsView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = AccidentCosts.objects.all()
    serializer_class = AccidentCostsSerializer


class WriteOffView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = WriteOff.objects.all()
    serializer_class = WriteOffSerializer


class AccidentVorView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = AccidentVor.objects.all()
    serializer_class = AccidentVorSerializer


class ThirdPartiesInvolvedView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = ThirdPartiesInvolved.objects.all()
    serializer_class = ThirdPartiesInvolvedSerializer


class AccidentDetailsView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = AccidentDetails.objects.all()
    serializer_class = AccidentDetailsSerializer


class VehicleRecoveredView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleRecovered.objects.all()
    serializer_class = VehicleRecoveredSerializer


class EntryGainedView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = EntryGained.objects.all()
    serializer_class = EntryGainedSerializer


class DoorsLockedView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = DoorsLocked.objects.all()
    serializer_class = DoorsLockedSerializer


class VehicleBrokenView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleBroken.objects.all()
    serializer_class = VehicleBrokenSerializer


class DamageToVehicleView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = DamageToVehicle.objects.all()
    serializer_class = DamageToVehicleSerializer


class RoadConditionsView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RoadConditions.objects.all()
    serializer_class = RoadConditionsSerializer


class RoadTypeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RoadType.objects.all()
    serializer_class = RoadTypeSerializer


class WeatherView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer


class CostCenterView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = CostCenter.objects.all()
    serializer_class = CostCenterSerializer


class OtherVehicleInvolvedView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = OtherVehicleInvolved.objects.all()
    serializer_class = OtherVehicleInvolvedSerializer


class RelationshipView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer


class DriverView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer


class AccidentBasicView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = AccidentBasic.objects.all()
    serializer_class = AccidentBasicSerializer


class ClaimInspectionReportView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = ClaimInspectionReport.objects.all()
    serializer_class = ClaimInspectionReportSerializer


class ClaimRepairEstimateView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = ClaimRepairEstimate.objects.all()
    serializer_class = ClaimRepairEstimateSerializer


class DriverLicenseRecievedView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = DriverLicenseRecieved.objects.all()
    serializer_class = DriverLicenseRecievedSerializer


class ClaimPoliceAbstractView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = ClaimPoliceAbstract.objects.all()
    serializer_class = ClaimPoliceAbstractSerializer


class ClaimFormRecievedView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = ClaimFormRecieved.objects.all()
    serializer_class = ClaimFormRecievedSerializer


class AccidentDescriptionView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = AccidentDescription.objects.all()
    serializer_class = AccidentDescriptionSerializer


class PartyToBlameView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = PartyToBlame.objects.all()
    serializer_class = PartyToBlameSerializer


class BrokersNameView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = BrokersName.objects.all()
    serializer_class = BrokersNameSerializer


class LiabilityFlagView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = LiabilityFlag.objects.all()
    serializer_class = LiabilityFlagSerializer


class AccidentStatusView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = AccidentStatus.objects.all()
    serializer_class = AccidentStatusSerializer


class TypeOfLossClaimView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = TypeOfLossClaim.objects.all()
    serializer_class = TypeOfLossClaimSerializer


class AccidentTypeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = AccidentType.objects.all()
    serializer_class = AccidentTypeSerializer


class VehicleAccidentView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleAccident.objects.all()
    serializer_class = VehicleAccidentSerializer


class RepairServiceHistoryView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairServiceHistory.objects.all()
    serializer_class = RepairServiceHistorySerializer


class RepairRechargeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairRecharge.objects.all()
    serializer_class = RepairRechargeSerializer


class RepairInvoicePaidView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairInvoicePaid.objects.all()
    serializer_class = RepairInvoicePaidSerializer


class RepairRecievedByView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairRecievedBy.objects.all()
    serializer_class = RepairRecievedBySerializer


class RepairInvoiceDetailsView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairInvoiceDetails.objects.all()
    serializer_class = RepairInvoiceDetailsSerializer


class RepairEstimationCostView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairEstimationCost.objects.all()
    serializer_class = RepairEstimationCostSerializer


class RepairPaperworkStatusView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairPaperworkStatus.objects.all()
    serializer_class = RepairPaperworkStatusSerializer


class RepairJobStatusView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairJobStatus.objects.all()
    serializer_class = RepairJobStatusSerializer


class RepairReasonView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairReason.objects.all()
    serializer_class = RepairReasonSerializer


class RepairWorkshopView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairWorkshop.objects.all()
    serializer_class = RepairWorkshopSerializer


class RepairDescriptionView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairDescription.objects.all()
    serializer_class = RepairDescriptionSerializer


class RepairSupplyView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = RepairSupply.objects.all()
    serializer_class = RepairSupplySerializer


class VehicleRepairView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleRepair.objects.all()
    serializer_class = VehicleRepairSerializer


class VehicleNotesView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleNotes.objects.all()
    serializer_class = VehicleNotesSerializer


class VehicleAssetsView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleAssets.objects.all()
    serializer_class = VehicleAssetsSerializer


class VehicleAllocationView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleAllocation.objects.all()
    serializer_class = VehicleAllocationSerializer


class VehicleInsuranceCompanyView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleInsuranceCompany.objects.all()
    serializer_class = VehicleInsuranceCompanySerializer


class VehicleBasicView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleBasic.objects.all()
    serializer_class = VehicleBasicSerializer


class VehicleDiaryView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleDiary.objects.all()
    serializer_class = VehicleDiarySerializer


class VehicleSummaryView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleSummary.objects.all()
    serializer_class = VehicleSummarySerializer


class VehicleInsuranceCompanyView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleInsuranceCompany.objects.all()
    serializer_class = VehicleInsuranceCompanySerializer


class VehicleTyreView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleTyre.objects.all()
    serializer_class = VehicleTyreSerializer


class VehicleTypeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleStatusView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleStatus.objects.all()
    serializer_class = VehicleStatusSerializer


class VehicleReturnedWorkshopView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleReturnedWorkshop.objects.all()
    serializer_class = VehicleReturnedWorkshopSerializer


class VehicleModelCodeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleModelCode.objects.all()
    serializer_class = VehicleModelCodeSerializer


class VehicleMakeCodeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleMakeCode.objects.all()
    serializer_class = VehicleMakeCodeSerializer


class VehicleLocationCodeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleLocationCode.objects.all()
    serializer_class = VehicleLocationCodeSerializer


class VehicleInPullView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleInPull.objects.all()
    serializer_class = VehicleInPullSerializer


class VehicleGearBoxView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleGearBox.objects.all()
    serializer_class = VehicleGearBoxSerializer


class VehicleFuelTypeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleFuelType.objects.all()
    serializer_class = VehicleFuelTypeSerializer


class VehicleDeductabilityView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleDeductability.objects.all()
    serializer_class = VehicleDeductabilitySerializer


class VehicleCurrencyCodesView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleCurrencyCodes.objects.all()
    serializer_class = VehicleCurrencyCodesSerializer


class VehicleCountyView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleCounty.objects.all()
    serializer_class = VehicleCountySerializer


class VehicleCountryView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleCountry.objects.all()
    serializer_class = VehicleCountrySerializer


class VehicleCostCenterView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleCostCenter.objects.all()
    serializer_class = VehicleCostCenterSerializer


class VehicleConventionTypeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleConventionType.objects.all()
    serializer_class = VehicleConventionTypeSerializer


class VehicleCompanyCodeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleCompanyCode.objects.all()
    serializer_class = VehicleCompanyCodeSerializer


class VehicleBodyTypeView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleBodyType.objects.all()
    serializer_class = VehicleBodyTypeSerializer


class VehicleClientView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = VehicleClient.objects.all()
    serializer_class = VehicleClientSerializer


class VehicleView(viewsets.ModelViewSet):
    permission_class = [IsAuthenticated]
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
