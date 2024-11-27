from django.db import models

class Restaurant(models.Model):
    # O Django já cria o ID automaticamente, não é necessário definir explicitamente
    name = models.CharField(max_length=100, blank=False)  # Nome do restaurante
    address = models.CharField(max_length=255)  # Endereço do restaurante
    number_cellphone = models.CharField(max_length=15)  # Número de celular (para contato)
    img = models.ImageField(upload_to='restaurants/', null=True, blank=True)  # Imagem do restaurante
    description = models.TextField()  # Descrição do restaurante
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Latitude
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)  # Longitude

    def __str__(self):
        return self.name
