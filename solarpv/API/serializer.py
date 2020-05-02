from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','userID','firstName','middleName','lastName','jobTitle','email','officePhone','cellPhone','prefix')
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'modelNumber', 'productName', 'cellTechnology', 'cellManufacturer', 'numberOfCells',
         'numberOfCellsInSeries', 'numberOfSeriesStrings', 'numberOfDiodes', 'productLength',
          'productWidth', 'productWeight', 'superstateType', 'superstateManufacturer', 'substrateType',
           'substrateManufacturer', 'frameType', 'frameAdhesive', 'encapsulateType', 'encapsulantManufacturer',
            'junctionBoxType', 'junctionBoxManufacturer')
class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('id', 'certificateNumber', 'certID', 'userID', 'reportNumber', 'issueDate', 'standardID', 'locationID', 'modelNumber')
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id','serviceID','serviceName','description','isFIRequired','FIfrequency','standardID')
