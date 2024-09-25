from django.urls import path

from alex import views

urlpatterns=[path('contact/', views.ContactCreateView.as_view(), name='contact'),]