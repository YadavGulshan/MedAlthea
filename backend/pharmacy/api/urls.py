# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from django.conf import settings
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)



from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from pharmacy.api.views.mapper.distance import CalculateDistance


from pharmacy.api.views.medical.list import MedicalViewList
from pharmacy.api.views.medical.search import MedicalSearch
from pharmacy.api.views.medical.views import MedicalView
from pharmacy.api.views.medicine.list import MedicineViewList
from pharmacy.api.views.medicine.search import MedicineSearch
from pharmacy.api.views.userActions import UserAction
from pharmacy.api.views.userActions.register import Register, UserNameAvailable
from pharmacy.api.views.userActions.token.view import MyTokenObtainPairView

# from . import Medical

urlpatterns = [
    # For getting the api view: i.e medical list and all
    path('', MedicalViewList.as_view(), name='get'),
    path('<int:pk>/', MedicalView.as_view(), name='get'),
    path('search/', MedicalSearch.as_view(), name='search'),

    # For medicine
    path('medicine/', MedicineViewList.as_view(), name='get'),
    path('search/medicine/', MedicineSearch.as_view(), name='search'),

    # User
    path('user/', UserAction.as_view(), name='user'),

    # Auth

    # Auth: login
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # Auth: register user
    path('register/', Register.as_view(), name='register'),
    path('register/search/<str:pk>/', UserNameAvailable.as_view(), name='register'),

    # Utilities goes here.
    path('distance/', CalculateDistance.as_view(), name="calculate_distance")

]

urlpatterns = format_suffix_patterns(urlpatterns)


# For media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
