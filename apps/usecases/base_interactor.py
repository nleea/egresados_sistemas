class BaseInteractor:
    def __init__(self, repo) -> None:
        self.repo = repo

    def get_instance(self, data):
        return self.repo.get_instance(data)

    def bulk_delete(self, ids):
        return self.repo.bulk_delete(ids)

    def get(self) -> list:
        return self.repo.get()

    def post(self, data):
        return self.repo.post(data)

    def put(self, id: int, data):
        return self.repo.put(id, data)

    def delete(self, data: list[int]):
        return self.repo.delete(data)
