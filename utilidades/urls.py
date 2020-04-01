from django.urls import path

from . import  views

app_name = 'utilidades'

urlpatterns = [
    path('', views.utilidad_list, name='list'),
    path('<int:utilidad_id>/', views.utilidad_detail, name='detail'),
    path('nuevo/', views.utilidad_create, name='new'),
    path('editar/<int:utilidad_id>/', views.utilidad_update, name='update'),
    path('delete/<int:utilidad_id>/', views.utilidad_delete, name='delete'),
]

