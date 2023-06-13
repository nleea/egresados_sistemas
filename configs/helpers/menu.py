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


resources = [
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
    {
        "path": "/persona/",
        "id_padre": 0,
        "method": "GET",
        "icono": "pi pi-user",
        "link": "/persona/",
        "titulo": "Persona",
        "items": [
            {
                "path": "/persona/datos-personales/",
                "method": "GET",
                "icono": "icon",
                "link": "/persona/datos-personales/",
                "titulo": "Datos Personales",
                "items": [
                    {
                        "path": "/persona/datos-personales/ver/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/persona/datos-personales/ver/",
                        "titulo": "Ver",
                    },
                    {
                        "path": "/persona/datos-personales/crear/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/persona/datos-personales/crear/",
                        "titulo": "Crear",
                    },
                    {
                        "path": "/persona/datos-personales/editar/",
                        "method": "PUT",
                        "icono": "icon",
                        "link": "/persona/datos-personales/editar/",
                        "titulo": "Editar",
                    },
                    {
                        "path": "/persona/datos-personales/eliminar",
                        "method": "DELETE",
                        "icono": "icon",
                        "link": "/persona/datos-personales/eliminar",
                        "titulo": "Eliminar",
                    },
                ],
            }
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
