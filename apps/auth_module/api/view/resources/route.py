from rest_framework.routers import Route, SimpleRouter
from apps.factory.base_interactor import BaseViewSetFactory
from apps.interfaces.routes.auth_module.resources import router
from apps.auth_module.models import Resources


class Router(SimpleRouter):
    router_base = router
    name_base = "resources"
    model = Resources

    routes = [
        Route(
            url=router_base.get_url(f"{name_base}_get"),
            mapping=router_base.map(f"{name_base}_get"),
            initkwargs={
                "viewset_factory": BaseViewSetFactory,
                "http_method_names": ["get"],
                "model": model,
            },
            name="{basename}-list",
            detail=True,
        )
    ]
