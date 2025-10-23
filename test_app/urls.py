from django.urls import path, include
from . import views

app_name = 'test_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:test_pk>/', views.detail, name='detail'),
]
