# 🚀 CareerNova AI — AI Career Guidance Platform

> **Next-Generation Technical Career Navigation, Precision Skill-Gap Diagnostics, and Actionable Learning Roadmaps.**  
> Optimized natively for serverless deployment on **Vercel** with **Python 3.12+**, **Flask**, **SQLAlchemy**, and managed **PostgreSQL**.

[![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live%20Demo-brightgreen?style=for-the-badge&logo=github)](https://rohanverma69.github.io/careernova-ai/)
[![Vercel Deployment](https://img.shields.io/badge/Vercel-Full%20Stack%20Live-black?style=for-the-badge&logo=vercel)](https://careernova-ai.vercel.app)

### 🌐 Live Links
- **GitHub Pages (Direct Browser App)**: [https://rohanverma69.github.io/careernova-ai/](https://rohanverma69.github.io/careernova-ai/)
- **Vercel (Full-Stack Python + PostgreSQL)**: [https://careernova-ai.vercel.app](https://careernova-ai.vercel.app)

---

## 🌌 Platform Overview

**CareerNova AI** solves modern technical career ambiguity. Rather than relying on generic personality quizzes, CareerNova employs a **mathematically-grounded multi-factor alignment algorithm** paired with an **optional AI Executive Counseling layer (Google Gemini 1.5 Flash)**.

The platform analyzes a user's academic standing, technical competencies, problem-solving interests, and work-style preferences to calculate compatibility across **18+ modern technology tracks** (including AI & Machine Learning, Cloud & DevOps, Cybersecurity, Full-Stack Engineering, Data Science, and Technical Product Management).

### ✨ Key Features
- **Deterministic Multi-Factor Recommendation Engine**: Evaluates core technical skills (weighted 3.0x), secondary tools (weighted 1.5x), domain passion vectors, and work environments.
- **Skill-Gap Analysis & Hexagonal Radar**: Dynamic HTML5 Canvas radar chart visualizing profile readiness across 6 technical pillars without external JS dependencies.
- **Actionable 4-Phase Chronological Roadmaps**: Every career is segmented into:
  1. *Foundations*
  2. *Core Competencies*
  3. *Advanced Implementations*
  4. *Production Milestones & Capstone Projects*
- **Curated Learning Resources**: Direct access to verified courses, interactive sandboxes, and documentation (Fast.ai, The Odin Project, roadmap.sh, OWASP, etc.).
- **Dual Intelligence Architecture (Zero-Key Fallback)**: Operates at 100% functionality out-of-the-box using the deterministic rule engine. When an `AI_API_KEY` is supplied, it enriches outputs with live generative interview tips, market trends, and 90-day action plans.
- **Interactive User Dashboard & Kanban Tracker**: Pinned roadmaps, historical assessment archives, and a 3-column Kanban board (*To Learn*, *In Progress*, *Mastered*) with live status updates.
- **Premium SaaS Dark Navy Design System**: Midnight navy cosmic background (`#050811`), glowing purple/cyan gradients, backdrop-filter glassmorphism, floating ambient orbs, and full `prefers-reduced-motion` accessibility support.

---

## 🛠️ Tech Stack & Architecture

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Runtime** | Python 3.12+ | Configured via `.python-version` |
| **Web Framework** | Flask 3.1 | Modular blueprint architecture (`main`, `auth`, `assessment`, `dashboard`, `api`) |
| **Database ORM** | SQLAlchemy 2.0 / Flask-SQLAlchemy | Serverless-ready PostgreSQL engine pooling |
| **Authentication** | Flask-Login | Scrypt password hashing, session management |
| **Form Security** | Flask-WTF / WTForms | Server-side validation, CSRF tokens |
| **Database** | PostgreSQL | Neon.tech / Supabase / Vercel Postgres (SQLite local fallback) |
| **AI Integration** | Google Gemini REST API | Lightweight standard library integration with automatic heuristic fallback |
| **Frontend UI** | HTML5 / CSS3 / Vanilla JS | Custom Canvas radar chart, responsive drawer, ambient particles |
| **Deployment** | Vercel Serverless WSGI | Root `app.py` top-level export with `vercel.json` rewrites |

---

## 📂 Project Structure

```
Career Guidance/
├── .env.example              # Sample environment configuration template
├── .gitignore                # Git ignore rules for Python, virtualenv, databases
├── .python-version           # Vercel Python runtime pin (3.12)
├── vercel.json               # Serverless route rewrites
├── requirements.txt          # Production dependencies
├── README.md                 # Complete documentation & deployment guide
├── app.py                    # Root WSGI entry point, exports `app`
├── config.py                 # Configuration loader (PostgreSQL SSL, pool settings)
├── extensions.py             # Shared db, login_manager, csrf instances
├── models.py                 # User, Assessment, SavedCareer, SkillProgress models
├── forms.py                  # Secure Flask-WTF forms
├── init_db.py                # Safe database table initialization CLI
├── engine/
│   ├── careers_data.py       # Catalog of 18 structured modern tech careers
│   ├── recommender.py        # Rule-based multi-factor alignment & radar engine
│   └── ai_advisor.py         # Gemini API client with heuristic fallback
├── routes/
│   ├── main.py               # Landing page, career catalog, career details
│   ├── auth.py               # Registration, login, logout
│   ├── assessment.py         # Multi-step wizard, scoring, results rendering
│   ├── dashboard.py          # Dashboard overview, history, saved paths, profile
│   └── api.py                # Health check (/api/health), async skill & save endpoints
├── static/
│   ├── css/
│   │   ├── style.css         # SaaS dark navy glassmorphic design system
│   │   └── animations.css    # Ambient orbs, pulse glows, skeleton loaders
│   ├── js/
│   │   ├── main.js           # Navigation drawer, toast alerts, scroll observer
│   │   ├── orbs.js           # Background particle canvas (reduced-motion safe)
│   │   ├── wizard.js         # Multi-step assessment wizard controller
│   │   ├── charts.js         # Vanilla HTML5 Canvas radar chart & score animators
│   │   └── dashboard.js      # Asynchronous bookmarking and Kanban updates
│   └── images/
│       └── favicon.svg       # Geometric futuristic Nova AI logo icon
├── templates/                # Jinja2 layouts and views
└── tests/                    # Automated pytest suite (22 unit & integration tests)
```

---

## 💻 Local Development Setup

### 1. Clone & Set Up Virtual Environment
```bash
# Clone the repository
git clone https://github.com/your-username/careernova-ai.git
cd careernova-ai

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment Variables
Copy `.env.example` to create your local `.env`:
```bash
cp .env.example .env
```
*(By default, if `DATABASE_URL` is omitted, the app automatically initializes a local SQLite file `careernova.db` for zero-friction local development).*

### 3. Initialize Database Tables
```bash
python init_db.py
```

### 4. Run Development Server
```bash
python app.py
```
Open **`http://localhost:5000`** in your browser.

---

## 🧪 Running Automated Tests

Run the full automated test suite (22 passing unit and integration tests):
```bash
pytest -v
```
Tests cover:
- Route HTTP responses & error pages (404, 500)
- User registration, password hashing (Scrypt), login, and session guards
- Recommendation engine matching accuracy and radar dimension limits
- Assessment submissions (both guest and authenticated flows)
- Async API bookmarks (`/api/careers/toggle-save`) and skill progress updates
- Static asset availability (`style.css`, `animations.css`, `main.js`, `favicon.svg`)
- Zero-key AI advisor heuristic fallback generation

---

## ☁️ Vercel Production Deployment Guide

CareerNova AI is built specifically for **Vercel's Serverless Python Runtime**.

### Prerequisites
1. A **GitHub** account.
2. A free **Vercel** account ([vercel.com](https://vercel.com)).
3. A free managed **PostgreSQL** database (e.g., from [Neon.tech](https://neon.tech), [Supabase.com](https://supabase.com), or Vercel Postgres).

---

### Step 1: Set Up Managed PostgreSQL (Neon.tech Example)
1. Go to [Neon.tech](https://neon.tech) and create a free project.
2. Under **Connection Details**, copy your pooled connection string:
   ```text
   postgresql://alex:AbCdEf123456@ep-cool-fog-123456.us-east-2.aws.neon.tech/neondb?sslmode=require
   ```
3. Run `init_db.py` once with your production URL to create tables:
   ```bash
   # In terminal
   DATABASE_URL="your-neon-url-here" python init_db.py
   ```
   *(CareerNova also features a safe non-destructive automatic `db.create_all()` hook on cold start as an extra failsafe).*

---

### Step 2: Deploy to Vercel via GitHub Import (Recommended)

1. **Push your code to a GitHub repository**:
   ```bash
   git init
   git add .
   git commit -m "feat: initial commit of CareerNova AI"
   git branch -M main
   git remote add origin https://github.com/<your-username>/careernova-ai.git
   git push -u origin main
   ```

2. **Import into Vercel**:
   - Open your [Vercel Dashboard](https://vercel.com/dashboard).
   - Click **Add New...** → **Project**.
   - Select your `careernova-ai` repository and click **Import**.
   - **Framework Preset**: Select `Other` (or leave default).
   - **Root Directory**: `./` (leave default).

3. **Configure Environment Variables** in the Vercel Import Screen:
   Expand **Environment Variables** and add:

   | Key | Value | Description |
   | :--- | :--- | :--- |
   | `SECRET_KEY` | *(Generate via `python -c "import secrets; print(secrets.token_hex(32))"`)* | Session & CSRF encryption key |
   | `DATABASE_URL` | `postgresql://...neon.tech/neondb?sslmode=require` | Managed PostgreSQL connection string |
   | `FLASK_ENV` | `production` | Enables secure HTTPS cookies |
   | `AI_API_KEY` | *(Optional)* | Your Google Gemini API key |
   | `AI_PROVIDER` | `gemini` | AI provider choice |

4. **Click Deploy**:
   Vercel will automatically build the serverless package and deploy your application to a live `*.vercel.app` domain.

---

### Alternative: Deploy via Vercel CLI
```bash
# 1. Install Vercel CLI globally
npm install -g vercel

# 2. Login to Vercel
vercel login

# 3. Add environment secrets
vercel env add SECRET_KEY production
vercel env add DATABASE_URL production
vercel env add FLASK_ENV production

# 4. Deploy to production
vercel --prod
```

---

## 📋 Post-Deployment Smoke-Test Checklist

Once deployed to `https://<your-project>.vercel.app`, perform this quick verification:

- [ ] **1. Health Check Endpoint**:
  Visit `https://<your-project>.vercel.app/api/health`.
  Verify response is HTTP `200` with JSON:
  ```json
  {
    "database": "connected",
    "service": "CareerNova AI Guidance Engine",
    "status": "healthy",
    "version": "1.0.0"
  }
  ```
- [ ] **2. Static Assets Verification**:
  Open developer tools (F12) → Network tab.
  Verify that `/static/css/style.css`, `/static/css/animations.css`, `/static/js/main.js`, and `/static/images/favicon.svg` load with status `200` (no 404s).
- [ ] **3. User Registration & Authentication**:
  Navigate to `/register`, create a new account, verify you are redirected to the dashboard with a welcome flash message.
- [ ] **4. Career Assessment Execution**:
  Navigate to `/assessment`. Complete the 4-step wizard.
  Verify that the `/assessment/results/<id>` page loads with:
  - Circular match percentage score counter
  - Interactive HTML5 Canvas radar chart
  - Skill-gap analysis breakdown
  - AI Advisor action plan
  - 4-Phase Chronological Roadmap
- [ ] **5. Career Bookmarking & Kanban Skills Board**:
  Click "Save Career Path". Navigate to `/dashboard/saved` and `/dashboard/skills` to verify that saved careers appear and skills can be toggled to *In Progress* or *Mastered*.
- [ ] **6. Responsive & Reduced Motion Test**:
  Test on mobile viewport. Toggle `prefers-reduced-motion` in browser rendering settings to ensure animations gracefully deactivate.

---

## 🔒 Security Best Practices Implemented
- **No Secrets in Code or Client JS**: `SECRET_KEY`, `DATABASE_URL`, and `AI_API_KEY` are read exclusively from environment variables.
- **Serverless PostgreSQL Connection Pooling**: Uses `pool_pre_ping=True` and `pool_recycle=300` to prevent stale connection timeouts during serverless function reuse.
- **CSRF Token Protection**: Every state-changing form and asynchronous API call requires a validated CSRF token.
- **Scrypt Password Hashing**: Passwords hashed securely using Werkzeug's `scrypt` implementation.
- **HTTPS-Only Cookies**: In production, `SESSION_COOKIE_SECURE=True`, `SESSION_COOKIE_HTTPONLY=True`, and `SESSION_COOKIE_SAMESITE='Lax'` are strictly enforced.
- **Zero Local Disk Reliance**: No user-uploaded files or persistent state written to local disk.

---

## 📄 License
MIT License. Built for developers, students, and technology professionals worldwide.
