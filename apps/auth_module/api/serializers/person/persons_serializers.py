from ....models import Persons
from rest_framework.serializers import ModelSerializer,Serializer,CharField,DateField
from ..document.document_serializers import DocumentSerializersView
from ..gender.gender_Serializers import GenderSerializers
from ..user.users_serializers import UserSerializersSimple


class PersonsSerializers(ModelSerializer):
    document_type = DocumentSerializersView(read_only=True)
    gender_type = GenderSerializers(read_only=True)
    user = UserSerializersSimple(read_only=True,expands=False)

    class Meta:
        model = Persons
        fields = '__all__'


class PersonsSimpleSerializers(Serializer):
    name  = CharField(read_only=True)
    document_type = CharField(read_only=True)
    surname  = CharField(read_only=True)
    identification  = CharField(read_only=True)
    address  = CharField(read_only=True)
    nationality  = CharField(read_only=True)
    date_of_birth = DateField(read_only=True)
    gender_type = CharField(read_only=True)
    phone = CharField(read_only=True)


    class Meta:
        fields = "__all__"
