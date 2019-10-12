from app import create_app
from .utils import update

update.run()
app = create_app()
