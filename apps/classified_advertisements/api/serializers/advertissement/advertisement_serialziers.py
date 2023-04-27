from rest_framework import serializers
from ....models.models import Anuncio, SubCategoria, RedesSociales, TiposCapacitaciones
from ..subCategory.subCategory_serializers import SubCategorySerializers
from apps.auth_module.api.serializers.user.users_serializers import UserSerializersSimple
from ..BaseSerializers import BaseSerializers


class TipoCapacitacionSerializers(BaseSerializers):
    name = serializers.CharField()

    class Meta:
        fields = "__all__"


class RedesSocialesSerializers(BaseSerializers):
    link = serializers.CharField()

    class Meta:
        fields = '__all__'


class RedesHasSocialesSerializers(BaseSerializers):
    redes = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = '__all__'


class AdvertisementSerializersView(BaseSerializers):

    id = serializers.IntegerField(read_only=True)
    nombre_emprendimiento = serializers.CharField(read_only=True)
    descripción = serializers.CharField(read_only=True)
    telefono_emprendimiento = serializers.CharField(read_only=True)
    correo_emprendimiento = serializers.EmailField(read_only=True)
    ciudad = serializers.CharField(read_only=True)
    municipio = serializers.CharField(read_only=True)
    redes = RedesSocialesSerializers(many=True, read_only=True)
    direccion = serializers.CharField(read_only=True)
    subCategori = serializers.CharField(read_only=True)
    metodos_entrega = serializers.CharField(read_only=True)
    formas_pago = serializers.CharField(read_only=True)
    tipo_capacitacion = TipoCapacitacionSerializers(many=True, read_only=True)

    def to_representation(self, instance):
        results = super().to_representation(instance)
        results["formas_pago"] = instance.formas_pago.split(",")
        return results

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
    subCategori = serializers.IntegerField()
    metodos_entrega = serializers.ListField()
    formas_pago = serializers.ListField()
    tipo_capacitacion = serializers.ListField()

    class Meta:
        fields = "__all__"

    def create(self, validated_data):

        metodos_entrega = ",".join(validated_data["metodos_entrega"])
        formas_pago = ",".join(validated_data["formas_pago"])

        anuncio = Anuncio.objects.create(nombre_emprendimiento=validated_data["nombre_emprendimiento"],
                                         descripción=validated_data["descripción"], telefono_emprendimiento=validated_data[
                                             "telefono_emprendimiento"],
                                         correo_emprendimiento=validated_data[
                                             "correo_emprendimiento"], ciudad=validated_data["ciudad"],
                                         municipio=validated_data["municipio"], direccion=validated_data[
                                             "direccion"], userCreate=validated_data["userCreate"],
                                         subCategori_id=validated_data["subCategori"], metodos_entrega=metodos_entrega,
                                         formas_pago=formas_pago)

        if len(validated_data.get("tipo_capacitacion", None)):
            capacitaciones = TiposCapacitaciones.objects.filter(pk__in=validated_data.pop("tipo_capacitacion", None))
            for capacitacion in capacitaciones:
                anuncio.tipo_capacitacion.add(capacitacion)

        if len(validated_data.get("redes", None)):
            for red in validated_data.pop("redes", None):
                anuncio.redes.add(RedesSociales.objects.create(
                    link=red["link"]).pk)

        return anuncio

    def update(self, instance, validated_data):
        metodos_entrega = ",".join(
            validated_data["metodos_entrega"]) if "metodos_entrega" in validated_data != None else instance.metodos_entrega
        formas_pago = ",".join(
            validated_data["formas_pago"]) if "formas_pago" in validated_data != None else instance.formas_pago
        instance.nombre_emprendimiento = validated_data.get(
            'nombre_emprendimiento', instance.nombre_emprendimiento)
        instance.descripción = validated_data.get(
            'descripción', instance.descripción)
        instance.telefono_emprendimiento = validated_data.get(
            'telefono_emprendimiento', instance.telefono_emprendimiento)
        instance.correo_emprendimiento = validated_data.get(
            'correo_emprendimiento', instance.correo_emprendimiento)
        instance.ciudad = validated_data.get('ciudad', instance.ciudad)
        instance.municipio = validated_data.get(
            'direccion', instance.municipio)
        instance.direccion = validated_data.get(
            'direccion', instance.direccion)
        instance.subCategori_id = validated_data.get(
            'subCategori', instance.subCategori)
        instance.metodos_entrega = metodos_entrega
        instance.formas_pago = formas_pago
        instance.tipo_capacitacion_id = validated_data.get(
            'tipo_capacitacion', instance.tipo_capacitacion)
        instance.save()
        return instance
