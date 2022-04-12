# Copyright (C) 2022 by YadavGulshan@Github, < https://github.com/YadavGulshan >.
#
# This file is part of < https://github.com/Yadavgulshan/PharmaService > project,
# and is released under the "BSD 3-Clause License Agreement".
# Please see < https://github.com/YadavGulshan/pharmaService/blob/master/LICENCE >
#
# All rights reserved.

from django.conf import settings
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView

from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from pharmacy.api.views import userActions, medicine, medical, mapper

urlpatterns = [
    # For getting the api view: i.e medical list and all
    path("", medical.MedicalViewList.as_view(), name="get"),
    path("<int:pk>/", medical.MedicalView.as_view(), name="get"),
    path("search/", medical.MedicalSearch.as_view(), name="search"),
    path("mymedical/", medical.MyMedical.as_view(), name="mymedical"),
    # For getting the list of medicine in specific medical
    path(
        "mymedical/<int:pk>/",
        medical.MedicineViewByID.as_view(),
        name="mymedicalMedicne",
    ),
    # For medicine
    path("medicine/", medicine.MedicineViewList.as_view(), name="get"),
    # Functionality to edit or delete a medicine
    path("medicine/<int:pk>/", medicine.MedicineView.as_view(), name="get"),
    path("medicine/search/", medicine.MedicineSearch.as_view(), name="search"),
    # User
    path("user/", userActions.UserView.as_view(), name="user"),
    # Auth
    # Auth: login
    path(
        "token/",
        userActions.token.MyTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    # Auth: register user
    path("register/", userActions.Register.as_view(), name="register"),
    path(
        "register/search/",
        userActions.register.UserNameAvailable.as_view(),
        name="serch",
    ),
    path(
        "emailverification/<uidb64>/<token>/",
        userActions.Activate.as_view(),
        name="emailverification",
    ),
    # path(
    #     "passwordreset/<str:mail>/",
    #     userActions.PasswordReset.as_view(),
    #     name="passwordreset",
    # ),
    # path(
    #     "passwordreset/<uidb64>/<token>/",
    #     userActions.PasswordResetConfirm.as_view(),
    #     name="passwordresetconfirm",
    # ),
    path(
        "delete/",
        userActions.UserView.as_view(),
        name="deleteAccount",
    ),
    # Utilities goes here.
    path("distance/", mapper.CalculateDistance.as_view(), name="calculate_distance"),
    path(
        "nearbymedical/", mapper.DisplayNearbyMedical.as_view(), name="nearby_medical"
    ),
    path(
        "nearbymedicine/",
        mapper.MedicineSearch.as_view(),
        name="nearby_medicine",
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)


# For media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += staticfiles_urlpatterns()
