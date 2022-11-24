from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.

class LanguageView(viewsets.ModelViewSet):
    queryset= Language.objects.all()
    serializer_class = LanguageSerializer
    
class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class CoderView(viewsets.ModelViewSet):
    queryset = Coder.objects.all()
    serializer_class = CoderSerializer