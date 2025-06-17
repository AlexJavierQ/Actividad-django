from django.contrib import admin
from app.models import *
# Register your models here.

class InscripcionInLine(admin.TabularInline):
    model = Inscripcion
    extra = 1
    verbose_name = "Inscripiòn"
    verbose_name_plural = "Inscripciones"
class CursoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'departamento', 'instructor')
    list_filter = ('departamento', 'instructor')
    search_fields = ('titulo',)
    inlines = (InscripcionInLine,)
    
class EntregaInLine(admin.TabularInline):
    model = Entrega
    extra = 1
    verbose_name = "Entrega"
    verbose_name_plural = "Entregas"
class TareaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'curso', 'fecha_entrega')
    list_filter = ('curso',) 
    search_fields = ('titulo',)
    inlines = (EntregaInLine,)

admin.site.register(Departamento)
admin.site.register(Instructor)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Estudiante)
admin.site.register(Inscripcion)
admin.site.register(Tarea, TareaAdmin)
admin.site.register(Entrega)
