from ..modules import path


from django.conf.urls import include
from django.urls import path


from apps.auth_module.api.view.documents.routes import DocumentRouter
from apps.auth_module.api.view.documents.views import MessageViewSet

router = DocumentRouter()
router.register("", viewset=MessageViewSet, basename="documents")
urlpatterns = [path("", include(router.urls))]

