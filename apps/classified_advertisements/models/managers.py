from django.db import models


class SubCategoryManagers(models.Manager):
    def filter_subcategory_has_category(self, categoriId):
        subCategory = (
            self.filter(categoriaId=int(categoriId))
            .defer(
                "userCreate",
                "userUpdate",
                "categoriaId__userCreate_id",
                "categoriaId__userUpdate_id",
            )
            .select_related("categoriaId")
        )
        return subCategory


class AdvertisementsManagers(models.Manager):
    def filter_Advertisement_subCategory(self, subCategoryId):
        advertisements = (
            self.filter(subCategoria=int(subCategoryId), visible=True)
            .prefetch_related("redes", "tipo_capacitacion")
            .defer(
                "subCategoria__userCreate",
                "subCategoria__userUpdate_id",
                "subCategoria__categoriaId__userCreate",
                "subCategoria__categoriaId__userUpdate",
                "userCreate",
                "userUpdate",
            )
            .select_related("subCategoria", "subCategoria__categoriaId")
        )
        return advertisements

    def change_state(self, state):
        self.state = state
        return self.model

