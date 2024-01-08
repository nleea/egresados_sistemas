"""centro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from django.core.cache import cache
from django.http import HttpResponse
import debug_toolbar

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),  # type: ignore
    public=True,
    permission_classes=[permissions.AllowAny],
)


def clear_cache(request):
    cache.clear()
    return HttpResponse("Clear Cache", content_type="application/json", status=200)


app_name = "root"

PATH_APP = "src.application"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(f"{PATH_APP}.auth_module.api.urls")),
    path("advertisements/", include(f"{PATH_APP}.classified_advertisements.api.urls")),
    path("eventos/", include(f"{PATH_APP}.eventos.api.urls")),
    re_path("poll/", include(f"{PATH_APP}.encuestas.api.urls")),
    path("pqrs/", include(f"{PATH_APP}.pqrs.api.urls")),
    path("reportes/", include(f"{PATH_APP}.reportes.api.urls")),
    path("clear/cache", clear_cache, name="clear-cache"),
    re_path(
        r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        path(r"^__debug__/", include(debug_toolbar.urls)),
    ]