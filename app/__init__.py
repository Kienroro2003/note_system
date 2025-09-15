# app/__init__.py
from flask import Flask

from .config import Config


def create_app():
    app = Flask(__name__)

    # Tải cấu hình từ class Config
    app.config.from_object(Config)

    # Đăng ký blueprint (chứa các routes API)
    from .routes import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
