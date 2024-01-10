from src.domain.routing import Route, Router
from src.domain.constants import (
    HTTP_VERB_GET,
    HTTP_VERB_POST,
    HTTP_VERB_DELETE,
    HTTP_VERB_PUT,
)
from src.interfaces.controllers.classified.classified_controller import (
    ClassifiedController,
)

router = Router()

name_base = "advertisement"

router.register(
    [
        Route(
            http_verb=HTTP_VERB_GET,
            path=r"(?P<all>)$",
            controller=ClassifiedController,
            method="get",
            name=f"{name_base}_get",
        ),
        Route(
            http_verb=HTTP_VERB_POST,
            path=r"create/$",
            controller=ClassifiedController,
            method="post",
            name=f"{name_base}_post",
        ),
        Route(
            http_verb=HTTP_VERB_PUT,
            path="update/(?P<id>[0-9]+)/$",
            controller=ClassifiedController,
            method="put",
            name=f"{name_base}_put",
        ),
        Route(
            http_verb=HTTP_VERB_DELETE,
            path=r"delete/?(?P<id>[0-9]+)?/$",
            controller=ClassifiedController,
            method="delete",
            name=f"{name_base}_delete",
        ),
        Route(
            http_verb=HTTP_VERB_GET,
            path="mine/$",
            controller=ClassifiedController,
            method="mine",
            name=f"{name_base}_mine",
        ),
        Route(
            http_verb=HTTP_VERB_POST,
            path=r"recomendar/$",
            controller=ClassifiedController,
            method="save_voto",
            name=f"{name_base}_voto",
        ),
        Route(
            http_verb=HTTP_VERB_GET,
            path="valorados/$",
            controller=ClassifiedController,
            method="most_view",
            name=f"{name_base}_view",
        ),
        Route(
            http_verb=HTTP_VERB_POST,
            path=r"(?P<id>[0-9]+)/change/state/$",
            controller=ClassifiedController,
            method="state_changes",
            name=f"{name_base}_changes",
        ),
        Route(
            http_verb=HTTP_VERB_POST,
            path=r"query/$",
            controller=ClassifiedController,
            method="query",
            name=f"{name_base}_query",
        ),
    ]
)
