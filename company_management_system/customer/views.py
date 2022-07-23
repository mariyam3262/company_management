from dataclasses import field
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Customer
from .forms import CustomerForm

# Create your views here.

class CustomerListView(ListView):
    model = Customer
    
class CustomerCreateView(CreateView):
    model = Customer
    # template_name = 'customer_form.html'
    form_class = CustomerForm
    # fields = "__all__"

class CustomerUpdateView(UpdateView):
    model = Customer
    # fields = "__all__"
    form_class = CustomerForm

class CustomerDetailView(DetailView):
    model = Customer
    fields = "__all__"

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer-list')