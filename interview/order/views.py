from django.shortcuts import render
from django.db.models import Prefetch
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.request import Request

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer, OrderSpecificTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer

class TagOrderCreateView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSpecificTagSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:

        try:
            order = Order.objects.exclude(tags__isnull=True).prefetch_related(
                Prefetch('tags', queryset=OrderTag.objects.filter(id=kwargs['id']), to_attr='filtered_tags')
            )
            serializer = self.serializer_class(order,many=True)

            return Response(serializer.data, status=200)
        
        except Exception as e:
            print("********* Exception: ",e)