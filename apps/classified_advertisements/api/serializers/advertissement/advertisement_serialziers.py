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
    
    
    def to_representation(self, instance):
        
        redes = RedesSociales.objects.filter(anuncio=instance.id)
        
        return {
            "id":instance.id ,
            "nombre_emprendimiento":instance.nombre_emprendimiento,
            "descripción" : instance.descripción,
            "telefono_emprendimiento" : instance.telefono_emprendimiento,
            "correo_emprendimiento" : instance.correo_emprendimiento,
            "ciudad" : instance.ciudad,
            "municipio" : instance.municipio,
            "redes" : [{"link":x.link,"name":x.name} for x in redes],
            "direccion" : instance.direccion,
            "persona" : instance.persona_id.username,
            "subCategoria" : instance.subCategori.name,
            "entrega_cuentas" : instance.entrega_cuentas,
            "formas_pago" : instance.formas_pago,
            "capacitacion" : instance.capacitacion,
            "tipo_capacitacion" : instance.tipo_capacitacion.id,
        }
    
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    nombre_emprendimiento = serializers.CharField()
    descripción = serializers.CharField()
    telefono_emprendimiento = serializers.CharField()
    correo_emprendimiento = serializers.EmailField()
    ciudad = serializers.CharField()
    municipio = serializers.CharField()
    redes = RedesSocialesSerializers(many=True,read_only=True)
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
        
        
        anuncio = Anuncio.objects.create(nombre_emprendimiento=validated_data["nombre_emprendimiento"],
        descripción=validated_data["descripción"],telefono_emprendimiento=validated_data["telefono_emprendimiento"],
        correo_emprendimiento=validated_data["correo_emprendimiento"],ciudad=validated_data["ciudad"],
        municipio=validated_data["municipio"],direccion=validated_data["direccion"],persona_id_id=validated_data["persona_id"],
        subCategori_id=validated_data["subCategori"],entrega_cuentas=validated_data["entrega_cuentas"],
        formas_pago=validated_data["formas_pago"],capacitacion=validated_data["capacitacion"],
        tipo_capacitacion_id=validated_data["tipo_capacitacion"])
        
        for red in validated_data.pop("redes",None):
            redes.append(RedesSociales(link=red["link"],anuncio=anuncio.pk))
        redes = RedesSociales.objects.bulk_create(redes)
        
        return anuncio


    def update(self, instance, validated_data):
        instance.nombre_emprendimiento = validated_data.get('nombre_emprendimiento', instance.nombre_emprendimiento)
        instance.descripción = validated_data.get('descripción', instance.descripción)
        instance.telefono_emprendimiento = validated_data.get('telefono_emprendimiento', instance.telefono_emprendimiento)
        instance.correo_emprendimiento = validated_data.get('correo_emprendimiento', instance.correo_emprendimiento)
        instance.ciudad = validated_data.get('ciudad', instance.ciudad)
        instance.municipio = validated_data.get('direccion', instance.municipio)
        instance.direccion = validated_data.get('persona_id', instance.direccion)
        instance.persona_id_id = validated_data.get('persona_id', instance.persona_id)
        instance.subCategori_id = validated_data.get('subCategori', instance.subCategori)
        instance.entrega_cuentas = validated_data.get('entrega_cuentas', instance.entrega_cuentas)
        instance.formas_pago = validated_data.get('formas_pago', instance.formas_pago)
        instance.capacitacion = validated_data.get('capacitacion', instance.capacitacion)
        instance.tipo_capacitacion_id = validated_data.get('tipo_capacitacion', instance.tipo_capacitacion)
        instance.save()
        return instance
