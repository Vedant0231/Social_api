from .serializers import Userserializer, Postserializer, Likeserializer
from .models import Usermodel, Postmodel, Likemodel
from rest_framework import viewsets
from rest_framework.response import Response
# Create your views here.


"""api for user"""
class Userlist(viewsets.ModelViewSet):

    queryset = Usermodel.objects.all()
    serializer_class = Userserializer


"""api for post"""
class Postlist(viewsets.ModelViewSet):
    
    queryset = Postmodel.objects.all()
    serializer_class = Postserializer


"""api for like"""
class Likelist(viewsets.ModelViewSet):
    
    queryset = Likemodel.objects.all()
    serializer_class = Likeserializer   
 

