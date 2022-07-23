from django.urls import path
from .views import (CustomerListView, CustomerCreateView, CustomerUpdateView,
CustomerDetailView, CustomerDeleteView)

urlpatterns=[
    path('list/', CustomerListView.as_view(), name = 'customer-list'),
    path('create/', CustomerCreateView.as_view(), name = 'customer-create'),
    path('<int:pk>/update/', CustomerUpdateView.as_view(), name = 'customer-update'),
    path('<int:pk>/detail/', CustomerDetailView.as_view(), name='customer-detail'),
    path('<int:pk>/delete/', CustomerDeleteView.as_view(), name='customer-delete')



]