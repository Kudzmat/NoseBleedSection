import os
from pathlib import Path
from dotenv import load_dotenv

# Production/Upsun settings.
from NoseBleedSeat.settings import BASE_DIR

if os.getenv('PLATFORM_APPLICATION_NAME') is not None:
    DEBUG = False

    # Static dir.
    if os.getenv('PLATFORM_APP_DIR') is not None:
        STATIC_ROOT = os.path.join(os.getenv('PLATFORM_APP_DIR'), 'static')

    # Secret Key.
    if os.getenv('PLATFORM_PROJECT_ENTROPY') is not None:
        SECRET_KEY = os.getenv('PLATFORM_PROJECT_ENTROPY')

    # Production database configuration.
    if os.getenv('PLATFORM_ENVIRONMENT') is not None:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql',
                'NAME': os.getenv('DATABASE_PATH'),
                'USER': os.getenv('DATABASE_USERNAME'),
                'PASSWORD': os.getenv('DATABASE_PASSWORD'),
                'HOST': os.getenv('DATABASE_HOST'),
                'PORT': os.getenv('DATABASE_PORT'),
            },
            'sqlite': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            }
        }
