import os
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()


class Config:
    """Base application configuration."""

    # Secret key for session security & CSRF
    SECRET_KEY = os.environ.get("SECRET_KEY")
    if not SECRET_KEY:
        # Development fallback with explicit security warning
        # In production on Vercel, SECRET_KEY must always be set in Project Settings
        SECRET_KEY = "dev-secret-careernova-ai-replace-in-production-2025"

    # Production / Environment flags
    FLASK_ENV = os.environ.get("FLASK_ENV", "development")
    IS_VERCEL = os.environ.get("VERCEL") == "1"
    IS_PRODUCTION = (FLASK_ENV == "production") or IS_VERCEL

    # Database configuration
    raw_db_url = os.environ.get("DATABASE_URL", "").strip()

    if raw_db_url:
        # Normalize postgres:// to postgresql:// for SQLAlchemy 2.0+ compatibility
        if raw_db_url.startswith("postgres://"):
            raw_db_url = raw_db_url.replace("postgres://", "postgresql://", 1)
        SQLALCHEMY_DATABASE_URI = raw_db_url
        
        # PostgreSQL Engine options optimized for serverless execution
        engine_options = {
            "pool_pre_ping": True,
            "pool_recycle": 300,
        }
        # Neon and Supabase require SSL. If not specified in the URL query, enforce it.
        if "postgresql" in raw_db_url and "sslmode" not in raw_db_url:
            engine_options["connect_args"] = {"sslmode": "require"}
            
        SQLALCHEMY_ENGINE_OPTIONS = engine_options
    else:
        # Fallback for zero-config local development only
        # Production deployments MUST provide DATABASE_URL (Neon / Supabase / Postgres)
        BASE_DIR = os.path.abspath(os.path.dirname(__file__))
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'careernova.db')}"
        SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_pre_ping": True,
        }

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Cookie & Session Security Settings
    # Enforce HTTPS cookies in production or on Vercel
    SESSION_COOKIE_SECURE = IS_PRODUCTION
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = "Lax"
    PERMANENT_SESSION_LIFETIME = 86400 * 7  # 7 days

    # CSRF Protection
    WTF_CSRF_ENABLED = True
    WTF_CSRF_TIME_LIMIT = 86400  # 24 hours

    # AI Configuration (Optional)
    AI_API_KEY = os.environ.get("AI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    AI_PROVIDER = os.environ.get("AI_PROVIDER", "gemini").lower()


class TestConfig(Config):
    """Configuration for automated test suite."""

    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SESSION_COOKIE_SECURE = False
    SECRET_KEY = "test-secret-key-12345"
    SQLALCHEMY_ENGINE_OPTIONS = {}
