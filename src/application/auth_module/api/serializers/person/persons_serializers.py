from ....models import Persons
from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    CharField,
    DateField,
    IntegerField,
    PrimaryKeyRelatedField,
)
from ..document.document_serializers import DocumentSerializersView
from ..gender.gender_Serializers import GenderSerializersView
from ..user.users_serializers import UserSerializersSimple
from rest_framework.validators import UniqueValidator



class PersonsSerializers(ModelSerializer):
    document_type = DocumentSerializersView(read_only=True)
    gender_type = GenderSerializersView(read_only=True)
    user = UserSerializersSimple(read_only=True, expands=False)

    class Meta:
        model = Persons
        exclude = ("createdAt", "updateAt", "visible")


class PersonsSimpleSerializersView(Serializer):
    id = PrimaryKeyRelatedField(read_only=True)
    name = CharField(read_only=True)
    document_type = DocumentSerializersView(read_only=True)
    surname = CharField(read_only=True)
    identification = CharField(read_only=True)
    address = CharField(read_only=True)
    nationality = CharField(read_only=True)
    date_of_birth = DateField(read_only=True)
    gender_type = GenderSerializersView(read_only=True)
    phone = CharField(read_only=True)


class PersonsSimpleSerializers(Serializer):
    name = CharField()
    document_type = IntegerField()
    surname = CharField()
    identification = IntegerField()
    address = CharField()
    nationality = CharField()
    date_of_birth = DateField()
    gender_type = CharField()
    phone = CharField()

    class Meta:
        fields = "__all__"

    def create(self, validated_data):
        person = Persons.objects.create(
            name=validated_data["name"],
            document_type_id=validated_data["document_type"],
            surname=validated_data["surname"],
            identification=validated_data["identification"],
            address=validated_data["address"],
            nationality=validated_data["nationality"],
            date_of_birth=validated_data["date_of_birth"],
            gender_type_id=validated_data["gender_type"],
            phone=validated_data["phone"],
        )
        return person

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.document_type_id = validated_data.get(
            "document_type", instance.document_type
        )
        instance.surname = validated_data.get("surname", instance.surname)
        instance.identification = validated_data.get(
            "identification", instance.identification
        )
        instance.address = validated_data.get("address", instance.address)
        instance.nationality = validated_data.get("nationality", instance.nationality)
        instance.date_of_birth = validated_data.get(
            "date_of_birth", instance.date_of_birth
        )
        instance.gender_type_id = validated_data.get(
            "gender_type", instance.gender_type
        )
        instance.phone = validated_data.get("phone", instance.phone)

        instance.save()
        return instance


queryset = Persons.objects.all()


class PersonsSerializer(Serializer):
    name = CharField(write_only=True, validators=[UniqueValidator(queryset=queryset)])
    surname = CharField(write_only=True, required=False)
    identification = CharField(
        write_only=True, required=False, validators=[UniqueValidator(queryset=queryset)]
    )
    address = CharField(write_only=True, required=False)
    nationality = CharField(write_only=True, required=False)
    date_of_birth = DateField(write_only=True, required=False)
    phone = CharField(write_only=True, required=False)
