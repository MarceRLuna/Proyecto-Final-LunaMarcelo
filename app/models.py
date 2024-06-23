from django.db import models

# Create your models here.

class Inmueble(models.Model):
    
    #definimos los atributos que tendrá la clase

    categoria = models.CharField(max_length=30)
    ubicacion = models.CharField(max_length=50)
    domitorios = models.IntegerField()
    metros_cuadrados = models.IntegerField()

    def __str__(self):
        return f'''- {self.categoria} 
                   - {self.ubicacion}
                   - {self.domitorios}
                   - {self.metros_cuadrados}'''
    

class Propietario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    mail = models.EmailField()

    def __str__(self):
        return f'''- {self.nombre} 
                   - {self.apellido}
                   - {self.telefono}
                   - {self.mail}'''

class Inquilino(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    telefono = models.IntegerField()
    mail = models.EmailField()
    valor_alquiler = models.IntegerField()

    def __str__(self):
        return f'''- {self.nombre} 
                   - {self.apellido}
                   - {self.telefono}
                   - {self.mail}
                   - {self.valor_alquiler}'''


