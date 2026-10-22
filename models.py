from datetime import datetime, timezone
import json
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from extensions import db, login_manager


class User(UserMixin, db.Model):
    """User account model."""
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(120), nullable=True)
    bio = db.Column(db.Text, nullable=True)
    target_role = db.Column(db.String(100), nullable=True)
    experience_level = db.Column(db.String(50), default="Student / Beginner")
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    # Relationships
    assessments = db.relationship(
        "Assessment", backref="user", lazy="dynamic", cascade="all, delete-orphan"
    )
    saved_careers = db.relationship(
        "SavedCareer", backref="user", lazy="dynamic", cascade="all, delete-orphan"
    )
    skill_progresses = db.relationship(
        "SkillProgress", backref="user", lazy="dynamic", cascade="all, delete-orphan"
    )

    def set_password(self, password: str) -> None:
        """Hash and set user password securely."""
        self.password_hash = generate_password_hash(password, method="scrypt")

    def check_password(self, password: str) -> bool:
        """Verify password hash."""
        return check_password_hash(self.password_hash, password)

    def get_initials(self) -> str:
        """Get 1-2 character user avatar initials."""
        if self.full_name and self.full_name.strip():
            parts = self.full_name.strip().split()
            if len(parts) >= 2:
                return (parts[0][0] + parts[-1][0]).upper()
            return parts[0][:2].upper()
        return self.username[:2].upper()

    def __repr__(self) -> str:
        return f"<User {self.username}>"


@login_manager.user_loader
def load_user(user_id: str):
    """Flask-Login user loader callback."""
    if user_id is None or user_id == "None":
        return None
    return db.session.get(User, int(user_id))


class Assessment(db.Model):
    """Career assessment submission and generated recommendations."""
    __tablename__ = "assessments"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True, index=True)

    # User inputs stored for historical review
    education_level = db.Column(db.String(80), nullable=False)
    experience_years = db.Column(db.String(40), nullable=False)
    work_style = db.Column(db.String(80), nullable=False)
    primary_skills_json = db.Column(db.Text, nullable=False, default="[]")
    interests_json = db.Column(db.Text, nullable=False, default="[]")
    career_goals = db.Column(db.Text, nullable=True)

    # Computed recommendations output stored as structured JSON
    results_json = db.Column(db.Text, nullable=False, default="{}")
    top_career_key = db.Column(db.String(100), nullable=True)
    top_career_title = db.Column(db.String(120), nullable=True)
    top_career_score = db.Column(db.Integer, default=0)

    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), index=True)

    @property
    def primary_skills(self):
        try:
            return json.loads(self.primary_skills_json)
        except Exception:
            return []

    @primary_skills.setter
    def primary_skills(self, value):
        self.primary_skills_json = json.dumps(value or [])

    @property
    def interests(self):
        try:
            return json.loads(self.interests_json)
        except Exception:
            return []

    @interests.setter
    def interests(self, value):
        self.interests_json = json.dumps(value or [])

    @property
    def results(self):
        try:
            return json.loads(self.results_json)
        except Exception:
            return {}

    @results.setter
    def results(self, value):
        self.results_json = json.dumps(value or {})

    def __repr__(self) -> str:
        return f"<Assessment #{self.id} User={self.user_id} Top={self.top_career_title}>"


class SavedCareer(db.Model):
    """User bookmarked careers with roadmap tracking status."""
    __tablename__ = "saved_careers"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    career_key = db.Column(db.String(100), nullable=False)
    career_title = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(40), default="exploring")  # exploring, preparing, applying
    notes = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))

    __table_args__ = (
        db.UniqueConstraint("user_id", "career_key", name="uq_user_career"),
    )

    def __repr__(self) -> str:
        return f"<SavedCareer User={self.user_id} Career={self.career_key}>"


class SkillProgress(db.Model):
    """User skill acquisition status tracking."""
    __tablename__ = "skill_progresses"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)
    skill_name = db.Column(db.String(100), nullable=False)
    career_key = db.Column(db.String(100), nullable=True)
    status = db.Column(db.String(40), default="to_learn")  # to_learn, in_progress, completed
    updated_at = db.Column(
        db.DateTime,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc)
    )

    __table_args__ = (
        db.UniqueConstraint("user_id", "skill_name", name="uq_user_skill"),
    )

    def __repr__(self) -> str:
        return f"<SkillProgress User={self.user_id} Skill={self.skill_name} Status={self.status}>"
