from rest_framework import serializers
from ....models.models import Anuncio,SubCategoria,RedesSociales,AnuncioHasRedes
from ..subCategory.subCategory_serializers import SubCategorySerializers
from apps.auth_module.api.serializers.user.users_serializers import UserSerializersSimple
from ..BaseSerializers import BaseSerializers


class RedesSocialesSerializers(BaseSerializers):
    link = serializers.CharField()
    
    class Meta:
        fields = '__all__'

class RedesHasSocialesSerializers(BaseSerializers):
    redes = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        fields = '__all__'

class AdvertisementSerializersView(BaseSerializers):
    nombre_emprendimiento = serializers.CharField()
    descripción = serializers.CharField()
    telefono_emprendimiento = serializers.CharField()
    correo_emprendimiento = serializers.EmailField()
    ciudad = serializers.CharField()
    redes = RedesHasSocialesSerializers(many=True,read_only=True)
    municipio = serializers.CharField()
    direccion = serializers.CharField()
    persona_id = serializers.PrimaryKeyRelatedField(read_only=True)
    subCategori = serializers.PrimaryKeyRelatedField(read_only=True)
    entrega_cuentas = serializers.CharField()
    formas_pago = serializers.CharField()
    capacitacion = serializers.CharField()
    tipo_capacitacion = serializers.PrimaryKeyRelatedField(read_only=True)
    
    class Meta:
        fields = '__all__'

class AdvertisementSerializers(BaseSerializers):

    nombre_emprendimiento = serializers.CharField()
    descripción = serializers.CharField()
    telefono_emprendimiento = serializers.CharField()
    correo_emprendimiento = serializers.EmailField()
    ciudad = serializers.CharField()
    municipio = serializers.CharField()
    direccion = serializers.CharField()
    persona_id = serializers.IntegerField()
    subCategori = serializers.IntegerField()
    entrega_cuentas = serializers.CharField()
    formas_pago = serializers.CharField()
    capacitacion = serializers.CharField()
    tipo_capacitacion = serializers.IntegerField()

    class Meta:
        fields = "__all__"
        
    
    def create(self, validated_data):
        
        redes = []
        
        for red in validated_data.pop("redes",None):
            redes.append(RedesSociales(link=red["link"]))
            
        ids_anteriores = RedesSociales.objects.values_list('id', flat=True)
        redes = RedesSociales.objects.bulk_create(redes)
        anuncio = Anuncio.objects.create(nombre_emprendimiento=validated_data["nombre_emprendimiento"],
        descripción=validated_data["descripción"],telefono_emprendimiento=validated_data["telefono_emprendimiento"],
        correo_emprendimiento=validated_data["correo_emprendimiento"],ciudad=validated_data["ciudad"],
        municipio=validated_data["municipio"],direccion=validated_data["direccion"],persona_id_id=validated_data["persona_id"],
        subCategori_id=validated_data["subCategori"],entrega_cuentas=validated_data["entrega_cuentas"],
        formas_pago=validated_data["formas_pago"],capacitacion=validated_data["capacitacion"],
        tipo_capacitacion_id=validated_data["tipo_capacitacion"])
        ids_nuevos = RedesSociales.objects.filter(id__gt=max(ids_anteriores)).values_list('id', flat=True)
        objetos = zip(redes, ids_nuevos)

        for _,i in objetos:
            AnuncioHasRedes.objects.create(anuncio_id=anuncio.pk,redes_id=i.pk,tipo="red")
        return anuncio


    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.categoriId_id = validated_data.get("categoriId",instance.categoriId)
        instance.userUpdate = validated_data.get('userUpdate', instance.userUpdate)
        instance.save()
        return instance