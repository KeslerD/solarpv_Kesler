from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import filters
from .models import *
from .serializer import *

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
class CertificateView(viewsets.ReadOnlyModelViewSet):
    search_fields = ['certID','certificateNumber']
    filter_backends = (filters.SearchFilter,)
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer