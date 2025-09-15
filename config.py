import os

from dotenv import load_dotenv

# Tự động tìm và tải các biến từ file .env vào môi trường
load_dotenv()


class Config:
    """
    Lớp cấu hình cho ứng dụng Flask.
    Đọc tất cả các giá trị từ biến môi trường để tăng tính bảo mật và linh hoạt.
    """

    # Đọc SECRET_KEY từ biến môi trường.
    # Nếu không tìm thấy, ứng dụng sẽ không khởi động (an toàn hơn)
    SECRET_KEY = os.environ.get("SECRET_KEY")

    # --- Cấu hình cho DB chính ---
    MYSQL_PRIMARY_HOST = os.environ.get("MYSQL_PRIMARY_HOST")
    MYSQL_PRIMARY_PORT = int(
        os.environ.get("MYSQL_PRIMARY_PORT")
    )  # Chuyển đổi sang kiểu số nguyên
    MYSQL_DB = os.environ.get("DB_NAME")
    MYSQL_USER = os.environ.get("DB_USER")
    MYSQL_PASSWORD = os.environ.get("DB_PASSWORD")

    # --- Cấu hình cho DB dự phòng ---
    MYSQL_STANDBY_HOST = os.environ.get("MYSQL_STANDBY_HOST")
    MYSQL_STANDBY_PORT = int(
        os.environ.get("MYSQL_STANDBY_PORT")
    )  # Chuyển đổi sang kiểu số nguyên

    # --- Cấu hình khác ---
    # Timeout kết nối (giây), đọc từ môi trường và chuyển sang kiểu số nguyên
    MYSQL_CONNECT_TIMEOUT = int(os.environ.get("MYSQL_CONNECT_TIMEOUT"))
