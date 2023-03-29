from django.urls import path, include

urlpatterns = [
    path('auth/', include('apps.auth_module.api.view.auth.urls')),
    path('users/', include('apps.auth_module.api.view.users.urls')),
    path('roles/', include('apps.auth_module.api.view.roles.urls')),
    path('resources/', include('apps.auth_module.api.view.resources.urls')),
    path('persons/', include('apps.auth_module.api.view.persons.urls')),
    path('genders/', include('apps.auth_module.api.view.genders.urls')),
    path('documents/', include('apps.auth_module.api.view.documents.urls')),
    path('security/',include('apps.auth_module.api.view.security.urls'))
]
