import os
from datetime import timedelta


class Config:
    # Flask app configuration
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'nazirlik_ai_secret_key_2025'

    # Gemini API configuration
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY') or "AIzaSyAk5UaULKxoV3CahPftPIwQA2Io4Ph3nno"

    # Database configuration
    # For Vercel, use /tmp directory for temporary database
    DATABASE_PATH = os.environ.get('DATABASE_PATH') or '/tmp/users.db'

    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)

    # Debug mode
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'

    # Server configuration
    HOST = os.environ.get('FLASK_HOST', '0.0.0.0')
    PORT = int(os.environ.get('FLASK_PORT', 5000))

    # Templates directory
    TEMPLATES_DIR = 'templates'