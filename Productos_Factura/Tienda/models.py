from django.db import models

class Productos(models.Model):
    id_productos = models.CharField(max_length=20, blank=False, primary_key=True)
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=200, blank=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    fecha_caducidad = models.DateField()

    def __str__(self):
        return self.nombre

class Categorias(models.Model):
    id_categorias = models.CharField(max_length=20, blank=False, primary_key=True)
    nombre = models.CharField(max_length=100, blank=False)
    descripcion = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.nombre

class Clientes(models.Model):
    id_clientes = models.CharField(max_length=20, blank=False, primary_key=True)
    nombre = models.CharField(max_length=100, blank=False)
    apellido = models.CharField(max_length=100, blank=False)
    direccion = models.CharField(max_length=200, blank=False)
    telefono = models.CharField(max_length=20, blank=False)
    email = models.EmailField(max_length=100, blank=False)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Factura(models.Model):
    id_factura = models.CharField(max_length=20, blank=False, primary_key=True)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.RESTRICT)
    id_producto = models.ForeignKey(Productos, on_delete=models.RESTRICT)
    fecha_factura = models.DateField()
    total_factura = models.DecimalField(max_digits=10, decimal_places=2, blank=False)

    def __str__(self):
        return self.id_factura

