from app import app, socket_io
from app.blueprints import BLUEPRINTS


# Register blueprints
for b in BLUEPRINTS:
    app.register_blueprint(b)


host = '0.0.0.0'
port = 5000

# app.run(host=host, port=port)
socket_io.run(app, host=host, port=port)
