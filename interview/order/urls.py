
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView, TagOrderCreateView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('tags/<int:id>',TagOrderCreateView.as_view(),name='tag-order-list'),
]