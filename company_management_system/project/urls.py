from django.urls import path
from .views import ProjectCreateView, ProjectListView,ProjectUpdateView,ProjectDetailView, ProjectDeleteView 

urlpatterns = [
    path('list/', ProjectListView.as_view(), name='project-list'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('<int:pk>/detail/', ProjectDetailView.as_view(), name='project-detail'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),




    ]