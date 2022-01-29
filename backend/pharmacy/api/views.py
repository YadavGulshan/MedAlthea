from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pharmacy.models import Medical
from .serializers import MedicalSerializer

@api_view(['GET'])
def getData(request):
    medical = Medical.objects.all()
    serializer = MedicalSerializer(medical, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def postData(request):
    serializer = MedicalSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['PUT'])
def updateData(request):
    medicalId = request.data['medicalId']
    medical = Medical.objects.get(medicalId)
    serializer = MedicalSerializer(instance=medical, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/token',
        'api/token/refresh',
    ]
    return Response(routes)