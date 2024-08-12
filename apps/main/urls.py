from django.urls import path
from apps.main import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('doctor/', views.doctor, name='doctor'),
    path('departments/', views.departments, name='departments'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('result/', views.result, name='result')
]
