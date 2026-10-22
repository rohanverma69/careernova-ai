"""
CareerNova AI - Next-Generation AI Career Guidance Platform
Main application entry point for local execution and Vercel serverless deployment.
Exports top-level Flask instance named 'app'.
"""

import os
from datetime import datetime, timezone
from flask import Flask, render_template, jsonify
from flask_wtf.csrf import CSRFError
from config import Config
from extensions import db, login_manager, csrf


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def create_app(config_class=Config) -> Flask:
    """Application factory for CareerNova AI."""
    app = Flask(
        __name__,
        static_folder=os.path.join(BASE_DIR, "static"),
        static_url_path="/static",
        template_folder=os.path.join(BASE_DIR, "templates")
    )

    # Load configuration
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)

    # Register Blueprints
    from routes.main import main_bp
    from routes.auth import auth_bp
    from routes.assessment import assessment_bp
    from routes.dashboard import dashboard_bp
    from routes.api import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(assessment_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(api_bp)

    # Global template context processors
    @app.context_processor
    def inject_global_template_data():
        return {
            "app_name": "CareerNova AI",
            "current_year": datetime.now(timezone.utc).year,
            "has_ai_key": bool(app.config.get("AI_API_KEY")),
            "is_production": app.config.get("IS_PRODUCTION", False)
        }

    # Custom Error Handlers
    @app.errorhandler(404)
    def page_not_found(e):
        return render_template("errors/404.html"), 404

    @app.errorhandler(403)
    def forbidden_access(e):
        return render_template(
            "errors/404.html",
            error_code=403,
            error_title="Access Forbidden",
            error_message="You don't have permission to access this career assessment or dashboard."
        ), 403

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template("errors/500.html"), 500

    @app.errorhandler(CSRFError)
    def handle_csrf_error(e):
        return render_template(
            "errors/500.html",
            error_title="Session Security Check",
            error_message="Your security token expired or is invalid. Please refresh the page and try again."
        ), 400

    # Non-destructive database initialization within context
    with app.app_context():
        import models  # noqa: F401 - Register models
        try:
            db.create_all()
        except Exception as e:
            app.logger.warning("Auto db.create_all() skipped or failed: %s", e)

    return app


# Export top-level Flask application instance required by Vercel
app = create_app()

if __name__ == "__main__":
    # Local development server
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
