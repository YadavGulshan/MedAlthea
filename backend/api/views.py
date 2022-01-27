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