import os

class Config:
    # Read database URL from environment variable, fallback to local SQLite for dev
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URL", "sqlite:///app.db")

    # Disable modification tracking to save resources
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Secret key for form CSRF protection (use a secure value in production)
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret_key")
