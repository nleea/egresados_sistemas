from ....models import Genders
from rest_framework.serializers import ModelSerializer


class GenderSerializers(ModelSerializer):
    class Meta:
        model = Genders
        fields = '__all__'
