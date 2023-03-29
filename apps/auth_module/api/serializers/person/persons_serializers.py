from ....models import Persons
from rest_framework.serializers import ModelSerializer
from ..document.document_serializers import DocumentSerializers
from ..gender.gender_Serializers import GenderSerializers
from ..user.users_serializers import UserSerializersSimple


class PersonsSerializers(ModelSerializer):
    document_type = DocumentSerializers(read_only=True)
    gender_type = GenderSerializers(read_only=True)
    user = UserSerializersSimple(read_only=True)

    class Meta:
        model = Persons
        fields = '__all__'


class PersonsSimpleSerializers(ModelSerializer):
    document_type = DocumentSerializers(read_only=True)

    class Meta:
        model = Persons
        fields = ('name', 'surname', 'document_type',
                  'phone', 'status', 'date_of_birth')
