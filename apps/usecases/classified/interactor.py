from apps.usecases.base_interactor import BaseInteractor


class ClassifiedInteractor(BaseInteractor):
    def __init__(self, repo) -> None:
        super().__init__(repo)

    def anuncio_subCategory(self, sub_category, user_id):
        return self.repo.anuncio_subCategory(sub_category, user_id)
