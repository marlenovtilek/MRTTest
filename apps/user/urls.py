from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.UserLoginFormView.as_view(), name = 'login'),
    path('registration/',views.UserRegisterFormView.as_view(), name = 'registration'),
    path('logout/', views.logout_user, name = "logout"),
    path('profile/', views.UserProfileView.as_view(), name='profile')
]

