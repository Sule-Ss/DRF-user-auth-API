from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiller.models import Profil, ProfilDurum
from profiller.api.serializers import ProfilSerializer, ProfilDurumSerializer, ProfilFotoSerializer

from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from profiller.api.permissions import KendiProfiliYadaReadOnly, DurumSahibiYadaReadOnly
from rest_framework.filters import SearchFilter


#! Bütün CRUD işlemlerini tek bir viewde çözmek için : 
class ProfilViewSet(
            mixins.ListModelMixin,
            mixins.RetrieveModelMixin,
            #! UpdateModelMixin le beraber browser da HTML form gelir.  
            mixins.UpdateModelMixin,
            # mixins.DestroyModelMixin,
            GenericViewSet):

    queryset = Profil.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = (IsAuthenticated,KendiProfiliYadaReadOnly)      
    filter_backends = (SearchFilter,)  # birden fazla arama filtresi dahil edilebilir
    search_fields = ("sehir",)  # profil modeline ait arama yapilmasi istenen field'lar

#! ModelViewSet kaynak kodunu incele!
class ProfilDurumViewSet(ModelViewSet):
    queryset = ProfilDurum.objects.all()
    serializer_class = ProfilDurumSerializer
    permission_classes = (IsAuthenticated,DurumSahibiYadaReadOnly)

    #! filtreleme yapmak için :
    def get_queryset(self):
        queryset = ProfilDurum.objects.all() # filtreleme yapmak icin queryset burada aliyoruz
        username = self.request.query_params.get("username", None) # url'imizde belirleyecegimiz username parametresi

        if username:
            #! models dan user profil(Profil nesnesi)in içindeki user ın username i:
            queryset = queryset.filter(user_profil__user__username=username)
        
        return queryset

    def perform_create(self, serializer):
        #! profil, user ın related nameinden gelir.
        user_profil = self.request.user.profil
        serializer.save(user_profil = user_profil)


class ProfilFotoUpdateView(generics.UpdateAPIView):
    # UpdateApiView aldığımız için sadece PUT request e izin vermiş oluyoruz.
    # serializer'imizda sadece foto alanini dahil etmistik
    # bu sebele bir update aksiyonunda sadece profil alani etkilenecek
    serializer_class = ProfilFotoSerializer
    permission_class = (IsAuthenticated,)
    # izin yazmamiza gerek yok, cunku get_object ile kisitladik

    def get_object(self):
        # bize tek bir profil nesnesi lazim
        # bu sebele queryset belirlemiyoruz ve GenericAPIView ile
        # gelen get_object metodunu override ediyoruz
        profil_nesnesi = self.request.user.profil
        return profil_nesnesi




# class ProfilViewSet(ReadOnlyModelViewSet):
#     queryset = Profil.objects.all()
#     serializer_class = ProfilSerializer
#     #! Sadece login olmuş kullanıcılara listeleme yapmak için :
#     permission_classes = (IsAuthenticated,)



# ?----------------------------------------------------------

#! client() içinde get ile istek atacağız o yüzden ListAPIView kullandık.
#! post metodunu kullanacak olsaydık .CreateAPIView kullanmamız gerekirdi.
#! Mevcut kullanıcı profillerini görüntüleyebilmek için : 

# class ProfilList(generics.ListAPIView):
#     queryset = Profil.objects.all()
#     serializer_class = ProfilSerializer
#     #! Sadece login olmuş kullanıcılara listeleme yapmak için :
#     permission_classes = (IsAuthenticated,)
# ?----------------------------------------------------------

