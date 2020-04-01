from django.urls import path

from . import  views

app_name = 'inversiones'

urlpatterns = [
    path('', views.inversion_list, name='list'),
    path('<int:inversion_id>/', views.inversion_detail, name='detail'),
    path('nuevo/', views.inversion_create, name='new'),
    path('editar/<int:inversion_id>/', views.inversion_update, name='update'),
    path('delete/<int:inversion_id>/', views.inversion_delete, name='delete'),
]

