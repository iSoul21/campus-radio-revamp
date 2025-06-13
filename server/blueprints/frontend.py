from flask import Blueprint, send_from_directory
import os

frontend_bp = Blueprint("frontend", __name__, static_folder="../apps/viewer", static_url_path="")

@frontend_bp.route("/")
def index():
    return frontend_bp.send_static_file("index.html")

@frontend_bp.route("/<path:path>")
def static_proxy(path):
    static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), "../apps/viewer"))
    return send_from_directory(static_folder, path)