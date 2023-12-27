from apps.domain.routing import Route, Router
from apps.domain.constants import (
    HTTP_VERB_GET,
    HTTP_VERB_POST,
    HTTP_VERB_DELETE,
    HTTP_VERB_PUT,
)
from apps.interfaces.controllers.base_controller import BaseController

router = Router()

name_base = "user"

router.register(
    [
        Route(
            http_verb=HTTP_VERB_GET,
            path=r"(?P<all>)$",
            controller=BaseController,
            method="get",
            name=f"{name_base}_get",
        ),
        Route(
            http_verb=HTTP_VERB_POST,
            path=r"create/$",
            controller=BaseController,
            method="post",
            name=f"{name_base}_post",
        ),
        Route(
            http_verb=HTTP_VERB_PUT,
            path="update/(?P<id>[0-9]+)/$",
            controller=BaseController,
            method="put",
            name=f"{name_base}_put",
        ),
    ]
)
