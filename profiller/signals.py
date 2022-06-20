from django.contrib.auth.models import User
from profiller.models import Profil, ProfilDurum

#! post_save in içerik dosyasına git. Signal zamanlamasını ayarlamak için.
from django.db.models.signals import post_save

#! receiver alıcı.Fonksiyonun ne zaman tetiklenmesi gerektiğinin belilendiği decorator.
from django.dispatch import receiver

#! sender =User => User modeli üzerinde post_save işlemi yapıldığında sinyali gönder demek.
#! Buradaki sinyalin alıcısı(receiver) User değil oluşturulan fonksiyon(create_profil).

@receiver(post_save, sender=User)

#! Fonksiyon isimleri unique olmalı dikkat
def create_profil(sender, instance, created, **kwargs):
    print(instance.username, '__Create : ', created)
    #! User üzerinden bir nesne oluşturulursa:
    if created:
        #! user=instance => Her defasında farklı bir user nesnesi yaratılacağı için 
        Profil.objects.create(user=instance)

#! App i signal den haberdar etmek için apps.py da import ederiz.(oraya bak) 


@receiver(post_save, sender=Profil)
def create_ilk_durum_mesaji(sender, instance, created, **kwargs):
 
    if created:
        ProfilDurum.objects.create(
            user_profil = instance,
            durum_mesaji= f'{instance.user.username} Klübe katıldı.',
        )




