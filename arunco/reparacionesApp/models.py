from django.db import models


# Create your models here.

class Reparaciones(models.Model):
    fecha_entrada = models.DateField(auto_now_add=True)
    fecha_salida = models.DateField(null=True, blank=True)
    cliente = models.ForeignKey("Clientes", verbose_name=("Cliente"), on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    trabajo = models.ManyToManyField("Trabajos", through='ManoDeObra')
    repuestos = models.ManyToManyField('Repuestos', through="Encargos", blank=True)
    total = models.IntegerField(verbose_name="costo",null=True, blank=True) # Costo de fabricacion
    venta = models.IntegerField(null=True, blank=True) # Precio de venta
    confirmado = models.BooleanField(default=False)
    plazo_de_entrega = models.DateField(null=True, blank=True)
    
    class Meta:
        verbose_name_plural = "reparaciones"

class Clientes(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=13, unique=True, null=True, blank=True)
    mail = models.EmailField(max_length=100, unique=True, null=True, blank=True)
    empresa = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "clientes"

class Trabajos(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    
    class Meta:
        verbose_name_plural = "trabajos"

class ManoDeObra(models.Model):
    reparacion = models.ForeignKey(Reparaciones, on_delete=models.CASCADE)
    trabajo = models.ForeignKey(Trabajos, verbose_name='Trabajo realizado' ,on_delete=models.CASCADE)
    horas = models.IntegerField(verbose_name="Horas estimadas")
    orden = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "mano de obra"
        ordering = ["orden"]

class Repuestos(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    proveedor = models.CharField(max_length=50)
    
    class Meta:
        verbose_name_plural = "repuestos"

class Encargos(models.Model):
    trabajo = models.ForeignKey(Reparaciones,on_delete=models.CASCADE)
    repuesto = models.ForeignKey(Repuestos, verbose_name="A comprar" ,on_delete=models.CASCADE)
    encargado = models.BooleanField(default=False)
    costo = models.IntegerField()
    
    class Meta:
        verbose_name_plural = "encargos"
    