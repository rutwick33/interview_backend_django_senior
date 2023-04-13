from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer, OrderTagOnlySerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

class OrderTagCreateView(generics.ListAPIView):
    queryset = Order.objects.all().only('id','tags')
    serializer_class = OrderTagOnlySerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        order = self.get_queryset(id=kwargs['id'])
        serializer = self.serializer_class(order)

        return Response(serializer.data, status=200)

    def get_queryset(self, **kwargs):
        return self.queryset.get(**kwargs)