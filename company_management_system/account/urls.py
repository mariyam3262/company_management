from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (ProfileListView, ProfileCreateView, ProfileUpdateView,ProfileDetailView, RegisterView)

urlpatterns = [
    path('list/', ProfileListView.as_view(), name='profile-list'),
    path('create/', ProfileCreateView.as_view(), name = 'profile-create'),
    path('<int:pk>/update/', ProfileUpdateView.as_view(), name = 'profile-update'),
    path('<int:pk>/detail/', ProfileDetailView.as_view(), name='profile-detail' ),

    #---------------------Authentication-------------------------------------

    path('register/', RegisterView.as_view(), name='registration'),
    path('login/', auth_views.LoginView.as_view(template_name='account/profile_form.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

   

]
