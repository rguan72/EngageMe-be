import os
base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:
    FLASK_APP = os.environ.get('FLASK_APP') or 'app/wsgi.py'
