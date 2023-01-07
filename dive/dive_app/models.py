from django.db import models

# Create your models here.

class Dive(models.Model):
     nama      = models.CharField(max_length=75)
     grs_lintang = models.FloatField(null=True)
     grs_bujur = models.FloatField(null=True)
     gambar   = models.ImageField(null=True, blank=True, upload_to="images/")

     def __str__(self):
         return self.nama

class Peralatan(models.Model):
     nama_Alat  = models.CharField(max_length=75)
     harga     = models.CharField(max_length=50)
     gambar    = models.ImageField(null=True, blank=True, upload_to="image/")
     deskripsi = models.CharField(max_length=650)
     
     def __str__(self):
         return self.nama_Alat