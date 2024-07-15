import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'cms.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')