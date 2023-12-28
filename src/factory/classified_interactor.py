from src.interfaces.repository.classified.classified_repository import (
    ClassifiedRepository,
)
from src.interfaces.repository.classified.repository_provider import (
    ClassifiedProviderRepository,
)
from src.interfaces.controllers.classified.classified_controller import (
    ClassifiedController,
)
from src.usecases.classified.interactor import ClassifiedInteractor


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
