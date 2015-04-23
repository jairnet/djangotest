from django.contrib import admin
from biblioteca.models import Editor, Autor, Libro

# Esta clase lo que hace es aplicar cambios visibles en la vista administrador de la tabla
# Autor, lo que esta haciendo es listar el nombre, apellidos y e-mail la linea 10 es agrega un buscador con los
# parametros de nombre y apellidos

class AutorAdmin(admin.ModelAdmin):
	list_display=('nombre','apellidos','email')
	search_fields=('nombre','apellidos')

# Esta clase lo que hace es agregar un filtro para ver los cambios que ha tenido la tabla libro
class LibroAdmin(admin.ModelAdmin):
	list_display=('titulo','editor','fecha_publicacion')
	list_filter=('fecha_publicacion',)

admin.site.register(Editor) 
admin.site.register(Autor, AutorAdmin) 
admin.site.register(Libro, LibroAdmin)
# Register your models here.
