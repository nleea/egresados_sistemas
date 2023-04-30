from django.db import models

class SubCategoryManagers(models.Manager):
    def filter_subcategory_has_category(self, categoriId):
        subCategory = self.filter(categoriaId=int(categoriId)).defer("userCreate","userUpdate","categoriaId__userCreate_id","categoriaId__userUpdate_id").select_related("categoriaId")
        return subCategory


class AdvertisementsManagers(models.Manager):
    def filter_Advertisement_subCategory(self, subCategoryId):
        advertisements = self.filter(subCategoria=int(subCategoryId)).defer("tipo_capacitacion","userCreate","userUpdate","subCategoria__userCreate_id","subCategoria__userUpdate_id").select_related("subCategoria")
        return advertisements
