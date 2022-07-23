from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Project
from django.urls import reverse_lazy
from .forms import ProjectForm
# Create your views here.

class ProjectListView(ListView):
    model =Project

class ProjectCreateView(CreateView):
    model =Project
    # fields = "__all__"
    form_class = ProjectForm
    template_name = 'project/project_form.html'
    

    

class ProjectUpdateView(UpdateView):
    model = Project
    # fields = "__all__"
    form_class = ProjectForm

class ProjectDetailView(DetailView):
    model = Project


class ProjectDeleteView(DeleteView):
    model = Project
    success_url = reverse_lazy('project-list')