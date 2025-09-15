import os


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "a-very-secret-key"

    # Cấu hình cho DB chính
    MYSQL_PRIMARY_HOST = "127.0.0.1"
    MYSQL_PRIMARY_PORT = 3306
    MYSQL_USER = "app_user"
    MYSQL_PASSWORD = "password"
    MYSQL_DB = "notes_db"

    # Cấu hình cho DB dự phòng
    MYSQL_STANDBY_HOST = "127.0.0.2"
    MYSQL_STANDBY_PORT = 3306

    # Timeout kết nối (giây) - Quan trọng để phát hiện lỗi nhanh
    MYSQL_CONNECT_TIMEOUT = 30
