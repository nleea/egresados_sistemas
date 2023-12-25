from abc import ABC


class ProviderRepository(ABC):
    def __init__(self, repo) -> None:
        self.repo = repo

    def get_instance(self, id):
        return self.repo.get_instance(id)

    def bulk_delete(self, ids):
        return self.repo.bulk_delete(ids)

    def get(self):
        return self.repo.get()

    def post(self, data):
        return self.repo.post(data)

    def put(self, id, data):
        return self.repo.put(id, data)

    def delete(self, id):
        return self.repo.delete(id)
