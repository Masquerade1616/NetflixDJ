from distutils.command.upload import upload
from tabnanny import verbose
from django.db import models

# netflix profil clası için gereken import
from django.contrib.auth.models import User
# hesabımıza baglı olan profilerri görmemiz gerekiyor
# Create your models here.
from django.utils.text import slugify

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isim = models.CharField(max_length=70)
    resim = models.FileField(upload_to='profiles/')
    #slugfield
    slug = models.SlugField(null=True, blank=True, unique=True, editable=False)
    def __str__(self):
        return self.isim

    def save(self, *args, **kwargs):
        self.slug = slugify(self.isim)
        super().save(*args, **kwargs)
    #admin panelinde isim görünsün diye girdigimiz self fonksiyonu


class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    resim = models.FileField(upload_to="profilResimleri/", verbose_name="Profil Resmi")
    tel = models.IntegerField()

    def __str__(self):
        return self.user.username   