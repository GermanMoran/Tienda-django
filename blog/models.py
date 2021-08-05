from django.db import models
from django.contrib.auth.models import User
# Create your models here.

        

# Creamos una clase parala categoria
class Categoria(models.Model):
    nombre=models.CharField(max_length=50)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='categoria'
        verbose_name_plural='categorias'
    
    def __str__(self):
        return self.nombre
        

# Creamos una clase para el post
class Post(models.Model):
    titulo=models.CharField(max_length=50)
    contenido=models.CharField(max_length=50)
    #Con esto indicamos que la imagen del blog es opcional
    imagen=models.ImageField(upload_to='blog', null = True, blank=True)
    # Usamos la clave foranea para establecer la relacion entre el usuario y el post, aqui estamos diciendo que
    # cuando se elimine la clase user la eliminacion debe ser en cascada 
    autor = models.ForeignKey(User, on_delete=models.CASCADE)

    # Indicamos la relacion entre estas dos tablas
    categorias = models.ManyToManyField(Categoria)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name='post'
        verbose_name_plural='posts'
    
    def __str__(self):
        return self.titulo