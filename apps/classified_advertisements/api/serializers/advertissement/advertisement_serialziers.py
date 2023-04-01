from rest_framework import serializers
from ....models.models import Anuncio, SubCategoria, RedesSociales, AnuncioHasRedes, TiposCapacitaciones
from ..subCategory.subCategory_serializers import SubCategorySerializers
from apps.auth_module.api.serializers.user.users_serializers import UserSerializersSimple
from ..BaseSerializers import BaseSerializers


class TipoCapacitacionSerializers(BaseSerializers):

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

    def to_representation(self, instance):

        redes = RedesSociales.objects.filter(anuncio=instance.id)

        return {
            "id": instance.id,
            "nombre_emprendimiento": instance.nombre_emprendimiento,
            "descripción": instance.descripción,
            "telefono_emprendimiento": instance.telefono_emprendimiento,
            "correo_emprendimiento": instance.correo_emprendimiento,
            "ciudad": instance.ciudad,
            "municipio": instance.municipio,
            "redes": [{"link": x.link, "name": x.name} for x in redes.iterator()],
            "direccion": instance.direccion,
            "subCategoria": instance.subCategori.name,
            "metodos_entrega": [x for x in instance.metodos_entrega.split(",")],
            "formas_pago": [x for x in instance.formas_pago.split(",")],
            "tipo_capacitacion": [{"name": x.name, "id": x.id}for x in instance.tipo_capacitacion.prefetch_related("anuncio").iterator()]
        }

    id = serializers.PrimaryKeyRelatedField(read_only=True)
    nombre_emprendimiento = serializers.CharField()
    descripción = serializers.CharField()
    telefono_emprendimiento = serializers.CharField()
    correo_emprendimiento = serializers.EmailField()
    ciudad = serializers.CharField()
    municipio = serializers.CharField()
    redes = RedesSocialesSerializers(many=True, read_only=True)
    direccion = serializers.CharField()
    subCategori = serializers.PrimaryKeyRelatedField(read_only=True)
    metodos_entrega = serializers.CharField()
    formas_pago = serializers.CharField()
    tipo_capacitacion = TipoCapacitacionSerializers(many=True, read_only=True)

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

        redes = []

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
            for capacitacion in validated_data.pop("tipo_capacitacion", None):
                anuncio.tipo_capacitacion.add(
                    TiposCapacitaciones.objects.get(pk=capacitacion))

        if len(validated_data.get("redes", None)):
            for red in validated_data.pop("redes", None):
                redes.append(RedesSociales(
                    link=red["link"], anuncio_id=anuncio.pk))
            RedesSociales.objects.bulk_create(redes)

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
