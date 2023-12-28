from django.urls import path
from django.conf.urls import include
from src.application.encuestas.api.views.questions.router import Router
from src.application.encuestas.api.views.questions.view import QuestionsViewSet

router = Router()
router.register("", viewset=QuestionsViewSet, basename="questions")
urlpatterns = [path("", include(router.urls))]
