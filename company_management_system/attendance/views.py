from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from .models import Attendance, DailyReport
from .forms import AttendanceForm


# Create your views here.

class AttendanceListView(ListView):
    model = Attendance
    template_name = 'attendance_list'

class AttendanceCreateView(CreateView):
    model = Attendance
    form_class = AttendanceForm

class AttendanceUpdateView(UpdateView):
    model = Attendance
    form_class = AttendanceForm

class AttendanceDetailView(DetailView):
    model = Attendance

class AttendanceDeleteView(DeleteView):
    model = Attendance 
    success_url = reverse_lazy('attendance-list')

#---------------------------------DAILY-REPORT-----------------------------------------




class DailyReportListView(ListView):
    model = DailyReport
    template_name = 'dailyReport_list'

class DailyReportCreateView(CreateView):
    model = DailyReport
    fields = ('employee','designation','working_project','performedTask_today','performedTask_next_day')

class DailyReportUpdateView(UpdateView):
    model = DailyReport
    fields = "__all__"

class DailyReportDetailView(DetailView):
    model = DailyReport

class DailyReportDeleteView(DeleteView):
    model = DailyReport 
    success_url = reverse_lazy('dailyReport-list')