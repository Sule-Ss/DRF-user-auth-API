
from django.urls import path, include
# from profiller.api import views
from profiller.api.views import ProfilViewSet, ProfilDurumViewSet, ProfilFotoUpdateView
from rest_framework.routers import DefaultRouter

#! viewSetler ve router lar beraber çalışırlar.
router = DefaultRouter()
#! ham bir text ollduğu için başına r harfi konur.
router.register(r'profiller', ProfilViewSet)
#! queryset vermeyip get_queryset metoduyla işimizi hallettiğimiz için AssertionError almayı önleemek için basename kullanmaıyız.
router.register(r'durum', ProfilDurumViewSet, basename='durum')

urlpatterns = [
      #! router.urls bir liste yapısı olduğu için bütün registerları kapsar.
      path('', include(router.urls)),
      #! ProfilFotoUpdateView bir viewSet olmadığı için yeni bir path yazıyoruz.
      path('profil-foto/', ProfilFotoUpdateView.as_view(), name = 'profil-foto')
]

# #! .asview() içerisine hangi metodu yazarsak onu gerçekleştirir :
# profil_list = ProfilViewSet.as_view({'get': 'list'})
# profil_detay = ProfilViewSet.as_view({'get': 'retrieve'})

#!her defasında tek tek yazmamak için router yöntemi kullanılabilir.
# urlpatterns = [
#     path("kullanici-profilleri/", profil_list, name="profiller"),
#     path("kullanici-profilleri/<int:pk>/", profil_detay, name="profil-detay"),
# ]
