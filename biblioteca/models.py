from django.db import models

# Create your models here.

class Editor(models.Model):
	nombre = models.CharField(max_length=30) 
	domicilio = models.CharField(max_length=50) 
	ciudad = models.CharField(max_length=60) 
	estado = models.CharField(max_length=30) 
	pais = models.CharField(max_length=50) 
	website = models.URLField(blank=True) # el blank=True indica que este campo de la tabla puede ser opcional

	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Editores"

	def __str__(self): # __unicode__ en Python 2 
		return self.nombre

class Autor(models.Model):
	nombre = models.CharField(max_length=30) 
	apellidos = models.CharField(max_length=40) 
	email = models.EmailField(blank=True, verbose_name='e-mail')

	class Meta:
		ordering = ["nombre"]
		verbose_name_plural = "Autores"

	def __str__(self): # __unicode__ en Python 2 
		return '%s %s' % (self.nombre, self.apellidos)

class Libro(models.Model):
	titulo = models.CharField(max_length=100)
	autores = models.ManyToManyField(Autor)
	editor = models.ForeignKey(Editor) 
	fecha_publicacion = models.DateField()
	portada = models.ImageField(upload_to='portadas')

	class Meta:
		ordering = ["titulo"]
		verbose_name_plural = "Libros"

	def __str__(self): # __unicode__ en Python 2 
		return self.titulo