from django.contrib.auth.models import User
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView, TemplateView
from .models import Profile

from django.contrib.auth.forms import UserCreationForm


from django.views import View

# Create your views here.

class ProfileListView(ListView):
    model = Profile


class ProfileCreateView(CreateView):
    model = Profile
    fields = "__all__"
    success_url = '/profile/'
    # template_name = 'account/registration.html'
    
    

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        user = User.objects.all().last()
        context['user'] = user
        return context

   

       

class ProfileUpdateView(UpdateView):
    model = Profile
    fields = "__all__"

class ProfileDetailView(DetailView):
    model = Profile
    fields = "__all__"

class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy('profile-list')


class RegisterView(View):
    def get(self, request):
        return render(request, 'account/profile_form.html', { 'form': UserCreationForm() })

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['username'])
            form.save()
            return redirect('profile-create')

        return render(request, 'account/profile_form.html', { 'form': form })




