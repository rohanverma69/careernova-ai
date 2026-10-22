"""
Flask-WTF forms for user authentication, career assessment, and profile settings.
Includes CSRF token protection and server-side validation.
"""

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField,
    TextAreaField,
    SelectField,
    SelectMultipleField,
    SubmitField,
    HiddenField,
    widgets
)
from wtforms.validators import (
    DataRequired,
    Email,
    Length,
    EqualTo,
    ValidationError,
    Optional,
    Regexp
)
from models import User


class MultiCheckboxField(SelectMultipleField):
    """Custom checkbox list widget for multi-select skills and interests."""
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class RegistrationForm(FlaskForm):
    """User account registration form."""
    username = StringField(
        "Username",
        validators=[
            DataRequired(message="Username is required."),
            Length(min=3, max=30, message="Username must be between 3 and 30 characters."),
            Regexp(r"^[A-Za-z0-9_]+$", message="Username must contain only letters, numbers, and underscores.")
        ],
        render_kw={"placeholder": "e.g. alex_nova", "autocomplete": "username"}
    )
    email = StringField(
        "Email Address",
        validators=[
            DataRequired(message="Email address is required."),
            Email(message="Please enter a valid email address format (e.g. demo@example.com)."),
            Length(max=120)
        ],
        render_kw={"placeholder": "you@example.com", "autocomplete": "email"}
    )
    full_name = StringField(
        "Full Name (Optional)",
        validators=[Optional(), Length(max=100)],
        render_kw={"placeholder": "e.g. Alex Morgan"}
    )
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(message="Password is required."),
            Length(min=4, message="Password must be at least 4 characters long.")
        ],
        render_kw={"placeholder": "••••••••", "autocomplete": "new-password"}
    )
    confirm_password = PasswordField(
        "Confirm Password",
        validators=[
            DataRequired(message="Please confirm your password."),
            EqualTo("password", message="Passwords must match.")
        ],
        render_kw={"placeholder": "••••••••", "autocomplete": "new-password"}
    )
    submit = SubmitField("Create Free Account")

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data.strip().lower()).first()
        if user:
            raise ValidationError("This username is already taken. Please choose another.")


class LoginForm(FlaskForm):
    """User sign-in form."""
    login_id = StringField(
        "Email or Username",
        validators=[DataRequired(message="Please enter your email or username.")],
        render_kw={"placeholder": "you@example.com or username", "autocomplete": "username"}
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(message="Password cannot be empty.")],
        render_kw={"placeholder": "••••••••", "autocomplete": "current-password"}
    )
    remember_me = BooleanField("Keep me signed in for 7 days")
    submit = SubmitField("Sign In to CareerNova")


class CareerAssessmentForm(FlaskForm):
    """Multi-step comprehensive career assessment wizard form."""
    education_level = SelectField(
        "Highest Education Level",
        choices=[
            ("High School / Secondary", "High School / Secondary Education"),
            ("Self-Taught / Bootcamp", "Self-Taught / Coding Bootcamp Graduate"),
            ("Bachelor's Degree", "Bachelor's Degree (CS, Engineering, or STEM)"),
            ("Bachelor's (Non-STEM)", "Bachelor's Degree (Humanities / Business / Other)"),
            ("Master's / Postgraduate", "Master's Degree (M.S., M.Tech, MBA)"),
            ("Doctorate / PhD", "Doctorate / PhD / Academic Research")
        ],
        validators=[DataRequired(message="Please select your education level.")]
    )

    experience_years = SelectField(
        "Current Professional Experience",
        choices=[
            ("0-1 years (Entry-Level)", "0-1 years (Student, Beginner, or Career Switcher)"),
            ("1-3 years (Junior)", "1-3 years (Junior Developer / Analyst)"),
            ("3-5 years (Mid-Level)", "3-5 years (Mid-Level Practitioner)"),
            ("5+ years (Senior)", "5+ years (Senior / Lead Professional)")
        ],
        validators=[DataRequired(message="Please select your experience range.")]
    )

    work_style = SelectField(
        "Preferred Work Style & Environment",
        choices=[
            ("Remote / Hybrid", "Remote / Hybrid (High autonomy & flexibility)"),
            ("Collaborative & Fast-paced", "Collaborative & Fast-paced (Cross-functional squads)"),
            ("Analytical & Research-heavy", "Analytical & Research-heavy (Deep focus & experimentation)"),
            ("High-Reliability & Systems", "High-Reliability & Systems (Mission-critical operations)")
        ],
        validators=[DataRequired(message="Please select your preferred work style.")]
    )

    # Core Skills (Users select from predefined high-demand skills or can add custom via JS)
    skills = MultiCheckboxField(
        "Primary Technical & Professional Skills",
        validate_choice=False,
        choices=[
            ("Python", "Python"),
            ("JavaScript / TypeScript", "JavaScript / TypeScript"),
            ("SQL", "SQL"),
            ("React", "React"),
            ("Node.js", "Node.js"),
            ("HTML5 & CSS3", "HTML5 & CSS3"),
            ("Machine Learning", "Machine Learning"),
            ("PyTorch", "PyTorch"),
            ("Docker", "Docker"),
            ("Kubernetes", "Kubernetes"),
            ("AWS / GCP / Azure", "Cloud Platforms (AWS / GCP)"),
            ("Linux / Bash", "Linux / Bash"),
            ("Figma", "Figma / UI Design"),
            ("Git", "Git / Version Control"),
            ("Ethical Hacking / Pen Testing", "Cybersecurity & Pen Testing"),
            ("Network Security", "Network Security"),
            ("Data Visualization", "Data Visualization (Tableau/Power BI)"),
            ("Statistics & Probability", "Math & Statistics"),
            ("Product Roadmap Strategy", "Product Strategy & Roadmaps"),
            ("Agile / Scrum Methodologies", "Agile / Scrum"),
            ("Solidity / Rust", "Solidity / Web3"),
            ("Flutter / React Native", "Mobile App Development"),
            ("Apache Spark / PySpark", "Big Data / PySpark")
        ]
    )

    # Interests
    interests = MultiCheckboxField(
        "Passions & Domain Interests",
        validate_choice=False,
        choices=[
            ("Artificial Intelligence", "Artificial Intelligence & LLMs"),
            ("Web Development", "Building Modern Web Applications"),
            ("Cloud Infrastructure", "Cloud Architecture & DevOps"),
            ("Cybersecurity", "Cyber Defense & Ethical Hacking"),
            ("Data Analysis", "Data Science & Predictive Modeling"),
            ("UI Design", "User Interface & Experience Design"),
            ("Mobile Apps", "Mobile Apps & Smartphone Tech"),
            ("Product Strategy", "Product Leadership & Strategy"),
            ("Decentralization", "Web3, Blockchain & Crypto"),
            ("System Reliability", "Scalable Systems & Uptime"),
            ("Business Strategy", "Business Intelligence & Strategy")
        ]
    )

    career_goals = TextAreaField(
        "Career Vision & Specific Goals",
        validators=[Optional(), Length(max=800)],
        render_kw={
            "placeholder": "e.g. I want to transition into an AI Engineer role within 9 months, build production LLM systems, and secure a high-growth remote position.",
            "rows": 3
        }
    )

    submit = SubmitField("Analyze My Profile & Generate Roadmap")


class ProfileSettingsForm(FlaskForm):
    """User account settings and career preferences form."""
    full_name = StringField(
        "Full Name",
        validators=[Optional(), Length(max=100)],
        render_kw={"placeholder": "e.g. Sarah Connor"}
    )
    target_role = StringField(
        "Target Dream Role",
        validators=[Optional(), Length(max=100)],
        render_kw={"placeholder": "e.g. Senior Machine Learning Engineer"}
    )
    experience_level = SelectField(
        "Experience Level",
        choices=[
            ("Student / Beginner", "Student / Beginner"),
            ("Junior Practitioner", "Junior Practitioner"),
            ("Mid-Level Professional", "Mid-Level Professional"),
            ("Senior / Lead", "Senior / Lead"),
            ("Executive / Architect", "Executive / Architect")
        ]
    )
    bio = TextAreaField(
        "Professional Bio",
        validators=[Optional(), Length(max=500)],
        render_kw={
            "placeholder": "Brief summary of your background, technical interests, and career ambitions.",
            "rows": 3
        }
    )
    submit = SubmitField("Save Profile Changes")
