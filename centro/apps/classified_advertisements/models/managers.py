from django.db import models


class SubCategoryManagers(models.Manager):
    def create_subcategory(self,name,categoriId):
        subCategory = self.create(name=name,categoriId_id=int(categoriId))
        return subCategory