from django.urls import include, path
from rest_framework.routers import DefaultRouter
from.views import PropertyViewSet, ApplianceViewSet, RepairsViewSet, InvestmentsViewSet, AppApiInfoViewSet, CustomUserViewSet, UserViewSet, DecodeApplianceView,add_appliance_view

router = DefaultRouter()
router.register('properties', PropertyViewSet)
router.register('appliances', ApplianceViewSet)
router.register('repairs', RepairsViewSet)
router.register('investments', InvestmentsViewSet)
router.register('appliance-details-from-api', AppApiInfoViewSet)
# router.register('users', CustomUserViewSet)
router.register('custom-users', CustomUserViewSet)
router.register('users', UserViewSet)

#the paths of the endpoints
#this file maps URLs to view. 
#when a user accesses a specific URL, django check the urls.py to determine which view to call

urlpatterns = [
    path('', include(router.urls)),
    path('decode-appliance/', DecodeApplianceView.as_view(), name='decode_appliance'),
    path('add-appliance/', add_appliance_view, name='add_appliance'),  # Add this line
]

