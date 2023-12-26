from rest_framework import status


class BaseController:
    def __init__(self, repo, serializer) -> None:
        self.repo = repo
        self.serializer = serializer

    def get_filter_related(self, filter_param=None, related=None):
        resp = self.repo.get_filter_related(filter_param, related)
        serializer = self.serializer(resp, many=True)
        return serializer.data, status.HTTP_200_OK

    def get(self):
        resp = self.repo.get()
        serializer = self.serializer(resp, many=True)
        return serializer.data, status.HTTP_200_OK

    def post(self, data):
        serializers = self.serializer(data=data)
        if serializers.is_valid():
            serializers.save()
            return "Ok", status.HTTP_201_CREATED
        return serializers.errors, status.HTTP_400_BAD_REQUEST

    def put(self, id: int, data):
        instance = self.repo.get_instance(id)

        if not instance:
            return "NOT FOUND", status.HTTP_400_BAD_REQUEST

        serializers = self.serializer(instance, data=data)
        if serializers.is_valid():
            serializers.save()
            return "Ok", status.HTTP_200_OK
        return serializers.errors, status.HTTP_400_BAD_REQUEST

    def delete(self, id, ids=None):
        if ids:
            err, valid = self.repo.bulk_delete(ids)

            if valid:
                return err, status.HTTP_400_BAD_REQUEST

            return "Ok", status.HTTP_200_OK

        instance = self.repo.get_instance(id)
        instance.delete()

        return "Ok", status.HTTP_200_OK
