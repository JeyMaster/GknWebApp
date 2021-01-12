from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Stock(models.Model):
    CATEGORIAS=(
        ('LT','Laptop'),
        ('PC','Desktop'),
    )
    categoria=models.CharField(max_length=2,choices=CATEGORIAS)
    id_stock = models.AutoField(primary_key=True)
    cantidad = models.SmallIntegerField()
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=15)
    ram = models.SmallIntegerField(null=True,blank=True,default=0)
    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stock'
        db_table='Stock'

    def __str__(self):
       return "{} {}  Ram:{}".format(self.marca,self.modelo,self.ram)

class Equipo(models.Model):

    ESTADOS=(
        ('Pr','En preparacion'),
        ('Et','Entregado'),
        ('Ep','Equipo pool'),
        ('Pd','Para donación'),
        ('Bs','Basura electronica'),
        ('Pa','Pool asignado'),
        ('Ua','Usuario asignado'),      
    )
    id_equipo = models.AutoField(primary_key=True)
    id_stock=models.ForeignKey(Stock,on_delete=models.CASCADE)
    service_tag = models.CharField(max_length=12,blank=True)
    estado = models.CharField(max_length=2,choices=ESTADOS,default='Pr')
    fecha_termino_garantia=models.DateField(blank=True,null=True)

    class Meta:
        verbose_name='equipo'
        verbose_name_plural='equipos'
        db_table='Equipos'

    def __str__(self):
        return '{} {}'.format(self.id_stock,self.service_tag)

class Basura_Electronica(models.Model):
    PLANTAS=(
        ('VIG','Villagran'),
        ('CEL','Celaya'),
    )

    id_basura_electronica = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=100)
    cantidad = models.SmallIntegerField()
    modelo = models.CharField(max_length=15)
    marca = models.CharField(max_length=15)
    no_serie = models.CharField(max_length=100,null=True,blank=True,default='N/A')
    planta = models.CharField(max_length=3,choices=PLANTAS)
    responsable = models.ForeignKey(User,on_delete=models.CASCADE)
    fecha_registro = models.DateField()
    recolectado = models.BooleanField()
    fecha_recoleccion = models.DateField(null=True,blank=True)


    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name = 'Basura Electronica'
        verbose_name_plural = 'Basura Electronica'
        db_table='BasuraElectronica'

class Equipo_Para_Entregar(models.Model):
    id_equipo_para_entregar = models.AutoField(primary_key=True)
    nombre_equipo = models.CharField(max_length=12)
    id_equipo = models.ForeignKey(Equipo,on_delete=models.CASCADE)
    usuario_final = models.CharField(max_length=20,blank=True)

    def __str__(self):
        return '%s'%(self.id_equipo_para_entregar)

    class Meta:
        verbose_name = 'Equipo para entregar'
        verbose_name_plural = 'Equipos para entregar'
        db_table='EquipoParaEntregar'

class Equipo_Para_Entregar_Detalles(models.Model):
    id_equipo_para_entregar=models.ForeignKey(Equipo_Para_Entregar,on_delete=models.CASCADE)
    preparado_por = ForeignKey(User,on_delete=models.CASCADE)
    configurado_por = models.CharField(max_length=15,null=True,blank=True)
    fecha_preparacion = models.DateField()
    check_list = models.FileField(upload_to='checkList',null=True,blank=True,default='')
    certificado_de_calidad = models.FileField(upload_to='certificado',null=True,blank=True,default='')
    solicitud = models.FileField(upload_to='solicitudes',null=True,blank=True,default='')
    site = models.CharField(max_length=5,blank=True,null=True)
    departamento = models.CharField(blank=True,max_length=30,null=True)
    area = models.CharField(blank=True,max_length=30,null=True)
    ubicacion_exacta = models.CharField(blank=True,max_length=30,null=True)
    apps_especiales = models.CharField(max_length=200,blank=True,null=True)
    registro_en_inventario = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Detalle de entrega'
        verbose_name_plural = 'Detalles de entrega'
        db_table='DetallesEntrega'

    def __str__(self):
        return str(self.id_equipo_para_entregar)

class Equipo_Pool_Entrega(models.Model):
        
    nombre_equipo = models.ForeignKey(Equipo_Para_Entregar,on_delete=models.CASCADE)
    fecha_salida = models.DateTimeField()
    fecha_entrega = models.DateTimeField(null=True, blank=True)
    caso_especial = models.BooleanField(default=False)
    equipo_recibido = models.BooleanField(default=False)
        
    def __str__(self):
        return str(self.nombre_equipo)
    
    class Meta:
        verbose_name = 'Equipo pool entrega'
        verbose_name_plural = 'Equipos Pool entrega'
        db_table='EquiposPoolEntrega'