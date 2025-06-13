from blueprints.frontend import frontend_bp
from blueprints.hls import hls_bp
from blueprints.media import media_bp
from blueprints.api import api_bp
from blueprints.broadcast import broadcast_bp, sock
from flask import Flask

app = Flask(__name__)
app.register_blueprint(frontend_bp)
app.register_blueprint(hls_bp)
app.register_blueprint(media_bp)
app.register_blueprint(api_bp)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)