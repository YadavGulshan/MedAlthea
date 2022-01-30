from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from .views import MyTokenObtainPairView
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('', views.DataList.as_view(), name='get'),
    path('<int:pk>/', views.Data.as_view()),

    # User
    path('user/', views.User.as_view()),

    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
