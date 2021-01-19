import waitress
from app import app

port = '5000'
host = '0.0.0.0'    # externally visibles
waitress.serve(
                app,
                url_scheme='https',
                port=port,
                # host=host
            )
