from apps.interfaces.repository.classified.classified_repository import (
    ClassifiedRepository,
)
from apps.interfaces.repository.classified.repository_provider import (
    ClassifiedProviderRepository,
)
from apps.interfaces.controllers.classified.classified_controller import (
    ClassifiedController,
)
from apps.usecases.classified.interactor import ClassifiedInteractor


class DatabaseRepositoryFactory:
    @staticmethod
    def get(model):
        return ClassifiedRepository(model)


class ProviderFactory:
    @staticmethod
    def get(model):
        db_repo = DatabaseRepositoryFactory.get(model)
        return ClassifiedProviderRepository(db_repo)


class InteractorFactory:
    @staticmethod
    def get(model):
        repo = ProviderFactory().get(model)
        return ClassifiedInteractor(repo)


class BaseViewSetFactory:
    @staticmethod
    def create(model, serializer):
        current_iterator = InteractorFactory.get(model)

        return ClassifiedController(current_iterator, serializer)
