from src.domain.routing import Route, Router
from src.domain.constants import (
    HTTP_VERB_GET,
    HTTP_VERB_POST,
    HTTP_VERB_DELETE,
    HTTP_VERB_PUT,
)
from src.interfaces.controllers.eventos.eventos_controller import EventosController

router = Router()

name_base = "eventos"

router.register(
    [
        Route(
            http_verb=HTTP_VERB_GET,
            path=r"$",
            controller=EventosController,
            method="get",
            name=f"{name_base}_get",
        ),
        # Route(
        #     http_verb=HTTP_VERB_POST,
        #     path=r"create/$",
        #     controller=EventosController,
        #     method="post",
        #     name=f"{name_base}_post",
        # ),
        Route(
            http_verb=HTTP_VERB_PUT,
            path="update/(?P<id>[0-9]+)/$",
            controller=EventosController,
            method="put",
            name=f"{name_base}_put",
        ),
        Route(
            http_verb=HTTP_VERB_DELETE,
            path="delete/(?P<id>[0-9]+)/$",
            controller=EventosController,
            method="delete",
            name=f"{name_base}_delete",
        ),
    ]
)
