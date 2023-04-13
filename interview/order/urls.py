
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, OrderTagCreateView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('<int:id>/tags/', OrderTagCreateView.as_view(), name='order-tag-list'),
]