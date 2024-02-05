from rest_framework.routers import Route, SimpleRouter
from src.factory.auth_interactor import AuthViewSetFactory
from src.interfaces.routes.auth_module.resources import router
from src.application.auth_module.models import Resources


class Router(SimpleRouter):
    router_base = router
    name_base = "resources"
    model = Resources

    routes = [
        Route(
            url=router_base.get_url(f"{name_base}_get"),
            mapping=router_base.map(f"{name_base}_get"),
            initkwargs={
                "viewset_factory": AuthViewSetFactory,
                "http_method_names": ["get"],
                "model": model,
            },
            name="{basename}-list",
            detail=True,
        ),
        Route(
            url=router_base.get_url(f"{name_base}_post"),
            mapping=router_base.map(f"{name_base}_post"),
            initkwargs={
                "viewset_factory": AuthViewSetFactory,
                "http_method_names": ["post"],
                "model": model,
            },
            name="{basename}-create",
            detail=True,
        ),
        Route(
            url=router_base.get_url(f"{name_base}_retrieve"),
            mapping=router_base.map(f"{name_base}_retrieve"),
            initkwargs={
                "viewset_factory": AuthViewSetFactory,
                "http_method_names": ["get"],
                "model": model,
            },
            name="{basename}-retrieve",
            detail=True,
        ),
    ]
