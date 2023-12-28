from src.domain.routing import Route, Router
from src.domain.constants import (
    HTTP_VERB_GET,
    HTTP_VERB_POST,
    HTTP_VERB_DELETE,
    HTTP_VERB_PUT,
)
from src.interfaces.controllers.encuestas.encuestas_controller import (
    EncuestasController,
)

router = Router()

name_base = "questions"

router.register(
    [
        Route(
            http_verb=HTTP_VERB_GET,
            path=r"$",
            controller=EncuestasController,
            method="get",
            name=f"{name_base}_get",
        ),
        Route(
            http_verb=HTTP_VERB_POST,
            path=r"create/$",
            controller=EncuestasController,
            method="post",
            name=f"{name_base}_post",
        ),
        Route(
            http_verb=HTTP_VERB_PUT,
            path="update/(?P<id>[0-9]+)/$",
            controller=EncuestasController,
            method="put",
            name=f"{name_base}_put",
        ),
        Route(
            http_verb=HTTP_VERB_DELETE,
            path="delete/$",
            controller=EncuestasController,
            method="delete",
            name=f"{name_base}_delete",
        ),
        Route(
            http_verb=HTTP_VERB_POST,
            path="responses/$",
            controller=EncuestasController,
            method="question_response",
            name=f"{name_base}_question_response",
        ),
    ]
)
