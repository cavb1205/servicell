from django.urls import path

from . import  views

app_name = 'inversiones'

urlpatterns = [
    path('', views.inversion_list, name='list'),
    path('<int:inversion_id>/', views.inversion_detail, name='detail'),
]

