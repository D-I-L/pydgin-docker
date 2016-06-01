import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5ez6uKJ^nV+uW;Vb?Q.GDyZU<TeWOBw<6b:>4t3UFZwVM[=g/(.bK}#H@iCAJ~wn,!eZcNjz0VziClHUMF>@2BEU?5|Vc/w_'

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
    'HOST': 'rserve',
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
                'name': 'dbsnp146', 'build': 38,
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
            'MARKER_146': {
                'name': 'dbsnp146_grch37', 'build': 37, 'auth_public': True,
                'idx_type': {'MARKER': {'type': 'marker'}},
            },
#             'MARKER_138': {
#                 'name': 'dbsnp138', 'build': 37, 'auth_public': True,
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
            'BAND': {
                'name': 'bands_hg38',
                'idx_type': {
                    'BAND': {'type': 'bands', 'search': False, 'auth_public': True, 'class': 'core.document.FeatureDocument'},
                    'CHROM': {'type': 'chromosome'}
                },
                'auth_public': True
            },
            'REGION': {
                'name': 'regions_latest',
                'idx_type': {
                    'STUDY_HITS': {'type': 'hits', 'search': True,
                                   'auth_public': True, 'class': 'region.document.StudyHitDocument'},
                    'DISEASE_LOCUS': {'type': 'disease_locus',  'auth_public': True,
                                      'class': 'region.document.DiseaseLocusDocument'},
                    'REGION': {'type': 'region', 'search': True,
                               'auth_public': True, 'class': 'region.document.RegionDocument'}
                },
                'suggester': True,
                'auth_public': True
            },
            'STUDY': {
                'name': 'studies_latest',
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
                    'GENE': {'type': 'gene', 'auth_public': True},
                    'MARKER': {'type': 'marker', 'auth_public': True}
                },
                'auth_public': True
            },
            'GENE_CRITERIA': {
                'name': 'pydgin_imb_criteria_gene',
                'idx_type': {
                    'IS_GENE_IN_MHC': {'type': 'is_gene_in_mhc',  'auth_public': True},
                    'CAND_GENE_IN_STUDY': {'type': 'cand_gene_in_study',  'auth_public': True},
                    'CAND_GENE_IN_REGION': {'type': 'cand_gene_in_region',  'auth_public': True},
                    'GENE_IN_REGION': {'type': 'gene_in_region',  'auth_public': True},
                    'EXONIC_INDEX_SNP_IN_REGION': {'type': 'exonic_index_snp_in_gene',  'auth_public': True},
                },
                'auth_public': True
            },
            'MARKER_CRITERIA': {
                'name': 'pydgin_imb_criteria_marker',
                'idx_type': {
                    'IS_MARKER_IN_MHC': {'type': 'is_marker_in_mhc',  'auth_public': True},
                    'IS_AN_INDEX_SNP': {'type': 'is_an_index_snp',  'auth_public': True},
                    'MARKER_IS_GWAS_SIGNIFICANT_STUDY': {'type': 'marker_is_gwas_significant_in_study',  'auth_public': True},
                    'RSQ_WITH_INDEX_SNP': {'type': 'rsq_with_index_snp',  'auth_public': True},
                    'MARKER_IS_GWAS_SIGNIFICANT_IC': {'type': 'marker_is_gwas_significant_in_ic',  'auth_public': True},
                },
                'auth_public': True
            },
            'REGION_CRITERIA': {
                'name': 'pydgin_imb_criteria_region',
                'idx_type': {
                    'IS_REGION_IN_MHC': {'type': 'is_region_in_mhc',  'auth_public': True},
                    'IS_REGION_FOR_DISEASE': {'type': 'is_region_for_disease',  'auth_public': True},
                },
                'auth_public': True
            },
            'STUDY_CRITERIA': {
                'name': 'pydgin_imb_criteria_study',
                'idx_type': {
                    'STUDY_FOR_DISEASE': {'type': 'study_for_disease',  'auth_public': True},
                },
                'auth_public': True
            },
            'IC_STATS': {
               'name': 'hg38_ic_statistics',
               'idx_type': {
                        'AS_IGAS': {'type': 'as_igas', 'auth_public': True},
                        'ATD_COOPER': {'type': 'atd_cooper'},
                        'CRO_JOSTINS': {'type': 'cro_jostins'},
                        'CRO_LIU': {'type': 'cro_liu'},
                        'CEL_TRYNKA': {'type': 'cel_trynka', 'auth_public': True},
                        'IBD_JOSTINS': {'type': 'ibd_jostins'},
                        'JIA_HINKS': {'type': 'jia_hinks'},
                        'MS_IMSGC': {'type': 'ms_imsgc', 'auth_public': True},
                        'NAR_FARACO': {'type': 'nar_faraco', 'auth_public': True},
                        'PBC_LIU': {'type': 'pbc_liu', 'auth_public': True},
                        'PSO_TSOI': {'type': 'pso_tsoi'},
                        'RA_EYRE': {'type': 'ra_eyre', 'auth_public': True},
                        'T1D_ONENGUT': {'type': 't1d_onengut', 'auth_public': True},
                        'UC_JOSTINS': {'type': 'uc_jostins'},
                        'UC_LIU': {'type': 'uc_liu'},
               },
               'auth_public': True
            },
            'GWAS_STATS': {
               'name': 'hg38_gwas_statistics',
               'idx_type': {
                   'RA_OKADA': {'type': 'ra_okada', 'auth_public': True}
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
#EMAIL_HOST = 'ppsw.cam.ac.uk'
EMAIL_HOST = '5.28.62.148'
EMAIL_HOST_USER = ''
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 25
EMAIL_USE_TLS = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')

# contact us
#RECAPTCHA_KEY = '6LfLShwTAAAAAJrIsxVnGKL-LumEKAZIqceitkXa'
#RECAPTCHA_SECRET = '6LfLShwTAAAAAEyDSU4veJ9jDR1EC1kLEuE7VP_r'

