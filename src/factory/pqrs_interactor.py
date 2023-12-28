from src.interfaces.repository.base_repository import BaseRepository
from src.interfaces.repository.provider_repository import ProviderRepository
from src.usecases.base_interactor import BaseInteractor
from src.interfaces.controllers.pqrs.pqrs_controller import PqrsController


class DatabaseRepositoryFactory:
    @staticmethod
    def get(model):
        return BaseRepository(model)


class ProviderFactory:
    @staticmethod
    def get(model):
        db_repo = DatabaseRepositoryFactory.get(model)

        return ProviderRepository(db_repo)


class MessageInteractorFactory:
    @staticmethod
    def get(model):
        repo = ProviderFactory().get(model)
        return BaseInteractor(repo)


class BaseViewSetFactory:
    @staticmethod
    def create(model, serializer):
        current_iterator = MessageInteractorFactory.get(model)

        return PqrsController(current_iterator, serializer)
