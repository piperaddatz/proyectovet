from django.db import models

# Create your models here.



class Usuario(models.Model):
    username = models.CharField(max_length=264, unique=True)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=12)
    rol = models.CharField(max_length=12)
    profile_pic = models.ImageField()
    created_at = models.DateTimeField()

    def __str__(self): 
        return self.username


 class Mascota(models.Model):   
    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    profile_pic = models.ImageField(upload_to='cars')
    user_id = models.OneToManyField(Usuario)
    created_at = models.DateTimeField()

    def __str__(self): 
        return self.nombre


class Clinica(models.Model): 
    nombre = models.CharField(max_length=50) 
    direccion = models.TextField() 
    email = models.EmailField(max_length=50) 
    fono = models.CharField(max_length=15) 
    profile_pic = models.ImageField() 
    created_at = models.DateTimeField()

    def __str__(self): 
        return self.nombre 


class Trabaja(models.Model): 
    fecha = models.DateField() 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE) 
    created_at = models.DateField()  

    def __str__(self): 
        return "Médico trabajador" 


class Diagnostico(models.Model): 

    titulo = models.CharField(max_length=50) 
    descripcion = models.TextField()
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE) 
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE) 
    clinica = models.ForeignKey(Clinica, on_delete=models.CASCADE) 
    created_at = models.DateField()
 
    def __str__(self): 
        return self.nombre     





