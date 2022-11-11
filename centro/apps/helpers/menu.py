resources = [
    {
        "path": "/dashboard",
        "id_padre": 0,
        "method": "GET",
        "icono": "pi pi-home",
        "link": "/dashboard",
        "titulo": "Admin",
        "items": [
            {
                "path": "/dashboard/admin",
                "method": "GET",
                "icono": "pi pi-user",
                "link": "/dashboard/admin",
                "titulo": "Roles Y Recursos",
                "items": [
                    {
                        "path": "/dashboard/admin/ver-crear/",
                        "method": "POST",
                        "icono": "icon",
                        "link": "/dashboard/admin/ver-editar/",
                        "titulo": "Ver Editar"
                    },
                    {
                        "path": "/dashboard/admin/ver/",
                        "method": "GET",
                        "icono": "icon",
                        "link": "/dashboard/admin/crear/",
                        "titulo": "Crear"
                    }
                ]
            }
        ]
    }
]
