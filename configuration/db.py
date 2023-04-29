
DBS = {
    'mysql-local': {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'egresados',
            'HOST': 'localhost',
            'PORT': '3306',
            'USER': 'root',
            'PASSWORD': 'xyz3602',
        }
    },
    'mysql-clever': {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'bryu1vdeobm9tpqkip87',
            'HOST': 'bryu1vdeobm9tpqkip87-mysql.services.clever-cloud.com',
            'PORT': '3306',
            'USER': 'uha9s6r2kw020rda',
            'PASSWORD': 'L7TagO9edlgmFGA1FxrC',
        }
    },
    'mysql-aws': {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db_egresados',
            'HOST': 'aws-egresado.cgtkjmmfwdhc.us-east-2.rds.amazonaws.com',
            'PORT': '3306',
            'USER': 'admin',
            'PASSWORD': 'xyz3602password',
        }
    }
}
