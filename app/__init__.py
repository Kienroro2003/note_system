# app/__init__.py
import os
import sys

from flask import Flask

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Thêm đường dẫn này vào sys.path
sys.path.insert(0, project_root)
from config import Config


def create_app():
    app = Flask(__name__)

    # Tải cấu hình từ class Config
    app.config.from_object(Config)

    # Đăng ký blueprint (chứa các routes API)
    from .routes import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
