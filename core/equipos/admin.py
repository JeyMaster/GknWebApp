from core.equipos.models import Equipo_Para_Entregar
from django.contrib import admin
from core.equipos import models

class Equipo_Admin(admin.ModelAdmin):
    list_filter=('estado','id_stock',)
    list_display=('id_stock','service_tag',
        'estado','ram',)
    search_fields=('service_tag',)


    def ram(self,obj):
        return obj.id_stock.ram

class Basura_Electronica_Admin(admin.ModelAdmin):
    list_display=('descripcion','cantidad','modelo','marca','no_serie','planta','responsable','fecha_registro'
    ,'recolectado','fecha_recoleccion')
    search_fields=('modelo','no_serie')
    list_filter=('responsable','recolectado',)

class Stock_Admin(admin.ModelAdmin):
    list_display=('marca','modelo','ram','categoria','cantidad')
    list_filter=('categoria',)

class Equipo_Para_Entregar_Detalles_Admin(admin.ModelAdmin):
    list_display=('id_equipo_para_entregar','service_tag','preparado_por','fecha_preparacion','usuario_final',)
    search_fields=('id_equipo_para_entregar__nombre_equipo','id_equipo_para_entregar__usuario_final',)
    list_filter=('preparado_por','fecha_preparacion',)

    def usuario_final(self,obj):
        #result=models.Equipo_Para_Entregar.objects.filter(pk=1)
        return obj.id_equipo_para_entregar.usuario_final

    def service_tag(self,obj):
        return obj.id_equipo_para_entregar.id_equipo.service_tag
    
class Equipo_Para_Entregar_Admin(admin.ModelAdmin):
    list_display=('nombre_equipo','id_equipo','usuario_final',)

admin.site.site_header='Gkn Stock Admin'
admin.site.site_title='Gkn Stock Admin'
admin.site.register(models.Equipo,Equipo_Admin)
admin.site.register(models.Stock,Stock_Admin)
admin.site.register(models.Basura_Electronica,Basura_Electronica_Admin)
admin.site.register(models.Equipo_Para_Entregar,Equipo_Para_Entregar_Admin)
admin.site.register(models.Equipo_Para_Entregar_Detalles,Equipo_Para_Entregar_Detalles_Admin)
admin.site.register(models.Equipo_Pool_Entrega)


# Register your models here.
