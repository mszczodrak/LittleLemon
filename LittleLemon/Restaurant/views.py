from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import generics

from django.http import HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Booking, Menu, MenuItem
from .serializers import BookingSerializer, MenuSerializer, MenuItemSerializer

def index(request):
    return render(request, 'index.html', {})


# Create your views here. 
class MenuItemsView(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

