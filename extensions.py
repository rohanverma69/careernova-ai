from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

# Configure login manager
login_manager.login_view = "auth.login"
login_manager.login_message = "Please sign in to access your dashboard and assessments."
login_manager.login_message_category = "info"
