from django.shortcuts import render
from .models import userinfo
from .serializers import userSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def getdata(request):
    if request.method=='GET':
        stdata=userinfo.objects.all()
        serial=userSerializers(stdata,many=True)
        return Response(serial.data)



