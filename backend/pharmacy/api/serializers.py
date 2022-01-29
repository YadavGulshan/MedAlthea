from rest_framework import serializers
from pharmacy.models import Medical


class MedicalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medical
        fields = '__all__'