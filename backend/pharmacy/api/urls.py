# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

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
    path('', views.MedicalViewList.as_view(), name='get'),
    path('<int:pk>/', views.MedicalView.as_view(), name='get'),
    path('search/', views.MedicalSearch.as_view(), name='search'),
    
    # For medicine
    path('medicine/', views.MedicineViewList.as_view(), name='get'),
    path('search/medicine/', views.MedicineSearch.as_view(), name='search'),

    # User
    path('user/', views.UserData.as_view(), name='user'),

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
