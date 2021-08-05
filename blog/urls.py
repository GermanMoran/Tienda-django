from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    #<categoria> para indicarle que es un parametro de la BD , este es el 
    #criterio con el cual se realizara el filtrado, se debe indicar como 
    # entero porque asi se define en la BD
    path('categoria/<int:categoria_id>/', views.categoria, name='categoria'),
]

