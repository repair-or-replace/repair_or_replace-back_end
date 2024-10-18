from django.urls import include, path
from rest_framework.routers import DefaultRouter
from.views import PropertyViewSet, ApplianceViewSet, RepairsViewSet, InvestmentsViewSet, ApplianceDetailsFromAPIViewSet, CustomUserViewSet, UserViewSet

router = DefaultRouter()
router.register('properties', PropertyViewSet)
router.register('appliances', ApplianceViewSet)
router.register('repairs', RepairsViewSet)
router.register('investments', InvestmentsViewSet)
router.register('appliance-details-from-api', ApplianceDetailsFromAPIViewSet)
# router.register('users', CustomUserViewSet)
router.register('custom-users', CustomUserViewSet)
router.register('users', UserViewSet)

#the paths of the endpoints
#this file maps URLs to view. 
#when a user accesses a specific URL, django check the urls.py to determine which view to call

urlpatterns = [
    path('', include(router.urls)),
]

