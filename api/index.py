import os
import sys

# Ensure the root project directory is in sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from app import app


class VercelPathFixMiddleware:
    """
    WSGI middleware that normalizes PATH_INFO on Vercel.
    When Vercel rewrites incoming requests to /api/index, PATH_INFO
    is prefixed with /api/index. This middleware strips that prefix
    so Flask routes match cleanly.
    """
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        path_info = environ.get("PATH_INFO", "")
        for prefix in ("/api/index", "/api/app", "/app.py"):
            if path_info.startswith(prefix):
                path_info = path_info[len(prefix):]
                if not path_info.startswith("/"):
                    path_info = "/" + path_info
                environ["PATH_INFO"] = path_info
                break

        return self.wsgi_app(environ, start_response)


# Wrap Flask application with the path normalization middleware
app.wsgi_app = VercelPathFixMiddleware(app.wsgi_app)
