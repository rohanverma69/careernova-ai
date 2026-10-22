import os
import sys
import re

# Add root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
from engine.careers_data import CAREERS_DATABASE

def build_github_pages():
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "docs"))
    os.makedirs(output_dir, exist_ok=True)
    
    # Copy static assets into docs/static
    import shutil
    static_src = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "static"))
    static_dest = os.path.join(output_dir, "static")
    if os.path.exists(static_dest):
        shutil.rmtree(static_dest)
    shutil.copytree(static_src, static_dest)
    print(f"Copied static assets to {static_dest}")

    # Routes to export
    routes_to_export = [
        ("/", "index.html"),
        ("/careers", "careers.html"),
        ("/about", "about.html"),
        ("/login", "login.html"),
        ("/register", "register.html"),
        ("/assessment", "assessment.html"),
    ]
    
    # Also export individual career detail pages
    for career_slug in CAREERS_DATABASE.keys():
        routes_to_export.append((f"/careers/{career_slug}", f"career-{career_slug}.html"))

    with app.test_client() as client:
        # Enable guest/demo session
        for route, filename in routes_to_export:
            resp = client.get(route)
            if resp.status_code == 200 or resp.status_code == 302:
                html = resp.data.decode("utf-8")
                
                # Replace links for GitHub Pages compatibility (/careernova-ai/)
                # 1. Update static links
                html = re.sub(r'href="/static/', r'href="./static/', html)
                html = re.sub(r'src="/static/', r'src="./static/', html)
                
                # 2. Update navigation links to point to .html files
                html = re.sub(r'href="/"', r'href="./index.html"', html)
                html = re.sub(r'href="/careers"', r'href="./careers.html"', html)
                html = re.sub(r'href="/about"', r'href="./about.html"', html)
                html = re.sub(r'href="/login"', r'href="./login.html"', html)
                html = re.sub(r'href="/register"', r'href="./register.html"', html)
                html = re.sub(r'href="/assessment"', r'href="./assessment.html"', html)
                html = re.sub(r'href="/dashboard"', r'href="./dashboard.html"', html)
                
                for slug in CAREERS_DATABASE.keys():
                    html = re.sub(rf'href="/careers/{slug}"', rf'href="./career-{slug}.html"', html)
                
                out_path = os.path.join(output_dir, filename)
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(html)
                print(f"Exported: {route} -> docs/{filename}")
            else:
                print(f"Skipped {route} (status {resp.status_code})")

    # Create .nojekyll in docs to allow standard files
    nojekyll_path = os.path.join(output_dir, ".nojekyll")
    with open(nojekyll_path, "w") as f:
        f.write("")
    print("Created docs/.nojekyll")
    print(f"\nSuccessfully built static GitHub Pages distribution in: {output_dir}")

if __name__ == "__main__":
    build_github_pages()
