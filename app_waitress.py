import waitress
from app import app

port = '5000'
waitress.serve(app, url_scheme='https', port=port)
