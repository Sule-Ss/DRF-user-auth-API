from django.apps import AppConfig


class ProfillerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiller'

    #! signalleri eklemek için : 
    def ready(self):
        import profiller.signals


#! Hata almayı engellemek için __init__.py dodsyasına ekleme yapıldı.