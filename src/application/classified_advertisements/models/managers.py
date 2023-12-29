from django.db import models


class SubCategoryManagers(models.Manager):
    def filter_subcategory_has_category(self, categoria_id):
        sub_category = (
            self.filter(categoriaId=int(categoria_id))
            .defer(
                "userCreate",
                "userUpdate",
                "categoriaId__userCreate_id",
                "categoriaId__userUpdate_id",
            )
            .select_related("categoriaId")
        )
        return sub_category


class AdvertisementsManagers(models.Manager):
    def filter_Advertisement_subCategory(self, subcategory_id):
        advertisements = (
            self.filter(subCategoria=int(subcategory_id), visible=True)
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

