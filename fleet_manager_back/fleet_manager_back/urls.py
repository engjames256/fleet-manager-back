"""fleet_manager_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "is_staff"]


# ViewSets define the view behavior.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r"^admin/", admin.site.urls),
    url(r"^", include(("vehicle.urls", "vehicle"), namespace="vehicle")),
    url(r"^", include(("vehicle_tyre.urls", "vehicletyre"), namespace="vehicletyre")),
    url(r"^", include(("vehicle_status.urls", "vehiclestatus"), namespace="vehiclestatus")),
    url(r"^", include(("vehicle_make_code.urls", "vehiclemakecode"), namespace="vehiclemakecode")),
    url(r"^", include(("vehicle_fuel_type.urls", "vehiclefueltype"), namespace="vehiclefueltype")),
    url(r"^", include(("vehicle_company_code.urls", "vehiclecompanycode"), namespace="vehiclecompanycode")),
    url(r"^", include(("vehicle_cost_center.urls", "vehiclecostcenter"), namespace="vehiclecostcenter")),
    url(r"^", include(("vehicle_convention_type.urls", "vehicleconventiontype"), namespace="vehicleconventiontype")),
    url(r"^", include(("vehicle_client.urls", "vehicleclient"), namespace="vehicleclient")),
    url(r"^", include(("vehicle_country.urls", "vehiclecountry"), namespace="vehiclecountry")),
    url(r"^", include(("vehicle_model_code.urls", "vehiclemodelcode"), namespace="vehiclemodelcode")),
    url(r"^", include(("vehicle_returned_workshop.urls", "vehiclereturnedworkshop"), namespace="vehiclereturnedworkshop")),
    url(r"^", include(("vehicle_location_code.urls", "vehiclelocationcode"), namespace="vehiclelocationcode")),
    url(r"^", include(("vehicle_currency_codes.urls", "vehiclecurrencycodes"), namespace="vehiclecurrencycodes")),
    url(r"^", include(("vehicle_in_pull.urls", "vehicleinpull"), namespace="vehicleinpull")),
    url(r"^", include(("vehicle_deductability.urls", "deductability"), namespace="deductability")),
    url(r"^", include(("vehicle_gear_box.urls", "gearbox"), namespace="gearbox")),
    url(
        r"^",
        include(
            ("vehicle_county.urls", "vehiclecounty"), namespace="vehiclecounty"
        ),
    ),
    url(r"^", include(router.urls)),
    url(r"^api-auth/", include("rest_framework.urls", namespace="home")),
]