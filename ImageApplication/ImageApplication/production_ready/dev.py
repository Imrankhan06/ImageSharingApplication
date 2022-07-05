""" This file is to maintain all dev settings. """

from decouple import config
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = config('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# For media store in the bucket
from google.oauth2 import service_account

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(os.path.join(BASE_DIR, 'credentials.json'))

# Configuration for media file storing and retriving media file from gcloud
DEFAULT_FILE_STORAGE = config('DEFAULT_FILE_STORAGE')
GS_PROJECT_ID = config('GS_PROJECT_ID')
GS_BUCKET_NAME = config('GS_BUCKET_NAME')
MEDIA_ROOT = "media/"
UPLOAD_ROOT = 'media/uploads/'
MEDIA_URL = f'https://storage.googleapis.com/{GS_BUCKET_NAME}/'
