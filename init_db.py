"""
Database initialization and verification utility for CareerNova AI.
Safely creates all database tables if they do not exist.
Does NOT drop or reset existing tables.
Usage:
    python init_db.py
"""

import sys
from app import create_app
from extensions import db
import models  # Ensure all model tables are registered with SQLAlchemy


def init_database():
    """Verify and initialize database tables safely."""
    app = create_app()
    with app.app_context():
        try:
            print("Connecting to database...")
            db.create_all()
            print("Successfully verified/created database tables:")
            for table_name in db.metadata.tables.keys():
                print(f"  - {table_name}")
            print("\nDatabase is ready for production use.")
        except Exception as e:
            print(f"Error initializing database: {e}", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    init_database()
