# File: app/db_manager.py (Đã sửa)
import logging

import pymysql
from flask import current_app

# Biến toàn cục để theo dõi DB nào đang hoạt động
active_db_config = "primary"


def get_db_connection():
    """
    Thiết lập kết nối đến cơ sở dữ liệu.
    Tự động chuyển sang DB dự phòng nếu DB chính gặp sự cố.
    """
    global active_db_config

    # Xây dựng từ điển cấu hình đầy đủ từ app.config
    configs = {
        "primary": {
            "host": current_app.config["MYSQL_PRIMARY_HOST"],
            "port": current_app.config["MYSQL_PRIMARY_PORT"],
            "user": current_app.config["MYSQL_USER"],
            "password": current_app.config["MYSQL_PASSWORD"],
            "database": current_app.config["MYSQL_DB"],
            "connect_timeout": current_app.config["MYSQL_CONNECT_TIMEOUT"],
            "cursorclass": pymysql.cursors.DictCursor,
        },
        "standby": {
            "host": current_app.config["MYSQL_STANDBY_HOST"],
            "port": current_app.config["MYSQL_STANDBY_PORT"],
            "user": current_app.config["MYSQL_USER"],
            "password": current_app.config["MYSQL_PASSWORD"],
            "database": current_app.config["MYSQL_DB"],
            "connect_timeout": current_app.config["MYSQL_CONNECT_TIMEOUT"],
            "cursorclass": pymysql.cursors.DictCursor,
        },
    }

    # Ưu tiên thử kết nối với DB đang active
    if active_db_config == "primary":
        preferred_order = ["primary", "standby"]
    else:
        preferred_order = ["standby", "primary"]

    for config_name in preferred_order:
        try:
            # Lấy cấu hình cho kết nối hiện tại
            config = configs[config_name]
            logging.info(
                f"Attempting to connect to {config_name} DB at {config['host']}:{config['port']}..."
            )

            # Sử dụng **config để truyền tất cả tham số vào hàm connect
            conn = pymysql.connect(**config)

            # Nếu kết nối thành công, cập nhật lại trạng thái active và trả về
            if active_db_config != config_name:
                logging.warning(f"SUCCESS: Switched active database to {config_name}")
                active_db_config = config_name
            else:
                logging.info(f"SUCCESS: Connected to {config_name} DB.")

            return conn

        except pymysql.err.OperationalError as e:
            logging.error(f"FAILED to connect to {config_name} DB: {e}")
            continue  # Thử kết nối tiếp theo

    # Nếu cả hai đều thất bại
    logging.critical("FATAL: Both primary and standby databases are unreachable.")
    raise Exception("Database service is unavailable.")
