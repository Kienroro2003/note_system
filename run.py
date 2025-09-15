# run.py
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Chạy ứng dụng ở chế độ debug
    # host='0.0.0.0' để có thể truy cập từ bên ngoài container (nếu bạn chạy app trong Docker)
    app.run(host="0.0.0.0", port=4000, debug=True)
