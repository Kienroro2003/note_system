import os

SECRET_KEY = os.environ.get("SECRET_KEY") or "a-very-secret-key"
print(SECRET_KEY)
