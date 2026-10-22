import os
import sys
import json
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
        path_info = environ.get("PATH_INFO", "")

        # Instant diagnostics endpoint
        if "debug=1" in qs or "debug_wsgi" in path_info:
            start_response("200 OK", [("Content-Type", "application/json")])
            debug_info = {
                "PATH_INFO": environ.get("PATH_INFO"),
                "QUERY_STRING": environ.get("QUERY_STRING"),
                "RAW_URI": environ.get("RAW_URI"),
                "REQUEST_URI": environ.get("REQUEST_URI"),
                "HTTP_X_FORWARDED_URI": environ.get("HTTP_X_FORWARDED_URI"),
                "HTTP_X_MATCHED_PATH": environ.get("HTTP_X_MATCHED_PATH"),
                "HTTP_X_VERCEL_PATH": environ.get("HTTP_X_VERCEL_PATH"),
                "ALL_MATCHING_KEYS": {
                    k: environ[k] for k in environ.keys()
                    if any(w in k for w in ("PATH", "URI", "URL", "ROUTE", "VERCEL"))
                }
            }
            return [json.dumps(debug_info, indent=2).encode("utf-8")]

        if qs and "__path=" in qs:
            params = urllib.parse.parse_qs(qs)
            if "__path" in params and params["__path"]:
                actual_path = params["__path"][0]
                while "//" in actual_path:
                    actual_path = actual_path.replace("//", "/")
                if not actual_path.startswith("/"):
                    actual_path = "/" + actual_path
                environ["PATH_INFO"] = actual_path
                
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
