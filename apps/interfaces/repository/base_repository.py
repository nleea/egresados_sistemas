from abc import ABC
from django.db import models


class BaseRepository(ABC):
    def __init__(self, model: models.Model) -> None:
        self.model = model

    def get_instance(self, id):
        try:
            return self.model.objects.get(pk=id)
        except self.model.DoesNotExist:
            return None

    def bulk_delete(self, ids):
        try:
            instances = self.model.objects.filter(pk__in=ids)

            for _, instance in enumerate(instances):
                instance.visible = False

            self.model.objects.bulk_update(instances, ["visible"])
            return "Ok", True
        except Exception as e:
            return e.args, False

    def get(self):
        return self.model.objects.filter(visible=True)

    def post(self):
        return None

    def put(self):
        return None

    def delete(self):
        return None
