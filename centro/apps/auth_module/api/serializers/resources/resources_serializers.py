from ....models import Resources
from rest_framework.serializers import ModelSerializer


class ResourcesSerializers(ModelSerializer):
    class Meta:
        model = Resources
        fields = '__all__'
