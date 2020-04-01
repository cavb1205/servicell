from django.urls import path

from . import  views

app_name = 'gastos'

urlpatterns = [
    path('', views.gasto_list, name='list'),
    path('<int:gasto_id>/', views.gasto_detail, name='detail'),
    path('nuevo/', views.gasto_create, name='new'),
    path('editar/<int:gasto_id>/', views.gasto_update, name='update'),
    path('delete/<int:gasto_id>/', views.gasto_delete, name='delete'),
]

