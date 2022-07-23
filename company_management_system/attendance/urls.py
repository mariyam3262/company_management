from django.urls import path
from .views import (AttendanceListView,AttendanceCreateView, AttendanceUpdateView, AttendanceDetailView,AttendanceDeleteView,DailyReportListView,DailyReportCreateView, DailyReportUpdateView, DailyReportDetailView,DailyReportDeleteView)

urlpatterns = [
    path('list/', AttendanceListView.as_view(), name = 'attendance-list'),
    path('create/', AttendanceCreateView.as_view(), name = 'attendance-create'),
    path('<int:pk>/update/', AttendanceUpdateView.as_view(), name = 'attendance-update'),
    path('<int:pk>/detail/', AttendanceDetailView.as_view(), name = 'attendance-detail'),
    path('<int:pk>/delete/', AttendanceDeleteView.as_view(), name = 'attendance-delete'),
#---------------------------------REPORT-----------------------------------------------------


    path('report-list/', DailyReportListView.as_view(), name = 'dailyReport-list'),
    path('report-create/', DailyReportCreateView.as_view(), name = 'dailyReport-create'),
    path('<int:pk>/report-update/', DailyReportUpdateView.as_view(), name = 'dailyReport-update'),
    path('<int:pk>/report-detail/', DailyReportDetailView.as_view(), name = 'dailyReport-detail'),
    path('<int:pk>/report-delete/', DailyReportDeleteView.as_view(), name = 'dailyReport-delete'),
]