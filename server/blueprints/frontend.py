from flask import Blueprint, send_from_directory
import os

frontend_bp = Blueprint("frontend", __name__)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../apps"))

@frontend_bp.route("/")
def index():
    print("BASE_DIR:", BASE_DIR)
    print("Contents of viewer:", os.listdir(os.path.join(BASE_DIR, "viewer")))
    return send_from_directory(os.path.join(BASE_DIR, "viewer"), "index.html")

@frontend_bp.route("/apps/<appname>/")
def serve_app_index(appname):
    # Serve index.html for broadcaster or viewer
    return send_from_directory(os.path.join(BASE_DIR, appname), "index.html")

@frontend_bp.route("/apps/<appname>/<path:filename>")
def serve_app_files(appname, filename):
    # Serve static files for each app
    return send_from_directory(os.path.join(BASE_DIR, appname), filename)