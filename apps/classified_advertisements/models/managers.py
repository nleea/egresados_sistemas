from django.db import models

class SubCategoryManagers(models.Manager):
    def filter_subcategory_has_category(self, categoriId):
        subCategory = self.filter(categoriaId=int(categoriId))
        return subCategory


class AdvertisementsManagers(models.Manager):
    def filter_Advertisement_subCategory(self, subCategoryId):
        advertisements = self.filter(subCategori=int(subCategoryId))
        return advertisements

    def saveTipoCapacitaciones(self, name):
        pass
