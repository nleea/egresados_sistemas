from src.application.classified_advertisements.models.models import SubCategoria
from src.application.classified_advertisements.api.serializers.subCategory.subCategory_serializers import (
    SubCategorySerializersView,
)
from src.interfaces.controllers.base_controller import BaseController
from rest_framework import status


class ClassifiedController(BaseController):
    def __init__(self, repo, serializer) -> None:
        super().__init__(repo, serializer)

    def mine(self, **kwargs):
        return self.repo.complex_filters(**kwargs)

    def save_voto(self, data):
        return self.post(data)

    def most_view(self, **kwargs):
        return self.repo.complex_filters(**kwargs)

    def query(self, sub_category, user_id, excludes=[]):
        try:
            resp = SubCategoria.objects.filter(categoriaId=sub_category)
            serializer = SubCategorySerializersView(resp, many=True)
            return serializer.data, 200
        except Exception as e:
            return e.args, 400

    def state_changes(self, id, data):
        instance = self.repo.get_instance(id)

        if isinstance(instance, str):
            return instance, status.HTTP_200_OK

        state = data.get("state", False)
        mensajes = data.get("mensajes", None)
        instance.change_state(state)

        if not state and mensajes:
            m_instance = self.serializer(data=data)
            if m_instance.is_valid():
                mensaje_instancia = m_instance.save()
                instance.mensajes.add(mensaje_instancia.id)
                return "Ok", status.HTTP_200_OK

            return m_instance.errors, status.HTTP_400_BAD_REQUEST
        return "Ok", status.HTTP_200_OK

    def anuncio_subCategory(self, sub_category, user_id):
        try:
            resp = self.repo.anuncio_subCategory(sub_category, user_id)
            return resp, status.HTTP_200_OK
        except Exception as e:
            return e.args, status.HTTP_400_BAD_REQUEST
