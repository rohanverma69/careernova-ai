import os
import sys
import urllib.parse

# Ensure the root project directory is in sys.path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from app import app


class VercelPathFixMiddleware:
    """
    WSGI middleware that normalizes PATH_INFO on Vercel.
    Extracts the matched incoming route from __path parameter
    or fallback headers/prefixes so all Flask routes, static assets,
    and blueprints match accurately.
    """
    def __init__(self, wsgi_app):
        self.wsgi_app = wsgi_app

    def __call__(self, environ, start_response):
        qs = environ.get("QUERY_STRING", "")
        if qs and "__path=" in qs:
            params = urllib.parse.parse_qs(qs)
            if "__path" in params and params["__path"]:
                actual_path = params["__path"][0]
                # Normalize double slashes
                while "//" in actual_path:
                    actual_path = actual_path.replace("//", "/")
                if not actual_path.startswith("/"):
                    actual_path = "/" + actual_path
                environ["PATH_INFO"] = actual_path
                
                # Remove __path from query string so endpoints receive clean arguments
                cleaned_params = {k: v for k, v in params.items() if k != "__path"}
                environ["QUERY_STRING"] = urllib.parse.urlencode(cleaned_params, doseq=True)
        else:
            raw_uri = (
                environ.get("RAW_URI")
                or environ.get("REQUEST_URI")
                or environ.get("HTTP_X_FORWARDED_URI")
                or environ.get("HTTP_X_MATCHED_PATH")
            )
            if raw_uri:
                path = raw_uri.split("?")[0]
                if path and not path.startswith("/api/index"):
                    environ["PATH_INFO"] = path

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
