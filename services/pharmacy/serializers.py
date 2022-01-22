from rest_framework import serializers
from pharmacy.models import medicineDetails, shopAndOwnerDetails


class medicineDetailsSerializer(serializers.Serializer):
    class Meta:
        name = medicineDetails
        fields = [
            'medicine_name',
            'medicine_price',
            'medicine_rating',
            'medicine_total_rating',
            'medicine_noOfTablets'
            ]


class ShopAndOwnerDetailsSerializer(serializers.Serializer):
    class Meta:
        fields = [
            'owner_first_name',
            'owner_last_name',
            'owner_email',
            'shop_name',
            'shop_address',
            'shope_District',
            'shop_state',
            'shop_contact',
            'medicines'
            ]
