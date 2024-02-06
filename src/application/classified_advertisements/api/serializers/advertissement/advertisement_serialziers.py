import json
from rest_framework import serializers
from ....models.models import (
    Anuncio,
    RedesSociales,
    TiposCapacitaciones,
    VotoAnuncio,
    Mensajes,
)
from ..subCategory.subCategory_serializers import SubCategorySerializersView
from src.application.default.base_serializer import BaseSerializers


class TipoCapacitacionSerializers(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField()

    class Meta:
        fields = "__all__"


class RedesSocialesSerializers(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    name = serializers.CharField(read_only=True)
    link = serializers.CharField(read_only=True)

    class Meta:
        fields = "__all__"


class RedesHasSocialesSerializers(BaseSerializers):
    redes = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        fields = "__all__"


class AdvertisementsMensajes(BaseSerializers):
    mensaje = serializers.CharField(required=False)

    def create(self, validated_data):
        try:
            mensajes = validated_data.get("mensaje", "")
            return Mensajes.objects.create(mensaje=mensajes)
        except Exception as e:
            raise e

    class Meta:
        fields = "__all__"


class AdvertisementsMensajesView(BaseSerializers):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    mensaje = serializers.CharField(read_only=True)

    class Meta:
        fields = "__all__"


class AdvertisementSerializersView(BaseSerializers):
    id = serializers.IntegerField(read_only=True)
    nombre_emprendimiento = serializers.CharField(read_only=True)
    descripcion = serializers.CharField(read_only=True)
    telefono_emprendimiento = serializers.CharField(read_only=True)
    correo_emprendimiento = serializers.EmailField(read_only=True)
    corregimiento = serializers.CharField(read_only=True)
    municipio = serializers.CharField(read_only=True)
    redes = RedesSocialesSerializers(many=True, read_only=True, meta=False)
    direccion = serializers.CharField(read_only=True)
    subCategoria = SubCategorySerializersView(read_only=True)
    metodos_entrega = serializers.CharField(read_only=True)
    formas_pago = serializers.CharField(read_only=True)
    tipo_capacitacion = TipoCapacitacionSerializers(many=True, read_only=True)
    categoria = serializers.DictField(read_only=True)
    user_voted = serializers.BooleanField(read_only=True)
    nun_votos = serializers.IntegerField(read_only=True)
    logo = serializers.CharField(read_only=True)
    state = serializers.BooleanField(read_only=True)
    mensajes = AdvertisementsMensajesView(
        read_only=True, many=True, meta=True, excludes=["userCreate", "userUpdate"]
    )
    state_value = serializers.CharField(read_only=True)

    def to_representation(self, instance):
        results = super().to_representation(instance)
        results["formas_pago"] = [x for x in instance.formas_pago.split(",")]
        results["metodos_entrega"] = [x for x in instance.metodos_entrega.split(",")]
        results["categoria"] = {
            "id": instance.subCategoria.categoriaId.id,
            "name": instance.subCategoria.categoriaId.name,
        }
        results["subCategoria"] = {
            "id": instance.subCategoria.id,
            "name": instance.subCategoria.name,
            "categoriaId": {
                "id": instance.subCategoria.categoriaId.id,
                "name": instance.subCategoria.categoriaId.name,
            },
        }
        return results

    class Meta:
        fields = "__all__"


class AdvertisementVotoSerializers(BaseSerializers):
    emprendimiento = serializers.IntegerField()
    user = serializers.IntegerField()

    def create(self, validated_data):
        try:
            resulst = VotoAnuncio.objects.create(
                user_id=validated_data["user"],
                emprendimiento_id=validated_data["emprendimiento"],
            )

            return resulst
        except Exception as e:
            raise e


class AdvertisementSerializers(BaseSerializers):
    nombre_emprendimiento = serializers.CharField()
    descripcion = serializers.CharField()
    telefono_emprendimiento = serializers.CharField()
    correo_emprendimiento = serializers.EmailField()
    corregimiento = serializers.CharField(required=False)
    municipio = serializers.CharField(required=False)
    direccion = serializers.CharField()
    subCategoria = serializers.IntegerField()
    metodos_entrega = serializers.ListField()
    formas_pago = serializers.ListField()
    tipo_capacitacion = serializers.ListField()
    redes = serializers.ListField()
    logo = serializers.FileField(required=False)
    visible = serializers.BooleanField(required=False, write_only=True)

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        metodos_entrega = ",".join(validated_data["metodos_entrega"])
        formas_pago = ",".join(validated_data["formas_pago"])

        anuncio = Anuncio.objects.create(
            nombre_emprendimiento=validated_data["nombre_emprendimiento"],
            descripcion=validated_data["descripcion"],
            telefono_emprendimiento=validated_data["telefono_emprendimiento"],
            correo_emprendimiento=validated_data["correo_emprendimiento"],
            corregimiento=validated_data.get("corregimiento", ""),
            municipio=validated_data.get("municipio", ""),
            direccion=validated_data["direccion"],
            userCreate=validated_data["userCreate"],
            subCategoria_id=int(validated_data["subCategoria"]),
            metodos_entrega=metodos_entrega,
            formas_pago=formas_pago,
            logo=validated_data.pop("logo", None),
        )

        tipo_capacitacion = validated_data.pop("tipo_capacitacion", None)
        print(list(map(int, tipo_capacitacion[0].split(","))))

        if tipo_capacitacion != None:
            if len(tipo_capacitacion):
                capacitaciones = TiposCapacitaciones.objects.filter(
                    pk__in=list(map(int, tipo_capacitacion[0].split(",")))
                    # pk__in=tipo_capacitacion
                )
                for capacitacion in capacitaciones:
                    anuncio.tipo_capacitacion.add(capacitacion)

        redes = json.loads(validated_data.pop("redes", None)[0])
        for red in redes:
            anuncio.redes.add(
                RedesSociales.objects.create(
                    link=red["link"], name=red["name"] if "name" in red else None
                ).pk
            )

        return anuncio

    def update(self, instance, validated_data):
        metodos_entrega = (
            ",".join(validated_data["metodos_entrega"])
            if "metodos_entrega" in validated_data != None
            else instance.metodos_entrega
        )
        formas_pago = (
            ",".join(validated_data["formas_pago"])
            if "formas_pago" in validated_data != None
            else instance.formas_pago
        )

        if len(validated_data.get("tipo_capacitacion", [])):
            instance.tipo_capacitacion.remove(*instance.tipo_capacitacion.all())

            capacitaciones = TiposCapacitaciones.objects.filter(
                pk__in=validated_data.pop("tipo_capacitacion", None)
            )
            instance.tipo_capacitacion.add(*capacitaciones)

        instance.nombre_emprendimiento = validated_data.get(
            "nombre_emprendimiento", instance.nombre_emprendimiento
        )
        instance.descripcion = validated_data.get("descripcion", instance.descripcion)
        instance.telefono_emprendimiento = validated_data.get(
            "telefono_emprendimiento", instance.telefono_emprendimiento
        )
        instance.correo_emprendimiento = validated_data.get(
            "correo_emprendimiento", instance.correo_emprendimiento
        )
        instance.corregimiento = validated_data.get(
            "corregimiento", instance.corregimiento
        )
        instance.municipio = validated_data.get("municipio", instance.municipio)
        instance.direccion = validated_data.get("direccion", instance.direccion)
        instance.subCategoria_id = validated_data.get(
            "subCategoria", instance.subCategoria.id
        )
        instance.metodos_entrega = metodos_entrega
        instance.formas_pago = formas_pago
        instance.tipo_capacitacion_id = validated_data.get(
            "tipo_capacitacion", instance.tipo_capacitacion
        )
        instance.visible = validated_data.get("visible", instance.visible)

        redes = validated_data.pop("redes", [])
        results = RedesSociales.objects.filter(id__in=[x["id"] for x in redes])

        for i, red in enumerate(results):
            red.link = redes[i]["link"]

        RedesSociales.objects.bulk_update(results, ["link"])
        instance.save()
        return instance
