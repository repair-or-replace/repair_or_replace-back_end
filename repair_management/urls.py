from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views.views import (
    UserDetailView,
    PropertyViewSet,
    ApplianceViewSet,
    RepairsViewSet,
    ApplianceApiViewSet,
    InvestmentsViewSet,
    UserViewSet,
    UserPropertyViewSet,
)
from .views.decode_appliance import DecodeApplianceView, add_appliance_view
from .views.signup import RegisterView
from .views.login import LoginView
from .views.reset_password import ResetPasswordView

router = DefaultRouter()
router.register('user-properties', UserPropertyViewSet, basename='user-properties')
router.register('properties', PropertyViewSet, basename='properties')
router.register('appliances', ApplianceViewSet)
router.register('repairs', RepairsViewSet)
router.register('investments', InvestmentsViewSet)
router.register('appliance-details-from-api', ApplianceApiViewSet)
# router.register('users', CustomUserViewSet)
# router.register('custom-users', CustomUserViewSet)
router.register('users', UserViewSet)


urlpatterns = [
    path('user-profile/', UserDetailView.as_view(), name='user-profile'),
    path('', include(router.urls)),
    path('decode-appliance/', DecodeApplianceView.as_view(), name='decode-appliance'),
    path('add-appliance/', add_appliance_view, name='add_appliance'), 


    # New paths for signup, login, and reset password
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset_password'),
]

