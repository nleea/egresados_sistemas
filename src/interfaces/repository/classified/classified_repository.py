from django.db import models
from src.interfaces.repository.base_repository import BaseRepository
from src.application.classified_advertisements.models.models import VotoAnuncio, Anuncio


class ClassifiedRepository(BaseRepository):
    def __init__(self, model: type[Anuncio]) -> None:
        super().__init__(model)
        self.model = model

    def anuncio_subCategory(self, sub_category, user_id):
        queryset = self.model.objects_subCategory.filter_Advertisement_subCategory(
            sub_category
        )
        resulst = queryset.annotate(
            user_voted=models.Exists(
                VotoAnuncio.objects.filter(
                    emprendimiento=models.OuterRef("pk"), user=user_id
                )
            )
        )

        return resulst
