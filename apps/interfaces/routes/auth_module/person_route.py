from apps.domain.routing import Route, Router
from apps.domain.constants import (
    HTTP_VERB_GET,
    HTTP_VERB_POST,
    HTTP_VERB_DELETE,
    HTTP_VERB_PUT,
)
from apps.interfaces.controllers.base_controller import BaseController

router = Router()

router.register(
    [
        Route(
            http_verb=HTTP_VERB_GET,
            path=r"$",
            controller=BaseController,
            method="get",
            name="person_get",
        ),
        Route(
            http_verb=HTTP_VERB_POST,
            path=r"create/$",
            controller=BaseController,
            method="post",
            name="person_post",
        ),
        Route(
            http_verb=HTTP_VERB_PUT,
            path="update/(?P<id>[0-9]+)/$",
            controller=BaseController,
            method="put",
            name="person_put",
        ),
        Route(
            http_verb=HTTP_VERB_DELETE,
            path=r"delete/$",
            controller=BaseController,
            method="delete",
            name="person_delete",
        ),
    ]
)
