import os
PROJECT_NAME = "projectionist"
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_DIR = os.path.join(BASE_DIR, 'projectionist/static')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'projectionist/templates')
MONGO_URI = "mongodb://127.0.0.1:27017"


PROXY = None

DOMAIN = "127.0.0.1:8000"

LAIN_DOMAIN = os.getenv('LAIN_DOMAIN')
CLIENT_COLLECTION = "projectionist"
# 补充线上
