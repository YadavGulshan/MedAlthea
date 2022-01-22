from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from pharmacy.models import medicineDetails, shopAndOwnerDetails
from pharmacy.serializers import medicineDetailsSerializer, ShopAndOwnerDetailsSerializer

# Create your views here.

