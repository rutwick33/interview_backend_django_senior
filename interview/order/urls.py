
from django.urls import path
from interview.order.views import OrderListCreateView, OrderTagListCreateView,\
    OrderFilterDateView


urlpatterns = [
    path('tags/', OrderTagListCreateView.as_view(), name='order-detail'),
    path('', OrderListCreateView.as_view(), name='order-list'),
    path('date/<str:start_date>&<str:embargo_date>',OrderFilterDateView.as_view(), name = 'date-range-order')
]