from django.apps import AppConfig

AUTO_FIELD = "django.db.models.BigAutoField"


class AuthConfig(AppConfig):
    default_auto_field = AUTO_FIELD
    name = "apps.auth_module"
    label = "auth"
    verbose_name = "Auth"


class ClassifiedAdvertisementsConfig(AppConfig):
    default_auto_field = AUTO_FIELD
    name = "apps.classified_advertisements"
    label = "classified_advertisements"
    verbose_name = "Classified_advertisements"


class EncuestasConfig(AppConfig):
    default_auto_field = AUTO_FIELD
    name = "apps.encuestas"
    label = "encuestas"
    verbose_name = "Encuestas"


class EventosConfig(AppConfig):
    default_auto_field = AUTO_FIELD
    name = "apps.eventos"
    label = "eventos"
    verbose_name = "Eventos"


class PqrsConfig(AppConfig):
    default_auto_field = AUTO_FIELD
    name = "apps.pqrs"
    label = "pqrs"
    verbose_name = "PQRS"

    def ready(self) -> None:
        from apps.pqrs import receivers


class ReportesConfig(AppConfig):
    default_auto_field = AUTO_FIELD
    name = "apps.reportes"
    label = "reportes"
    verbose_name = "Reportes"
