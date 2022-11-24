from rest_framework import serializers
from .models import *

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id','url','name','category')
        
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id','url','name')
    
class CoderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coder
        fields = ('id','url','name','language')