from ....models import Document_types
from rest_framework.serializers import ModelSerializer,Serializer,CharField

class DocumentSerializersView(Serializer):

    name = CharField(read_only=True)

    class Meta:
        fields = '__all__'

class DocumentSerializers(ModelSerializer):
    class Meta:
        model = Document_types
        fields = '__all__'
