from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

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


class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

@api_view()
@permission_classes([IsAuthenticated])
def securedview(request):
    return Response({"message": "needs authentication"})