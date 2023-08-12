# resources = [
#   {
#     "path": "/admin/",
#     "method": "GET",
#     "id_padre": 0,
#     "icono": "pi pi-home",
#     "link": "/admin/",
#     "titulo": "Admin",
#     "items": [
#       {
#         "path": "/admin/roles-recursos/",
#         "method": "GET",
#         "icono": "pi pi-home",
#         "link": "/admin/roles-recursos/",
#         "titulo": "Roles Y Recursos",
#         "items": [
#           {
#             "path": "/admin/roles-recursos/ver-crear/",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/admin/roles-recursos/ver-editar/",
#             "titulo": "Ver Editar"
#           },
#           {
#             "path": "/admin/roles-recursos/ver/",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/admin/roles-recursos/crear/",
#             "titulo": "Crear"
#           }
#         ]
#       },
#       {
#         "path": "/admin/roles/",
#         "method": "GET",
#         "icono": "pi pi-user-minus",
#         "link": "/admin/roles/",
#         "titulo": "Roles",
#         "items": [
#           {
#             "path": "/admin/roles/ver/",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/admin/roles/ver/",
#             "titulo": "Ver"
#           }
#         ]
#       }
#     ]
#   },
#   {
#     "path": "/persona/",
#     "id_padre": 0,
#     "method": "GET",
#     "icono": "pi pi-user",
#     "link": "/persona/",
#     "titulo": "Persona",
#     "items": [
#       {
#         "path": "/persona/datos-personales/",
#         "method": "GET",
#         "icono": "icon",
#         "link": "/persona/datos-personales/",
#         "titulo": "Datos Personales",
#         "items": [
#           {
#             "path": "/persona/datos-personales/ver/",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/persona/datos-personales/ver/",
#             "titulo": "Ver"
#           },
#           {
#             "path": "/persona/datos-personales/crear/",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/persona/datos-personales/crear/",
#             "titulo": "Crear"
#           },
#           {
#             "path": "/persona/datos-personales/editar/",
#             "method": "PUT",
#             "icono": "icon",
#             "link": "/persona/datos-personales/editar/",
#             "titulo": "Editar"
#           },
#           {
#             "path": "/persona/datos-personales/eliminar",
#             "method": "DELETE",
#             "icono": "icon",
#             "link": "/persona/datos-personales/eliminar",
#             "titulo": "Eliminar"
#           }
#         ]
#       }
#     ]
#   },
#   {
#     "path": "/encuestas/",
#     "id_padre": 0,
#     "method": "GET",
#     "icono": "pi pi-book",
#     "link": "/encuestas/",
#     "titulo": "Encuestas",
#     "items": [
#       {
#         "path": "/encuestas/preguntas/",
#         "method": "GET",
#         "icono": "icon",
#         "link": "/encuestas/preguntas/",
#         "titulo": "Preguntas",
#         "items": [
#           {
#             "path": "/encuestas/preguntas/crear/",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/encuestas/preguntas/crear/",
#             "titulo": "Crear"
#           },
#           {
#             "path": "/encuestas/preguntas/editar/",
#             "method": "PUT",
#             "icono": "icon",
#             "link": "/encuestas/preguntas/editar/",
#             "titulo": "Editar"
#           },
#           {
#             "path": "/encuestas/preguntas/eliminar",
#             "method": "DELETE",
#             "icono": "icon",
#             "link": "/encuestas/preguntas/eliminar",
#             "titulo": "Eliminar"
#           },
#           {
#             "path": "/encuestas/preguntas/ver/",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/encuestas/preguntas/ver/",
#             "titulo": "Ver"
#           }
#         ]
#       },
#       {
#         "path": "/encuestas/momentos/",
#         "method": "GET",
#         "icono": "icon",
#         "link": "/encuestas/momentos/",
#         "titulo": "Momentos",
#         "items": [
#           {
#             "path": "/encuestas/momentos/crear/",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/encuestas/momentos/crear/",
#             "titulo": "Crear"
#           },
#           {
#             "path": "/encuestas/momentos/editar/",
#             "method": "PUT",
#             "icono": "icon",
#             "link": "/encuestas/momentos/editar/",
#             "titulo": "Editar"
#           },
#           {
#             "path": "/encuestas/momentos/eliminar",
#             "method": "DELETE",
#             "icono": "icon",
#             "link": "/encuestas/momentos/eliminar",
#             "titulo": "Eliminar"
#           },
#           {
#             "path": "/encuestas/momentos/ver/",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/encuestas/momentos/ver/",
#             "titulo": "Ver"
#           }
#         ]
#       }
#     ]
#   },
#   {
#     "path": "/pqrs/",
#     "id_padre": 0,
#     "method": "GET",
#     "icono": "pi pi-folder",
#     "link": "/pqrs/",
#     "titulo": "PQRS",
#     "items": [
#       {
#         "path": "/pqrs/solicitud/",
#         "method": "GET",
#         "icono": "icon",
#         "link": "/pqrs/solicitud/",
#         "titulo": "Solicitud",
#         "items": [
#           {
#             "path": "/pqrs/solicitud/ver/",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/pqrs/solicitud/ver/",
#             "titulo": "Ver"
#           },
#           {
#             "path": "/pqrs/solicitud/crear/",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/pqrs/solicitud/crear/",
#             "titulo": "Crear"
#           },
#           {
#             "path": "/pqrs/solicitud/editar/",
#             "method": "PUT",
#             "icono": "icon",
#             "link": "/pqrs/solicitud/editar/",
#             "titulo": "Editar"
#           },
#           {
#             "path": "/pqrs/solicitud/eliminar/",
#             "method": "DELETE",
#             "icono": "icon",
#             "link": "/pqrs/solicitud/eliminar/",
#             "titulo": "Eliminar"
#           }
#         ]
#       },
#       {
#         "path": "/pqrs/respuesta/",
#         "method": "GET",
#         "icono": "icon",
#         "link": "/pqrs/respuesta/",
#         "titulo": "Respuestas",
#         "items": [
#           {
#             "path": "/pqrs/respuesta/ver/",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/pqrs/respuesta/ver/",
#             "titulo": "Ver"
#           },
#           {
#             "path": "/pqrs/respuesta/crear/",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/pqrs/respuesta/crear/",
#             "titulo": "Crear"
#           },
#           {
#             "path": "/pqrs/respuesta/editar/",
#             "method": "PUT",
#             "icono": "icon",
#             "link": "/pqrs/respuesta/editar/",
#             "titulo": "Editar"
#           },
#           {
#             "path": "/pqrs/respuesta/eliminar",
#             "method": "DELETE",
#             "icono": "icon",
#             "link": "/pqrs/respuesta/eliminar",
#             "titulo": "Eliminar"
#           }
#         ]
#       },
#       {
#         "path": "/pqrs/tipo/",
#         "method": "GET",
#         "icono": "icon",
#         "link": "/pqrs/tipo/",
#         "titulo": "Tipo de solicitud",
#         "items": [
#           {
#             "path": "/pqrs/tipo/ver/",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/pqrs/tipo/ver/",
#             "titulo": "Ver"
#           },
#           {
#             "path": "/pqrs/tipo/crear/",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/pqrs/tipo/crear/",
#             "titulo": "Crear"
#           },
#           {
#             "path": "/pqrs/tipo/editar/",
#             "method": "PUT",
#             "icono": "icon",
#             "link": "/pqrs/tipo/editar/",
#             "titulo": "Editar"
#           },
#           {
#             "path": "/pqrs/tipo/eliminar/",
#             "method": "DELETE",
#             "icono": "icon",
#             "link": "/pqrs/tipo/eliminar/",
#             "titulo": "Eliminar"
#           }
#         ]
#       },
#       {
#         "path": "/pqrs/asignacion/",
#         "method": "GET",
#         "icono": "icon",
#         "link": "/pqrs/asignacion/",
#         "titulo": "Asignacion",
#         "items": [
#           {
#             "path": "/pqrs/asignacion/mis-solicitudes",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/pqrs/asignacion/mis-solicitudes",
#             "titulo": "Mis Solicitudes"
#           },
#           {
#             "path": "/pqrs/asignacion/solicitudes",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/pqrs/asignacion/solicitudes",
#             "titulo": "Solicitudes"
#           }
#         ]
#       }
#     ]
#   },
#   {
#     "path": "/clasificados/",
#     "id_padre": 0,
#     "method": "GET",
#     "icono": "pi pi-briefcase",
#     "link": "/clasificados/",
#     "titulo": "Clasificados",
#     "items": [
#       {
#         "path": "/clasificados/emprendimientos/",
#         "method": "GET",
#         "icono": "icon",
#         "link": "/clasificados/emprendimientos/",
#         "titulo": "Emprendimientos",
#         "items": [
#           {
#             "path": "/clasificados/emprendimientos/crear",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/clasificados/emprendimientos/crear",
#             "titulo": "Crear"
#           },
#           {
#             "path": "/clasificados/emprendimientos/ver",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/clasificados/emprendimientos/ver",
#             "titulo": "Ver"
#           },
#           {
#             "path": "/clasificados/emprendimientos/editar",
#             "method": "PUT",
#             "icono": "icon",
#             "link": "/clasificados/emprendimientos/editar",
#             "titulo": "Editar"
#           },
#           {
#             "path": "/clasificados/emprendimientos/eliminar",
#             "method": "DELETE",
#             "icono": "icon",
#             "link": "/clasificados/emprendimientos/eliminar",
#             "titulo": "Eliminar"
#           }
#         ]
#       },
#       {
#         "path": "/clasificados/categoria/",
#         "method": "GET",
#         "icono": "icon",
#         "link": "/clasificados/categoria/",
#         "titulo": "Categorias",
#         "items": [
#           {
#             "path": "/clasificados/categoria/crear",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/clasificados/categoria/crear",
#             "titulo": "Crear"
#           },
#           {
#             "path": "/clasificados/categoria/ver",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/clasificados/categoria/ver",
#             "titulo": "Ver"
#           },
#           {
#             "path": "/clasificados/categoria/editar",
#             "method": "PUT",
#             "icono": "icon",
#             "link": "/clasificados/categoria/editar",
#             "titulo": "Editar"
#           },
#           {
#             "path": "/clasificados/categoria/eliminar",
#             "method": "DELETE",
#             "icono": "icon",
#             "link": "/clasificados/categoria/eliminar",
#             "titulo": "Eliminar"
#           }
#         ]
#       },
#       {
#         "path": "/clasificados/sub-categoria/",
#         "method": "GET",
#         "icono": "icon",
#         "link": "/clasificados/sub-categoria/",
#         "titulo": "Sub Categoria",
#         "items": [
#           {
#             "path": "/clasificados/sub-categoria/crear",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/clasificados/sub-categoria/crear",
#             "titulo": "Crear"
#           },
#           {
#             "path": "/clasificados/sub-categoria/ver",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/clasificados/sub-categoria/ver",
#             "titulo": "Ver"
#           },
#           {
#             "path": "/clasificados/sub-categoria/editar",
#             "method": "PUT",
#             "icono": "icon",
#             "link": "/clasificados/sub-categoria/editar",
#             "titulo": "Editar"
#           },
#           {
#             "path": "/clasificados/sub-categoria/eliminar",
#             "method": "DELETE",
#             "icono": "icon",
#             "link": "/clasificados/sub-categoria/eliminar",
#             "titulo": "Eliminar"
#           }
#         ]
#       }
#     ]
#   },
#   {
#     "path": "/eventos/",
#     "id_padre": 0,
#     "method": "GET",
#     "icono": "pi pi-ticket",
#     "link": "/eventos/",
#     "titulo": "Eventos",
#     "items": [
#       {
#         "path": "/eventos/actividades/",
#         "method": "GET",
#         "icono": "icon",
#         "link": "/eventos/actividades/",
#         "titulo": "Actividades",
#         "items": [
#           {
#             "path": "/eventos/actividades/ver/",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/eventos/actividades/ver/",
#             "titulo": "Ver"
#           },
#           {
#             "path": "/eventos/actividades/crear/",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/eventos/actividades/crear/",
#             "titulo": "Crear"
#           },
#           {
#             "path": "/eventos/actividades/editar/",
#             "method": "PUT",
#             "icono": "icon",
#             "link": "/eventos/actividades/editar/",
#             "titulo": "Editar"
#           },
#           {
#             "path": "/eventos/actividades/eliminar",
#             "method": "DELETE",
#             "icono": "icon",
#             "link": "/eventos/actividades/eliminar",
#             "titulo": "Eliminar"
#           }
#         ]
#       },
#       {
#         "path": "/eventos/areas/",
#         "method": "GET",
#         "icono": "icon",
#         "link": "/eventos/areas/",
#         "titulo": "Areas",
#         "items": [
#           {
#             "path": "/eventos/areas/ver/",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/eventos/areas/ver/",
#             "titulo": "Ver"
#           },
#           {
#             "path": "/eventos/areas/crear/",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/eventos/areas/crear/",
#             "titulo": "Crear"
#           },
#           {
#             "path": "/eventos/areas/editar/",
#             "method": "PUT",
#             "icono": "icon",
#             "link": "/eventos/areas/editar/",
#             "titulo": "Editar"
#           },
#           {
#             "path": "/eventos/areas/eliminar",
#             "method": "DELETE",
#             "icono": "icon",
#             "link": "/eventos/areas/eliminar",
#             "titulo": "Eliminar"
#           }
#         ]
#       },
#       {
#         "path": "/eventos/subareas/",
#         "method": "GET",
#         "icono": "icon",
#         "link": "/eventos/subareas/",
#         "titulo": "Sub-areas",
#         "items": [
#           {
#             "path": "/eventos/subareas/ver/",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/eventos/subareas/ver/",
#             "titulo": "Ver"
#           },
#           {
#             "path": "/eventos/subareas/crear/",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/eventos/subareas/crear/",
#             "titulo": "Crear"
#           },
#           {
#             "path": "/eventos/subareas/editar/",
#             "method": "PUT",
#             "icono": "icon",
#             "link": "/eventos/subareas/editar/",
#             "titulo": "Editar"
#           },
#           {
#             "path": "/eventos/subareas/eliminar",
#             "method": "DELETE",
#             "icono": "icon",
#             "link": "/eventos/subareas/eliminar",
#             "titulo": "Eliminar"
#           }
#         ]
#       },
#       {
#         "path": "/eventos/tipo-actividad/",
#         "method": "GET",
#         "icono": "icon",
#         "link": "/eventos/tipo-actividad/",
#         "titulo": "Tipo Actividad",
#         "items": [
#           {
#             "path": "/eventos/tipo-actividad/ver/",
#             "method": "GET",
#             "icono": "icon",
#             "link": "/eventos/tipo-actividad/ver/",
#             "titulo": "Ver"
#           },
#           {
#             "path": "/eventos/tipo-actividad/crear/",
#             "method": "POST",
#             "icono": "icon",
#             "link": "/eventos/tipo-actividad/crear/",
#             "titulo": "Crear"
#           },
#           {
#             "path": "/eventos/tipo-actividad/editar/",
#             "method": "PUT",
#             "icono": "icon",
#             "link": "/eventos/tipo-actividad/editar/",
#             "titulo": "Editar"
#           },
#           {
#             "path": "/eventos/tipo-actividad/eliminar",
#             "method": "DELETE",
#             "icono": "icon",
#             "link": "/eventos/tipo-actividad/eliminar",
#             "titulo": "Eliminar"
#           }
#         ]
#       }
#     ]
#   }
# ]

# [
#     {
#         "id": 1,
#         "id_padre": 0,
#         "path": "/admin/",
#         "icono": "pi pi-home",
#         "link": "/admin/",
#         "titulo": "Admin"
#     },
#     {
#         "id": 2,
#         "id_padre": 1,
#         "path": "/admin/roles-recursos/",
#         "icono": "pi pi-home",
#         "link": "/admin/roles-recursos/",
#         "titulo": "Roles Y Recursos"
#     },
#     {
#         "id": 3,
#         "id_padre": 2,
#         "path": "/admin/roles-recursos/ver-crear/",
#         "icono": "icon",
#         "link": "/admin/roles-recursos/ver-editar/",
#         "titulo": "Ver Editar"
#     },
#     {
#         "id": 4,
#         "id_padre": 2,
#         "path": "/admin/roles-recursos/ver/",
#         "icono": "icon",
#         "link": "/admin/roles-recursos/crear/",
#         "titulo": "Crear"
#     },
#     {
#         "id": 5,
#         "id_padre": 1,
#         "path": "/admin/roles/",
#         "icono": "pi pi-user-minus",
#         "link": "/admin/roles/",
#         "titulo": "Roles"
#     },
#     {
#         "id": 6,
#         "id_padre": 5,
#         "path": "/admin/roles/ver/",
#         "icono": "icon",
#         "link": "/admin/roles/ver/",
#         "titulo": "Ver"
#     },
#     {
#         "id": 13,
#         "id_padre": 0,
#         "path": "/encuestas/",
#         "icono": "pi pi-book",
#         "link": "/encuestas/",
#         "titulo": "Encuestas"
#     },
#     {
#         "id": 14,
#         "id_padre": 13,
#         "path": "/encuestas/preguntas/",
#         "icono": "icon",
#         "link": "/encuestas/preguntas/",
#         "titulo": "Preguntas"
#     },
#     {
#         "id": 15,
#         "id_padre": 14,
#         "path": "/encuestas/preguntas/gestionar/",
#         "icono": "icon",
#         "link": "/encuestas/preguntas/gestionar/",
#         "titulo": "Gestionar"
#     },
#     {
#         "id": 16,
#         "id_padre": 13,
#         "path": "/encuestas/momentos/",
#         "icono": "icon",
#         "link": "/encuestas/momentos/",
#         "titulo": "Momentos"
#     },
#     {
#         "id": 17,
#         "id_padre": 16,
#         "path": "/encuestas/momentos/gestionar/",
#         "icono": "icon",
#         "link": "/encuestas/momentos/gestionar/",
#         "titulo": "Gestionar"
#     },
#     {
#         "id": 18,
#         "id_padre": 0,
#         "path": "/pqrs/",
#         "icono": "pi pi-folder",
#         "link": "/pqrs/",
#         "titulo": "PQRS"
#     },
#     {
#         "id": 19,
#         "id_padre": 18,
#         "path": "/pqrs/solicitud/",
#         "icono": "icon",
#         "link": "/pqrs/solicitud/",
#         "titulo": "Solicitudes"
#     },
#     {
#         "id": 20,
#         "id_padre": 19,
#         "path": "/pqrs/solicitud/ver/",
#         "icono": "icon",
#         "link": "/pqrs/solicitud/ver/",
#         "titulo": "Ver"
#     },
#     {
#         "id": 21,
#         "id_padre": 19,
#         "path": "/pqrs/solicitud/crear/",
#         "icono": "icon",
#         "link": "/pqrs/solicitud/crear/",
#         "titulo": "Crear"
#     },
#     {
#         "id": 22,
#         "id_padre": 19,
#         "path": "/pqrs/solicitud/editar/",
#         "icono": "icon",
#         "link": "/pqrs/solicitud/editar/",
#         "titulo": "Editar"
#     },
#     {
#         "id": 23,
#         "id_padre": 19,
#         "path": "/pqrs/solicitud/eliminar/",
#         "icono": "icon",
#         "link": "/pqrs/solicitud/eliminar/",
#         "titulo": "Eliminar"
#     },
#     {
#         "id": 24,
#         "id_padre": 18,
#         "path": "/pqrs/tipo/",
#         "icono": "icon",
#         "link": "/pqrs/tipo/",
#         "titulo": "Tipo de solicitud"
#     },
#     {
#         "id": 25,
#         "id_padre": 24,
#         "path": "/pqrs/tipo/gestionar/",
#         "icono": "icon",
#         "link": "/pqrs/tipo/gestionar/",
#         "titulo": "Gestionar"
#     },
#     {
#         "id": 26,
#         "id_padre": 18,
#         "path": "/pqrs/asignacion/",
#         "icono": "icon",
#         "link": "/pqrs/asignacion/",
#         "titulo": "Asignacion"
#     },
#     {
#         "id": 27,
#         "id_padre": 26,
#         "path": "/pqrs/asignacion/mis-solicitudes/",
#         "icono": "icon",
#         "link": "/pqrs/asignacion/mis-solicitudes/",
#         "titulo": "Mis Solicitudes"
#     },
#     {
#         "id": 28,
#         "id_padre": 26,
#         "path": "/pqrs/asignacion/solicitudes/",
#         "icono": "icon",
#         "link": "/pqrs/asignacion/solicitudes/",
#         "titulo": "Solicitudes"
#     },
#     {
#         "id": 29,
#         "id_padre": 0,
#         "path": "/clasificados/",
#         "icono": "pi pi-briefcase",
#         "link": "/clasificados/",
#         "titulo": "Clasificados"
#     },
#     {
#         "id": 30,
#         "id_padre": 29,
#         "path": "/clasificados/emprendimientos/",
#         "icono": "icon",
#         "link": "/clasificados/emprendimientos/",
#         "titulo": "Emprendimientos"
#     },
#     {
#         "id": 31,
#         "id_padre": 30,
#         "path": "/clasificados/emprendimientos/crear",
#         "icono": "icon",
#         "link": "/clasificados/emprendimientos/crear",
#         "titulo": "Crear"
#     },
#     {
#         "id": 32,
#         "id_padre": 30,
#         "path": "/clasificados/emprendimientos/ver",
#         "icono": "icon",
#         "link": "/clasificados/emprendimientos/ver",
#         "titulo": "Mostrar"
#     },
#     {
#         "id": 33,
#         "id_padre": 30,
#         "path": "/clasificados/emprendimientos/editar",
#         "icono": "icon",
#         "link": "/clasificados/emprendimientos/editar",
#         "titulo": "Editar"
#     },
#     {
#         "id": 34,
#         "id_padre": 30,
#         "path": "/clasificados/emprendimientos/eliminar",
#         "icono": "icon",
#         "link": "/clasificados/emprendimientos/eliminar",
#         "titulo": "Eliminar"
#     },
#     {
#         "id": 35,
#         "id_padre": 29,
#         "path": "/clasificados/categoria/",
#         "icono": "icon",
#         "link": "/clasificados/categoria/",
#         "titulo": "Categorias"
#     },
#     {
#         "id": 36,
#         "id_padre": 35,
#         "path": "/clasificados/categoria/gestionar",
#         "icono": "icon",
#         "link": "/clasificados/categoria/gestionar",
#         "titulo": "Gestionar"
#     },
#     {
#         "id": 37,
#         "id_padre": 29,
#         "path": "/clasificados/sub-categoria/",
#         "icono": "icon",
#         "link": "/clasificados/sub-categoria/",
#         "titulo": "Sub Categoria"
#     },
#     {
#         "id": 38,
#         "id_padre": 37,
#         "path": "/clasificados/sub-categoria/gestionar",
#         "icono": "icon",
#         "link": "/clasificados/sub-categoria/gestionar",
#         "titulo": "Gestionar"
#     },
#     {
#         "id": 39,
#         "id_padre": 0,
#         "path": "/eventos/",
#         "icono": "pi pi-ticket",
#         "link": "/eventos/",
#         "titulo": "Eventos"
#     },
#     {
#         "id": 40,
#         "id_padre": 39,
#         "path": "/eventos/actividades/",
#         "icono": "icon",
#         "link": "/eventos/actividades/",
#         "titulo": "Actividades"
#     },
#     {
#         "id": 41,
#         "id_padre": 40,
#         "path": "/eventos/actividades/ver/",
#         "icono": "icon",
#         "link": "/eventos/actividades/ver/",
#         "titulo": "Ver"
#     },
#     {
#         "id": 42,
#         "id_padre": 40,
#         "path": "/eventos/actividades/crear/",
#         "icono": "icon",
#         "link": "/eventos/actividades/crear/",
#         "titulo": "Crear"
#     },
#     {
#         "id": 43,
#         "id_padre": 40,
#         "path": "/eventos/actividades/editar/",
#         "icono": "icon",
#         "link": "/eventos/actividades/editar/",
#         "titulo": "Editar"
#     },
#     {
#         "id": 44,
#         "id_padre": 40,
#         "path": "/eventos/actividades/eliminar",
#         "icono": "icon",
#         "link": "/eventos/actividades/eliminar",
#         "titulo": "Eliminar"
#     },
#     {
#         "id": 45,
#         "id_padre": 39,
#         "path": "/eventos/areas/",
#         "icono": "icon",
#         "link": "/eventos/areas/",
#         "titulo": "Areas"
#     },
#     {
#         "id": 46,
#         "id_padre": 45,
#         "path": "/eventos/areas/gestionar/",
#         "icono": "icon",
#         "link": "/eventos/areas/gestionar/",
#         "titulo": "Gestionar"
#     },
#     {
#         "id": 47,
#         "id_padre": 39,
#         "path": "/eventos/subareas/",
#         "icono": "icon",
#         "link": "/eventos/subareas/",
#         "titulo": "Sub-areas"
#     },
#     {
#         "id": 48,
#         "id_padre": 47,
#         "path": "/eventos/subareas/gestionar/",
#         "icono": "icon",
#         "link": "/eventos/subareas/gestionar/",
#         "titulo": "Gestionar"
#     },
#     {
#         "id": 49,
#         "id_padre": 39,
#         "path": "/eventos/tipo-actividad/",
#         "icono": "icon",
#         "link": "/eventos/tipo-actividad/",
#         "titulo": "Tipo Actividad"
#     },
#     {
#         "id": 50,
#         "id_padre": 49,
#         "path": "/eventos/tipo-actividad/gestionar/",
#         "icono": "icon",
#         "link": "/eventos/tipo-actividad/gestionar/",
#         "titulo": "Gestionar"
#     },
#     {
#         "id": 51,
#         "id_padre": 39,
#         "path": "/eventos/progrma/",
#         "icono": "icon",
#         "link": "/eventos/programa/",
#         "titulo": "Programas"
#     },
#     {
#         "id": 52,
#         "id_padre": 51,
#         "path": "/eventos/programa/gestionar/",
#         "icono": "icon",
#         "link": "/eventos/programa/gestionar/",
#         "titulo": "Gestionar"
#     },
#     {
#         "id": 53,
#         "id_padre": 39,
#         "path": "/eventos/sede/",
#         "icono": "icon",
#         "link": "/eventos/sede/",
#         "titulo": "Sede"
#     },
#     {
#         "id": 54,
#         "id_padre": 53,
#         "path": "/eventos/sede/gestionar/",
#         "icono": "icon",
#         "link": "/eventos/sede/gestionar/",
#         "titulo": "Sede"
#     },
#     {
#         "id": 55,
#         "id_padre": 39,
#         "path": "/eventos/facultad/",
#         "icono": "icon",
#         "link": "/eventos/facultad/",
#         "titulo": "Facultad"
#     },
#     {
#         "id": 56,
#         "id_padre": 55,
#         "path": "/eventos/faculta/gestionar/",
#         "icono": "icon",
#         "link": "/eventos/faculta/gestionar/",
#         "titulo": "Gestionar"
#     },
#     {
#         "id": 57,
#         "id_padre": 39,
#         "path": "/eventos/asistencias/",
#         "icono": "",
#         "link": "/eventos/asistencias/",
#         "titulo": "Asistencias"
#     },
#     {
#         "id": 58,
#         "id_padre": 57,
#         "path": "/eventos/asistencias/llenar-asistencias/",
#         "icono": "icon",
#         "link": "/eventos/asistencias/llenar-asistencias/",
#         "titulo": "Llenar"
#     },
#     {
#         "id": 59,
#         "id_padre": 57,
#         "path": "/eventos/asistencias/ver-asistencias/",
#         "icono": "icon",
#         "link": "/eventos/asistencias/ver-asistencias/",
#         "titulo": "Ver"
#     },
#     {
#         "id": 67,
#         "id_padre": 0,
#         "path": "/inicio/",
#         "icono": "pi pi-home",
#         "link": "/inicio/",
#         "titulo": "Inicio"
#     },
#     {
#         "id": 68,
#         "id_padre": 67,
#         "path": "/inicio/datos-personales/",
#         "icono": "icon",
#         "link": "/inicio/datos-personales/",
#         "titulo": "Datos Personales"
#     },
#     {
#         "id": 69,
#         "id_padre": 68,
#         "path": "/inicio/datos-personales/actualizar-datos/",
#         "icono": "icon",
#         "link": "/inicio/datos-personales/actualizar-datos/",
#         "titulo": "Actualizar Datos"
#     },
#     {
#         "id": 66,
#         "id_padre": 40,
#         "path": "/eventos/actividades/mis-actividades/",
#         "icono": "icon",
#         "link": "/eventos/actividades/mis-actividades/",
#         "titulo": "Mis Actividades"
#     },
#     {
#         "id": 63,
#         "id_padre": 30,
#         "path": "/clasificados/emprendimientos/detalles/",
#         "icono": "icon",
#         "link": "/clasificados/emprendimientos/detalles/",
#         "titulo": "Ver"
#     },
#     {
#         "id": 64,
#         "id_padre": 30,
#         "path": "/clasificados/emprendimientos/mis-emprendimientos/",
#         "icono": "icon",
#         "link": "/clasificados/emprendimientos/mis-emprendimientos/",
#         "titulo": "Mis Emprendimientos"
#     },
#     {
#         "id": 65,
#         "id_padre": 19,
#         "path": "/pqrs/solicitud/mis-solicitudes/",
#         "icono": "icon",
#         "link": "/pqrs/solicitud/mis-solicitudes/",
#         "titulo": "Mis Solicitudes"
#     },
#     {
#         "id": 70,
#         "id_padre": 13,
#         "path": "/encuestas/mis-encuestas/",
#         "icono": "icon",
#         "link": "/encuestas/mis-encuestas/",
#         "titulo": "Mis Encuestas"
#     },
#     {
#         "id": 71,
#         "id_padre": 70,
#         "path": "/encuestas/mis-encuestas/llenar-encuestas/",
#         "icono": "icon",
#         "link": "/encuestas/mis-encuestas/llenar-encuestas/",
#         "titulo": "LLenar encuestas"
#     },
#     {
#         "id": 72,
#         "id_padre": 29,
#         "path": "/clasificados/capacitacion/",
#         "icono": "icon",
#         "link": "/clasificados/capacitacion/",
#         "titulo": "Capacitaciones"
#     },
#     {
#         "id": 73,
#         "id_padre": 72,
#         "path": "/clasificados/capacitacion/gestionar/",
#         "icono": "icon",
#         "link": "/clasificados/capacitacion/gestionar/",
#         "titulo": "Gestionar"
#     }
# ]
resources = [
    {
        "id_padre": 0,
        "path": "/inicio/",
        "icono": "pi pi-home",
        "method": "GET",
        "link": "/inicio/",
        "titulo": "Inicio",
        "items": [
            {
                "path": "/inicio/datos-personales/",
                "icono": "icon",
                "link": "/inicio/datos-personales/",
                "method": "GET",
                "titulo": "Datos Personales",
                "items": [
                    {
                        "path": "/inicio/datos-personales/actualizar-datos/",
                        "icono": "icon",
                        "method": "POST",
                        "link": "/inicio/datos-personales/actualizar-datos/",
                        "titulo": "Actualizar Datos",
                    },
                ],
            },
        ],
    },
    {
        "path": "/admin/",
        "method": "GET",
        "id_padre": 0,
        "icono": "pi pi-home",
        "link": "/admin/",
        "titulo": "Admin",
        "items": [
            {
                "path": "/admin/roles-recursos/",
                "method": "GET",
                "icono": "pi pi-home",
                "link": "/admin/roles-recursos/",
                "titulo": "Roles Y Recursos",
                "items": [
                    {
                        "path": "/admin/roles-recursos/ver-crear/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/admin/roles-recursos/ver-editar/",
                        "titulo": "Ver Editar",
                    },
                    {
                        "path": "/admin/roles-recursos/ver/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/admin/roles-recursos/crear/",
                        "titulo": "Crear",
                    },
                ],
            },
            {
                "path": "/admin/roles/",
                "method": "GET",
                "icono": "pi pi-user-minus",
                "link": "/admin/roles/",
                "titulo": "Roles",
                "items": [
                    {
                        "path": "/admin/roles/ver/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/admin/roles/ver/",
                        "titulo": "Ver",
                    }
                ],
            },
        ],
    },
    # {
    #     "path": "/persona/",
    #     "id_padre": 0,
    #     "method": "GET",
    #     "icono": "pi pi-user",
    #     "link": "/persona/",
    #     "titulo": "Persona",
    #     "items": [
    #         {
    #             "path": "/persona/datos-personales/",
    #             "method": "GET",
    #             "icono": "icon",
    #             "link": "/persona/datos-personales/",
    #             "titulo": "Datos Personales",
    #             "items": [
    #                 {
    #                     "path": "/persona/datos-personales/ver/",
    #                     "method": "GET",
    #                     "icono": "icon",
    #                     "link": "/persona/datos-personales/ver/",
    #                     "titulo": "Ver",
    #                 },
    #                 {
    #                     "path": "/persona/datos-personales/crear/",
    #                     "method": "POST",
    #                     "icono": "icon",
    #                     "link": "/persona/datos-personales/crear/",
    #                     "titulo": "Crear",
    #                 },
    #                 {
    #                     "path": "/persona/datos-personales/editar/",
    #                     "method": "PUT",
    #                     "icono": "icon",
    #                     "link": "/persona/datos-personales/editar/",
    #                     "titulo": "Editar",
    #                 },
    #                 {
    #                     "path": "/persona/datos-personales/eliminar",
    #                     "method": "DELETE",
    #                     "icono": "icon",
    #                     "link": "/persona/datos-personales/eliminar",
    #                     "titulo": "Eliminar",
    #                 },
    #             ],
    #         }
    #     ],
    # },
    {
        "path": "/encuestas/",
        "id_padre": 0,
        "method": "GET",
        "icono": "pi pi-book",
        "link": "/encuestas/",
        "titulo": "Encuestas",
        "items": [
            {
                "path": "/encuestas/preguntas/",
                "method": "GET",
                "icono": "icon",
                "link": "/encuestas/preguntas/",
                "titulo": "Preguntas",
                "items": [
                    {
                        "path": "/encuestas/preguntas/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/encuestas/preguntas/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/encuestas/momentos/",
                "method": "GET",
                "icono": "icon",
                "link": "/encuestas/momentos/",
                "titulo": "Momentos",
                "items": [
                    {
                        "path": "/encuestas/momentos/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/encuestas/momentos/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
        ],
    },
    {
        "path": "/pqrs/",
        "id_padre": 0,
        "method": "GET",
        "icono": "pi pi-folder",
        "link": "/pqrs/",
        "titulo": "PQRS",
        "items": [
            {
                "path": "/pqrs/solicitud/",
                "method": "GET",
                "icono": "icon",
                "link": "/pqrs/solicitud/",
                "titulo": "Solicitud",
                "items": [
                    {
                        "path": "/pqrs/solicitud/ver/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/ver/",
                        "titulo": "Ver",
                    },
                    {
                        "path": "/pqrs/solicitud/crear/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/crear/",
                        "titulo": "Crear",
                    },
                    {
                        "path": "/pqrs/solicitud/editar/",
                        "method": "PUT",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/editar/",
                        "titulo": "Editar",
                    },
                    {
                        "path": "/pqrs/solicitud/eliminar/",
                        "method": "DELETE",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/eliminar/",
                        "titulo": "Eliminar",
                    },
                ],
            },
            {
                "path": "/pqrs/tipo/",
                "method": "GET",
                "icono": "icon",
                "link": "/pqrs/tipo/",
                "titulo": "Tipo de solicitud",
                "items": [
                    {
                        "path": "/pqrs/tipo/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/pqrs/tipo/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/pqrs/asignacion/",
                "method": "GET",
                "icono": "icon",
                "link": "/pqrs/asignacion/",
                "titulo": "Asignacion",
                "items": [
                    {
                        "path": "/pqrs/asignacion/mis-solicitudes",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/pqrs/asignacion/mis-solicitudes",
                        "titulo": "Mis Solicitudes",
                    },
                    {
                        "path": "/pqrs/asignacion/solicitudes",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/pqrs/asignacion/solicitudes",
                        "titulo": "Solicitudes",
                    },
                ],
            },
        ],
    },
    {
        "path": "/clasificados/",
        "id_padre": 0,
        "method": "GET",
        "icono": "pi pi-briefcase",
        "link": "/clasificados/",
        "titulo": "Clasificados",
        "items": [
            {
                "path": "/clasificados/emprendimientos/",
                "method": "GET",
                "icono": "icon",
                "link": "/clasificados/emprendimientos/",
                "titulo": "Emprendimientos",
                "items": [
                    {
                        "path": "/clasificados/emprendimientos/crear",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/crear",
                        "titulo": "Crear",
                    },
                    {
                        "path": "/clasificados/emprendimientos/ver",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/ver",
                        "titulo": "Ver",
                    },
                    {
                        "path": "/clasificados/emprendimientos/editar",
                        "method": "PUT",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/editar",
                        "titulo": "Editar",
                    },
                    {
                        "path": "/clasificados/emprendimientos/eliminar",
                        "method": "DELETE",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/eliminar",
                        "titulo": "Eliminar",
                    },
                ],
            },
            {
                "path": "/clasificados/categoria/",
                "method": "GET",
                "icono": "icon",
                "link": "/clasificados/categoria/",
                "titulo": "Categorias",
                "items": [
                    {
                        "path": "/clasificados/categoria/gestionar",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/clasificados/categoria/gestionar",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/clasificados/sub-categoria/",
                "method": "GET",
                "icono": "icon",
                "link": "/clasificados/sub-categoria/",
                "titulo": "Sub Categoria",
                "items": [
                    {
                        "path": "/clasificados/sub-categoria/gestionar",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/clasificados/sub-categoria/gestionar",
                        "titulo": "Gestionar",
                    }
                ],
            },
        ],
    },
    {
        "path": "/eventos/",
        "id_padre": 0,
        "method": "GET",
        "icono": "pi pi-ticket",
        "link": "/eventos/",
        "titulo": "Eventos",
        "items": [
            {
                "path": "/eventos/actividades/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/actividades/",
                "titulo": "Actividades",
                "items": [
                    {
                        "path": "/eventos/actividades/ver/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/actividades/ver/",
                        "titulo": "Ver",
                    },
                    {
                        "path": "/eventos/actividades/crear/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/eventos/actividades/crear/",
                        "titulo": "Crear",
                    },
                    {
                        "path": "/eventos/actividades/editar/",
                        "method": "PUT",
                        "icono": "icon",
                        "link": "/eventos/actividades/editar/",
                        "titulo": "Editar",
                    },
                    {
                        "path": "/eventos/actividades/eliminar",
                        "method": "DELETE",
                        "icono": "icon",
                        "link": "/eventos/actividades/eliminar",
                        "titulo": "Eliminar",
                    },
                ],
            },
            {
                "path": "/eventos/areas/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/areas/",
                "titulo": "Areas",
                "items": [
                    {
                        "path": "/eventos/areas/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/areas/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/eventos/subareas/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/subareas/",
                "titulo": "Sub-areas",
                "items": [
                    {
                        "path": "/eventos/subareas/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/subareas/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/eventos/tipo-actividad/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/tipo-actividad/",
                "titulo": "Tipo Actividad",
                "items": [
                    {
                        "path": "/eventos/tipo-actividad/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/tipo-actividad/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/eventos/progrma/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/programa/",
                "titulo": "Programas",
                "items": [
                    {
                        "path": "/eventos/programa/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/programa/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
            {
                "path": "/eventos/sede/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/sede/",
                "titulo": "Sede",
                "items": [
                    {
                        "path": "/eventos/sede/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/sede/gestionar/",
                        "titulo": "Sede",
                    }
                ],
            },
            {
                "path": "/eventos/facultad/",
                "method": "GET",
                "icono": "icon",
                "link": "/eventos/facultad/",
                "titulo": "Facultad",
                "items": [
                    {
                        "path": "/eventos/faculta/gestionar/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/eventos/faculta/gestionar/",
                        "titulo": "Gestionar",
                    }
                ],
            },
        ],
    },
]

resources_egresado = [
    {
        "id_padre": 0,
        "path": "/inicio/",
        "icono": "pi pi-home",
        "method": "GET",
        "link": "/inicio/",
        "titulo": "Inicio",
        "items": [
            {
                "path": "/inicio/datos-personales/",
                "icono": "icon",
                "link": "/inicio/datos-personales/",
                "method": "GET",
                "titulo": "Datos Personales",
                "items": [
                    {
                        "path": "/inicio/datos-personales/actualizar-datos/",
                        "icono": "icon",
                        "method": "POST",
                        "link": "/inicio/datos-personales/actualizar-datos/",
                        "titulo": "Actualizar Datos",
                    },
                ],
            },
        ],
    },
    {
        "path": "/encuestas/",
        "id_padre": 0,
        "method": "GET",
        "icono": "pi pi-book",
        "link": "/encuestas/",
        "titulo": "Encuestas",
        "items": [
            {
                "path": "/encuestas/mis-encuestas/",
                "icono": "icon",
                "method": "GET",
                "link": "/encuestas/mis-encuestas/",
                "titulo": "Mis Encuestas",
                "items": [
                    {
                        "path": "/encuestas/mis-encuestas/llenar-encuestas/",
                        "icono": "icon",
                        "method": "GET",
                        "link": "/encuestas/mis-encuestas/llenar-encuestas/",
                        "titulo": "LLenar encuestas",
                    },
                ],
            },
        ],
    },
    {
        "path": "/pqrs/",
        "id_padre": 0,
        "method": "GET",
        "icono": "pi pi-folder",
        "link": "/pqrs/",
        "titulo": "PQRS",
        "items": [
            {
                "path": "/pqrs/solicitud/",
                "icono": "icon",
                "link": "/pqrs/solicitud/",
                "titulo": "Solicitudes",
                "items": [
                    {
                        "path": "/pqrs/solicitud/crear/",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/crear/",
                        "titulo": "Crear",
                    },
                    {
                        "path": "/pqrs/solicitud/mis-solicitudes/",
                        "icono": "icon",
                        "link": "/pqrs/solicitud/mis-solicitudes/",
                        "titulo": "Mis Solicitudes",
                    },
                ],
            },
        ],
    },
    {
        "path": "/clasificados/",
        "id_padre": 0,
        "method": "GET",
        "icono": "pi pi-briefcase",
        "link": "/clasificados/",
        "titulo": "Clasificados",
        "items": [
            {
                "path": "/clasificados/emprendimientos/",
                "icono": "icon",
                "method": "GET",
                "link": "/clasificados/emprendimientos/",
                "titulo": "Emprendimientos",
                "items": [
                    {
                        "path": "/clasificados/emprendimientos/ver",
                        "icono": "icon",
                        "method": "GET",
                        "link": "/clasificados/emprendimientos/ver",
                        "titulo": "Mostrar",
                    },
                    {
                        "path": "/clasificados/emprendimientos/crear",
                        "icono": "icon",
                        "method": "GET",
                        "link": "/clasificados/emprendimientos/crear",
                        "titulo": "Crear",
                    },
                    {
                        "path": "/clasificados/emprendimientos/mis-emprendimientos/",
                        "icono": "icon",
                        "link": "/clasificados/emprendimientos/mis-emprendimientos/",
                        "titulo": "Mis Emprendimientos",
                    },
                ],
            },
        ],
    },
    {
        "path": "/eventos/",
        "id_padre": 0,
        "method": "GET",
        "icono": "pi pi-ticket",
        "link": "/eventos/",
        "titulo": "Eventos",
        "items": [
            {
                "path": "/eventos/actividades/",
                "icono": "icon",
                "method": "GET",
                "link": "/eventos/actividades/",
                "titulo": "Actividades",
                "items": [
                    {
                        "path": "/eventos/actividades/mis-actividades/",
                        "icono": "icon",
                        "method": "GET",
                        "link": "/eventos/actividades/mis-actividades/",
                        "titulo": "Mis Actividades",
                    },
                ],
            },
        ],
    },
]

# [
#     {
#         "id": 54,
#         "id_padre": 0,
#         "path": "/inicio/",
#         "icono": "pi pi-home",
#         "link": "/inicio/",
#         "titulo": "Inicio"
#     },
#     {
#         "id": 55,
#         "id_padre": 54,
#         "path": "/inicio/datos-personales/",
#         "icono": "icon",
#         "link": "/inicio/datos-personales/",
#         "titulo": "Datos Personales"
#     },
#     {
#         "id": 56,
#         "id_padre": 55,
#         "path": "/inicio/datos-personales/actualizar-datos/",
#         "icono": "icon",
#         "link": "/inicio/datos-personales/actualizar-datos/",
#         "titulo": "Actualizar Datos"
#     },
#     {
#         "id": 57,
#         "id_padre": 0,
#         "path": "/encuestas/",
#         "icono": "pi pi-book",
#         "link": "/encuestas/",
#         "titulo": "Encuestas"
#     },
#     {
#         "id": 58,
#         "id_padre": 57,
#         "path": "/encuestas/mis-encuestas/",
#         "icono": "icon",
#         "link": "/encuestas/mis-encuestas/",
#         "titulo": "Mis Encuestas"
#     },
#     {
#         "id": 59,
#         "id_padre": 58,
#         "path": "/encuestas/mis-encuestas/llenar-encuestas/",
#         "icono": "icon",
#         "link": "/encuestas/mis-encuestas/llenar-encuestas/",
#         "titulo": "LLenar encuestas"
#     },
#     {
#         "id": 60,
#         "id_padre": 0,
#         "path": "/pqrs/",
#         "icono": "pi pi-folder",
#         "link": "/pqrs/",
#         "titulo": "PQRS"
#     },
#     {
#         "id": 61,
#         "id_padre": 60,
#         "path": "/pqrs/solicitud/",
#         "icono": "icon",
#         "link": "/pqrs/solicitud/",
#         "titulo": "Solicitudes"
#     },
#     {
#         "id": 62,
#         "id_padre": 61,
#         "path": "/pqrs/solicitud/crear/",
#         "icono": "icon",
#         "link": "/pqrs/solicitud/crear/",
#         "titulo": "Crear"
#     },
#     {
#         "id": 63,
#         "id_padre": 61,
#         "path": "/pqrs/solicitud/mis-solicitudes/",
#         "icono": "icon",
#         "link": "/pqrs/solicitud/mis-solicitudes/",
#         "titulo": "Mis Solicitudes"
#     },
#     {
#         "id": 67,
#         "id_padre": 0,
#         "path": "/clasificados/",
#         "icono": "pi pi-briefcase",
#         "link": "/clasificados/",
#         "titulo": "Clasificados"
#     },
#     {
#         "id": 68,
#         "id_padre": 67,
#         "path": "/clasificados/emprendimientos/",
#         "icono": "icon",
#         "link": "/clasificados/emprendimientos/",
#         "titulo": "Emprendimientos"
#     },
#     {
#         "id": 69,
#         "id_padre": 68,
#         "path": "/clasificados/emprendimientos/ver",
#         "icono": "icon",
#         "link": "/clasificados/emprendimientos/ver",
#         "titulo": "Mostrar"
#     },
#     {
#         "id": 70,
#         "id_padre": 68,
#         "path": "/clasificados/emprendimientos/crear",
#         "icono": "icon",
#         "link": "/clasificados/emprendimientos/crear",
#         "titulo": "Crear"
#     },
#     {
#         "id": 73,
#         "id_padre": 0,
#         "path": "/eventos/",
#         "icono": "pi pi-ticket",
#         "link": "/eventos/",
#         "titulo": "Eventos"
#     },
#     {
#         "id": 74,
#         "id_padre": 73,
#         "path": "/eventos/actividades/",
#         "icono": "icon",
#         "link": "/eventos/actividades/",
#         "titulo": "Actividades"
#     },
#     {
#         "id": 75,
#         "id_padre": 74,
#         "path": "/eventos/actividades/mis-actividades/",
#         "icono": "icon",
#         "link": "/eventos/actividades/mis-actividades/",
#         "titulo": "Mis Actividades"
#     },
#     {
#         "id": 76,
#         "id_padre": 68,
#         "path": "/clasificados/emprendimientos/mis-emprendimientos/",
#         "icono": "icon",
#         "link": "/clasificados/emprendimientos/mis-emprendimientos/",
#         "titulo": "Mis Emprendimientos"
#     }
# ]
