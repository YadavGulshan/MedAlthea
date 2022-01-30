from django.conf import settings
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)
from .views import MyTokenObtainPairView
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    # For getting the api view: i.e medical list and all
    path('', views.DataList.as_view(), name='get'),
    path('<int:pk>/', views.Data.as_view(), name='get'),

    # User
    path('user/', views.User.as_view(), name='user'),

    ## Auth

    # Auth: login
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Auth: register user
    path('register/', views.Register.as_view(), name='register'),
]

urlpatterns = format_suffix_patterns(urlpatterns)


# For media files   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
