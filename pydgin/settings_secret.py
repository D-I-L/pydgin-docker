import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'pcw(yn@$%+#!9tb5cs(cwhw62my4o46+%_hs&af(m(*l0!l#s3'

# Memcached caching
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'localhost:11211',
    }
}

# Remember to create the database first
# sudo -u postgres psql -c "CREATE database pydgin_authdb;"
# sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE "pydgin_authdb" TO webuser;"

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'pydgin_authdb',
#        'USER': 'webuser',
#        'PASSWORD': 'webuser',
#        'HOST': 'localhost',
#        'PORT': '5432',
#        'TEST': {
#                'NAME': 'auto_tests',
#            },
#        },
#
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT'],
        'TEST': {
                'NAME': 'auto_tests',
            },
    }
}



RSERVE = {
    'HOST': 'localhost',
    'PORT': 6311
}
# remember this is the key of the auth_db DATABASES settings
AUTH_DB = 'default'
INCLUDE_USER_UPLOADS = False

# DATABASE_ROUTERS = ['pydgin_auth.routers.AuthRouter', 'pydgin.routers.DefaultRouter']

# elastic search engine
ELASTIC = {
    'default': {
        'ELASTIC_URL': ['http://elasticsearch:9200/'],
        'VERSION': {'major': 2},
        'DOCUMENT_FACTORY': 'core.document.PydginDocument',
        'IDX': {
            'GENE': {
                'name': 'genes_hg38_v0.0.2',
                'idx_type': {
                    'GENE': {'type': 'gene', 'search': True,
                             'auth_public': True, 'class': 'gene.document.GeneDocument'},
                    'PATHWAY': {'type': 'pathway_genesets', 'auth_public': True},
                    'INTERACTIONS': {'type': 'interactions',  'auth_public': True}
                },
                'label': 'gene related indices',
                'suggester': True,
                'auth_public': True
            },
            'PUBLICATION': {
                'name': 'publications_v0.0.5',
                'idx_type': {
                    'PUBLICATION': {'type': 'publication', 'search': True,
                                    'auth_public': True, 'class': 'core.document.PublicationDocument'}
                },
                'suggester': True,
                'auth_public': True
            },
            'MARKER': {
                'name': 'dbsnp146', 'build': '38',
                'idx_type': {
                    'MARKER': {'type': 'marker', 'description': 'dbsnp', 'search': True,
                               'auth_public': True, 'class': 'marker.document.MarkerDocument'},
                    'HISTORY': {'type': 'rs_merge', 'search': True,
                                'auth_public': True, 'class': 'marker.document.MarkerDocument'},
                    'IC': {'type': 'immunochip', 'search': True,
                           'auth_public': True, 'class': 'marker.document.ImmunoChipDocument'}
                },
                'suggester': True,
                'auth_public': True
            },
#             'MARKER_144': {
#                 'name': 'dbsnp144', 'build': '38', 'auth_public': True,
#                 'idx_type': {'MARKER': {'type': 'marker'}},
#             },
#             'MARKER_138': {
#                 'name': 'dbsnp138', 'build': '37', 'auth_public': True,
#                 'idx_type': {'MARKER': {'type': 'marker'}},
#             },
            'DISEASE': {
                'name': 'disease',
                'idx_type': {
                    'DISEASE': {'type': 'disease', 'search': True,  'auth_public': True,
                                'class': 'disease.document.DiseaseDocument'}
                },
                'suggester': True,
                'auth_public': True
            },
            'REGION': {
                'name': 'regions_v0.0.5',
                'idx_type': {
                    'STUDY_HITS': {'type': 'hits', 'search': True,
                                   'auth_public': True, 'class': 'region.document.StudyHitDocument'},
                    'DISEASE_LOCUS': {'type': 'disease_locus',  'auth_public': True},
                    'REGION': {'type': 'region', 'search': True,
                               'auth_public': True, 'class': 'region.document.RegionDocument'}
                },
                'suggester': True,
                'auth_public': True
            },
            'STUDY': {
                'name': 'studies_v0.0.2',
                'idx_type': {
                    'STUDY': {'type': 'studies', 'auth_public': True, 'search': True,
                              'class': 'study.document.StudyDocument'}
                },
                'suggester': True,
                'auth_public': True
            },
            'CRITERIA': {
                'name': 'imb_criteria',
                'idx_type': {
                    'GENE': {'type': 'gene',  'auth_public': True},
                    'MARKER': {'type': 'marker',  'auth_public': True}
                },
                'auth_public': True
            }
        },
        'TEST': 'auto_tests_tjc',
        'REPOSITORY': 'my_backup',
        'TEST_REPO_DIR': '/Users/tjc29/elastic_data/repo/',
#        'TEST_REPO_DIR': '/ipswich/data/pydgin/elastic/repos/'
    }
}

# selenium browser testing host and headless mode
SELENIUM = {
    'HEADLESS': True,
    'HOST': 'localhost:8000',
    'CHROME_DRIVER': '/gdxbase/www/drivers/chromedriver',
    'OPERA_DRIVER': '/gdxbase/www/drivers/operadriver64',
    'OPERA_BIN': '/usr/bin/opera',
}

# Admin URL path for obfuscating the admin interface
ADMIN_URL_PATH = 'pydginadmin'

# SMTP
DEFAULT_FROM_EMAIL = 'immunobase-feedback@cimr.cam.ac.uk'
SERVER_EMAIL = 'immunobase-feedback@cimr.cam.ac.uk'
EMAIL_HOST = 'ppsw.cam.ac.uk'
EMAIL_HOST_USER = ''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 25
EMAIL_USE_TLS = True
