import logging

import pymysql
from flask import current_app

active_db_config = "primary"


def get_db_connection():
    global active_db_config

    configs = {
        "primary": {
            "host": current_app.config["MYSQL_PRIMARY_HOST"],
            "port": current_app.config["MYSQL_PRIMARY_PORT"],
            # ... các thông tin khác
        },
        "standby": {
            "host": current_app.config["MYSQL_STANDBY_HOST"],
            "port": current_app.config["MYSQL_STANDBY_PORT"],
            # ... các thông tin khác
        },
    }

    # Ưu tiên thử kết nối với DB đang active
    if active_db_config == "primary":
        preferred_order = ["primary", "standby"]
    else:
        preferred_order = ["standby", "primary"]

    for config_name in preferred_order:
        config = configs[config_name]
        try:
            conn = pymysql.connect(
                host=config["host"],
                port=config["port"],
                user=current_app.config["MYSQL_USER"],
                password=current_app.config["MYSQL_PASSWORD"],
                database=current_app.config["MYSQL_DB"],
                connect_timeout=current_app.config["MYSQL_CONNECT_TIMEOUT"],
                cursorclass=pymysql.cursors.DictCursor,
            )

            # Nếu kết nối thành công, cập nhật lại trạng thái active và trả về
            if active_db_config != config_name:
                logging.warning(f"Switched active database to {config_name}")
                active_db_config = config_name

            return conn

        except pymysql.err.OperationalError as e:
            logging.error(f"Failed to connect to {config_name} DB: {e}")
            continue  # Thử kết nối tiếp theo

    # Nếu cả hai đều thất bại
    logging.critical("FATAL: Both primary and standby databases are unreachable.")
    raise Exception("Database service is unavailable.")
