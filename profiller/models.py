from django.db import models
from django.contrib.auth.models import User
from PIL import Image


class Profil(models.Model):
    #!Bir kullanıcının bir profili olabilir bir profilde bir kullanıcıya ait olabilir.
    #!related_name = örn : user.profil ile user a bağlı bu class altındaki bütün ayarları çekebiliriz.
    #! null=True : doldurulması zorunlu olmayan alan

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    bio = models . CharField(max_length=300, blank=True, null=True)
    sehir = models . CharField(max_length=120, blank=True, null=True)
    foto = models . ImageField(null=True, blank=True, upload_to= 'profil_fotolari/%Y/%m/')

    def __str__(self):
        return self.user.username

    #! Django default olarak admin dashboardda 's' takısı ekler. Admin D.daki görünen tablo ismini değiştirmek için : 
    class Meta:
        verbose_name_plural = 'Profiller'

    #! IMAGE RESIZE
    def save(self, * args, ** kwargs):
        super().save(* args, ** kwargs)
        #! profil oluşturulurken foto girildiyse devam etmesi hata vermemesi için : 
        if self.foto:
            img = Image.open(self.foto.path)
            if img.height > 600 or img.width > 600:
                output_size = (600, 600)
                img.thumbnail(output_size)
                img.save(self.foto.path)


class ProfilDurum(models.Model):
    #! auto_now_add = True => bir kere oluşturulur bir daha değişmez
    #! auyo_now=True => her güncellemede yenilenir.

    user_profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    durum_mesaji = models . CharField(max_length=240)
    yaratilma_zamani = models.DateTimeField(auto_now_add=True)
    guncellenme_zamani = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Profil Mesajları'

    #!self.user_profil, Profil nesnesini döndürür. str(self.user_profil) Profil nesnesi içindeki __str__ yi döndürür.
    def __str__(self):
        return str(self.user_profil)
