import logging

# app/__init__.py
import os
import sys
from logging.handlers import RotatingFileHandler

from flask import Flask

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# Thêm đường dẫn này vào sys.path
sys.path.insert(0, project_root)
from config import Config


def create_app():
    app = Flask(__name__)

    # Tải cấu hình từ class Config
    app.config.from_object(Config)
    if not app.debug:
        # Tạo thư mục logs nếu chưa tồn tại
        if not os.path.exists("logs"):
            os.mkdir("logs")

        # Cấu hình ghi log ra file
        file_handler = RotatingFileHandler(
            "logs/note_system.log", maxBytes=10240, backupCount=10
        )

        # Cấu hình định dạng của log message
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]"
            )
        )

        # Thiết lập cấp độ log
        file_handler.setLevel(logging.INFO)

        # Gắn handler vào logger của app
        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.INFO)
        app.logger.info("Note System startup")
    # -----------------------

    # Đăng ký blueprint (chứa các routes API)
    from .routes import api as api_blueprint

    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app
