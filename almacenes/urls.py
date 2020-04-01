from django.urls import path

from . import views


app_name = 'almacenes'
urlpatterns = [
    path('<int:almacen_id>/', views.almacen_detail, name='detail'),
]
