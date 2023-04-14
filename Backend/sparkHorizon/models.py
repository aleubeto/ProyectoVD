from django.db import models

# Create your models here.
class TeamMember(models.Model):
    id = models.AutoField(primary_key=True)
    matricula = models.CharField(max_length=9)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=150)
    correo = models.EmailField()
    imagen = models.FileField(upload_to='sparkHorizon/imagen/')
    def __str__(self):
        return self.nombre + ' ' + self.apellido

class Gender(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    correo = models.EmailField()
    password = models.CharField(max_length=500)
    def __str__(self):
        return self.correo

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    sinopsis = models.TextField()
    portada = models.FileField(upload_to='sparkHorizon/portadas/')
    fecha_publicacion = models.DateField('fecha de publicación')
    num_pag = models.IntegerField('número de páginas', default=0)
    genero = models.ForeignKey(Gender, on_delete=models.CASCADE)
    autores = models.ManyToManyField(TeamMember)
    calificacion = models.ManyToManyField(Usuario, through='Calificacion')
    def __str__(self):
        return self.titulo

class Calificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='calificaciones')
    calificacion = models.IntegerField()
    comentario = models.TextField()
    def __str__(self):
        return str(self.calificacion, '|', self.calificacion)