"""
Comprehensive Career Catalog for CareerNova AI.
Contains 18 structured, future-proof modern careers across tech, AI, design, product,
cybersecurity, and data with skills, salary ranges, learning roadmaps, and resources.
"""

CAREERS_DATABASE = {
    "ai_ml_engineer": {
        "key": "ai_ml_engineer",
        "title": "AI & Machine Learning Engineer",
        "category": "Artificial Intelligence & Data",
        "badge": "Trending & High Demand",
        "icon": "brain",
        "tagline": "Architect intelligent neural networks, foundation models, and scalable AI systems.",
        "description": "AI & Machine Learning Engineers build predictive models, fine-tune Large Language Models (LLMs), and deploy deep learning pipelines into high-throughput production environments. They bridge the gap between theoretical data science and enterprise software engineering.",
        "salary_range": {"entry": "$105,000", "median": "$162,000", "senior": "$235,000+"},
        "growth_rate": "+32% through 2032 (Much faster than average)",
        "work_styles": ["Analytical & Research-heavy", "Experimental", "Remote / Hybrid", "Deep Focus"],
        "education_recommended": ["Bachelor's / Master's in CS, Math, Data Science, or self-taught portfolio"],
        "core_skills": [
            "Python", "Machine Learning", "PyTorch", "TensorFlow", "Math & Statistics",
            "Deep Learning", "Data Structures"
        ],
        "secondary_skills": [
            "Docker", "MLOps", "Git", "SQL", "Cloud Platforms (AWS/GCP)", "NLP", "Computer Vision", "FastAPI"
        ],
        "soft_skills": [
            "Problem Solving", "Mathematical Intuition", "Continuous Learning", "Research Communication"
        ],
        "interests": [
            "Artificial Intelligence", "Neural Networks", "Automation", "Math & Algorithms", "Pattern Discovery"
        ],
        "roles": [
            "Machine Learning Engineer", "AI Applied Scientist", "LLM Applications Engineer",
            "MLOps Engineer", "Algorithm Specialist"
        ],
        "roadmap": [
            {
                "phase": "Phase 1: Foundations",
                "timeframe": "Months 1-2",
                "skills": ["Python 3", "Linear Algebra", "Calculus", "NumPy", "Pandas"],
                "project": "Build an exploratory data analysis & regression model on a Kaggle dataset."
            },
            {
                "phase": "Phase 2: Classical Machine Learning",
                "timeframe": "Months 3-4",
                "skills": ["Scikit-Learn", "Feature Engineering", "Model Evaluation", "SQL", "Git"],
                "project": "End-to-end customer churn prediction system with cross-validation."
            },
            {
                "phase": "Phase 3: Deep Learning & Transformers",
                "timeframe": "Months 5-6",
                "skills": ["PyTorch", "CNNs", "Transformers / Hugging Face", "Vector DBs (Chroma/Pinecone)"],
                "project": "Build a domain-specific RAG (Retrieval-Augmented Generation) assistant."
            },
            {
                "phase": "Phase 4: MLOps & Production Deployment",
                "timeframe": "Months 7-8",
                "skills": ["MLflow", "Docker", "FastAPI", "AWS SageMaker", "Monitoring & Drift Detection"],
                "project": "Deploy an auto-scaling ML microservice with CI/CD and latency benchmarking."
            }
        ],
        "resources": [
            {"title": "Fast.ai: Practical Deep Learning for Coders", "type": "Interactive Course", "url": "https://course.fast.ai", "free": True},
            {"title": "DeepLearning.AI: Machine Learning Specialization", "type": "Course", "url": "https://www.deeplearning.ai", "free": False},
            {"title": "Hugging Face Deep Learning & NLP Course", "type": "Tutorials & Docs", "url": "https://huggingface.co/learn", "free": True},
            {"title": "CS229: Machine Learning by Stanford University", "type": "Lecture Series", "url": "https://cs229.stanford.edu", "free": True}
        ]
    },

    "full_stack_dev": {
        "key": "full_stack_dev",
        "title": "Full-Stack Web Developer",
        "category": "Software Engineering",
        "badge": "High Demand",
        "icon": "code",
        "tagline": "Craft end-to-end web applications from responsive frontends to scalable backends.",
        "description": "Full-Stack Developers create complete digital experiences. They architect databases, build secure server-side APIs, implement modern UI components, and deploy cloud-native software used by millions.",
        "salary_range": {"entry": "$82,000", "median": "$128,000", "senior": "$185,000+"},
        "growth_rate": "+25% through 2032 (High growth)",
        "work_styles": ["Collaborative", "Fast-paced & Shipping-focused", "Remote / Hybrid", "Creative"],
        "education_recommended": ["Any degree, Bootcamp graduate, or demonstrable open-source portfolio"],
        "core_skills": [
            "JavaScript / TypeScript", "Python", "React", "Node.js", "HTML5 & CSS3", "SQL", "Git"
        ],
        "secondary_skills": [
            "Next.js", "Flask / FastAPI", "PostgreSQL", "Docker", "REST & GraphQL APIs", "Tailwind CSS", "Redis"
        ],
        "soft_skills": [
            "Product Sense", "Cross-team Communication", "Debugging Tenacity", "Attention to Detail"
        ],
        "interests": [
            "Web Development", "Building Products", "UI Design", "Open Source", "Software Architecture"
        ],
        "roles": [
            "Full-Stack Software Engineer", "Frontend Architect", "Backend Systems Engineer",
            "Technical Lead", "Startup Founding Engineer"
        ],
        "roadmap": [
            {
                "phase": "Phase 1: Web Fundamentals",
                "timeframe": "Months 1-2",
                "skills": ["HTML5 Semantic Markup", "Modern CSS & Flexbox/Grid", "Modern JavaScript (ES6+)", "Git & GitHub"],
                "project": "Build an interactive responsive dashboard with vanilla JS and glassmorphism styling."
            },
            {
                "phase": "Phase 2: Modern Frontend & State",
                "timeframe": "Months 3-4",
                "skills": ["React / Next.js", "TypeScript", "Tailwind CSS", "Client State Management"],
                "project": "Create a rich collaborative Kanban task management application."
            },
            {
                "phase": "Phase 3: Robust Backend & Databases",
                "timeframe": "Months 5-6",
                "skills": ["Node.js or Python (Flask/FastAPI)", "PostgreSQL", "ORM & Schema Migrations", "JWT & Auth"],
                "project": "Build a secure multi-tenant SaaS REST API with payment gateway webhook integration."
            },
            {
                "phase": "Phase 4: Production & DevOps",
                "timeframe": "Months 7-8",
                "skills": ["Docker", "Vercel / AWS", "Redis Caching", "CI/CD Actions", "Web Security & OWASP"],
                "project": "Deploy and load-test a production-ready SaaS application with automated tests."
            }
        ],
        "resources": [
            {"title": "The Odin Project - Full Stack Curriculum", "type": "Interactive Curriculum", "url": "https://www.theodinproject.com", "free": True},
            {"title": "Full Stack Open (University of Helsinki)", "type": "Course", "url": "https://fullstackopen.com", "free": True},
            {"title": "MDN Web Docs", "type": "Official Reference", "url": "https://developer.mozilla.org", "free": True},
            {"title": "Frontend Masters: Complete Intro to Web Dev", "type": "Video Series", "url": "https://frontendmasters.com", "free": False}
        ]
    },

    "cloud_devops_architect": {
        "key": "cloud_devops_architect",
        "title": "Cloud & DevOps Architect",
        "category": "Cloud & Infrastructure",
        "badge": "Critical Infrastructure",
        "icon": "cloud",
        "tagline": "Automate infrastructure, scale resilient Kubernetes clusters, and power CI/CD delivery.",
        "description": "Cloud & DevOps Architects design highly available, fault-tolerant cloud infrastructures. They eliminate manual operations through Infrastructure as Code (IaC), implement security guardrails, and streamline software delivery pipelines.",
        "salary_range": {"entry": "$98,000", "median": "$150,000", "senior": "$215,000+"},
        "growth_rate": "+27% through 2032 (Very high demand)",
        "work_styles": ["Systematic", "High-Reliability Mindset", "Remote / Hybrid", "Collaborative"],
        "education_recommended": ["CS degree, IT/Networking background, or Cloud Certifications"],
        "core_skills": [
            "Linux / Bash", "Docker", "Kubernetes", "AWS / GCP / Azure", "Terraform", "CI/CD (GitHub Actions)"
        ],
        "secondary_skills": [
            "Python / Go", "Prometheus & Grafana", "Networking (DNS, VPC, CIDR)", "Ansible", "Cloud Security", "Helm"
        ],
        "soft_skills": [
            "Incident Management", "Root Cause Analysis", "Disaster Planning", "Automation Mindset"
        ],
        "interests": [
            "Cloud Infrastructure", "Automation & Scripting", "System Reliability", "Scalability", "DevOps"
        ],
        "roles": [
            "DevOps Engineer", "Cloud Architect", "Platform Engineer",
            "Infrastructure Engineer", "Release Manager"
        ],
        "roadmap": [
            {
                "phase": "Phase 1: Linux & Networking Mastery",
                "timeframe": "Months 1-2",
                "skills": ["Linux SysAdmin", "Bash Scripting", "TCP/IP, DNS, SSL/TLS", "Git Branching Workflows"],
                "project": "Configure a hardened Linux server running reverse proxy Nginx with auto SSL."
            },
            {
                "phase": "Phase 2: Containers & Orchestration",
                "timeframe": "Months 3-4",
                "skills": ["Docker Multi-stage Builds", "Docker Compose", "Kubernetes Pods & Services", "Helm"],
                "project": "Containerize a microservice stack and deploy to a local Minikube/k3s cluster."
            },
            {
                "phase": "Phase 3: Infrastructure as Code & Cloud",
                "timeframe": "Months 5-6",
                "skills": ["Terraform", "AWS (EC2, S3, RDS, IAM, VPC)", "GitHub Actions CI/CD", "Secret Management"],
                "project": "Provision an automated AWS VPC and deploy a web application via Terraform & GitHub Actions."
            },
            {
                "phase": "Phase 4: Observability & Cloud Architecture",
                "timeframe": "Months 7-8",
                "skills": ["Prometheus", "Grafana", "OpenTelemetry", "Cost Optimization", "Chaos Engineering"],
                "project": "Set up a centralized monitoring dashboard with alert manager and SLA monitoring."
            }
        ],
        "resources": [
            {"title": "DevOps Roadmap (roadmap.sh)", "type": "Interactive Roadmap", "url": "https://roadmap.sh/devops", "free": True},
            {"title": "KodeKloud: Certified Kubernetes Administrator (CKA)", "type": "Interactive Labs", "url": "https://kodekloud.com", "free": False},
            {"title": "AWS Skill Builder: Cloud Practitioner & Solutions Architect", "type": "Official Training", "url": "https://skillbuilder.aws", "free": True},
            {"title": "Learn Terraform (HashiCorp Tutorials)", "type": "Documentation", "url": "https://developer.hashicorp.com/terraform/tutorials", "free": True}
        ]
    },

    "cybersecurity_engineer": {
        "key": "cybersecurity_engineer",
        "title": "Cybersecurity Specialist & Ethical Hacker",
        "category": "Security & Defense",
        "badge": "Top Security Priority",
        "icon": "shield",
        "tagline": "Protect digital ecosystems, identify critical vulnerabilities, and neutralize cyber threats.",
        "description": "Cybersecurity Specialists defend digital assets against malicious actors. They perform penetration tests, audit cloud systems, design zero-trust architectures, and respond rapidly to emerging security incidents.",
        "salary_range": {"entry": "$92,000", "median": "$142,000", "senior": "$210,000+"},
        "growth_rate": "+35% through 2032 (Fastest growing sector)",
        "work_styles": ["Investigative", "Vigilant", "Methodical", "High-Stakes Problem Solving"],
        "education_recommended": ["CS, Cybersecurity degree, or Security certifications (CompTIA Security+, CEH, OSCP)"],
        "core_skills": [
            "Network Security", "Ethical Hacking / Pen Testing", "Linux", "Python / Bash", "SIEM & Threat Analysis", "OWASP Top 10"
        ],
        "secondary_skills": [
            "Cryptography", "Wireshark & Burp Suite", "Cloud Security (AWS/Azure)", "Reverse Engineering", "Incident Response"
        ],
        "soft_skills": [
            "Ethical Integrity", "Adversarial Thinking", "Detailed Documentation", "Crisis Communication"
        ],
        "interests": [
            "Cybersecurity", "Penetration Testing", "Cryptography", "Forensics", "Defensive Operations"
        ],
        "roles": [
            "Cybersecurity Analyst", "Penetration Tester", "Security Operations Center (SOC) Analyst",
            "Information Security Officer", "AppSec Specialist"
        ],
        "roadmap": [
            {
                "phase": "Phase 1: IT & Network Foundations",
                "timeframe": "Months 1-2",
                "skills": ["OSI Model", "TCP/IP & Packet Analysis (Wireshark)", "Linux Command Line", "Windows Internals"],
                "project": "Build an isolated virtual home lab with pfSense router and analyze attack traffic."
            },
            {
                "phase": "Phase 2: Defensive Security & SIEM",
                "timeframe": "Months 3-4",
                "skills": ["Security Hardening", "Snort / Suricata IDS", "Splunk / ELK SIEM", "Access Controls"],
                "project": "Deploy an ELK SIEM stack and build custom detection rules for brute force attempts."
            },
            {
                "phase": "Phase 3: Offensive Security & Vulnerability Assessment",
                "timeframe": "Months 5-6",
                "skills": ["Burp Suite", "OWASP Top 10 Exploitation", "Metasploit", "Nmap", "Privilege Escalation"],
                "project": "Perform a complete white-box penetration audit on Juice Shop or DVWA."
            },
            {
                "phase": "Phase 4: Cloud Security & Certifications",
                "timeframe": "Months 7-8",
                "skills": ["AWS Security (GuardDuty, IAM)", "Zero-Trust Architecture", "Incident Playbooks", "OSCP Prep"],
                "project": "Conduct an automated cloud infrastructure audit and present an executive risk report."
            }
        ],
        "resources": [
            {"title": "TryHackMe: Hands-on Cyber Security Training", "type": "Interactive Labs", "url": "https://tryhackme.com", "free": True},
            {"title": "Hack The Box Academy", "type": "Interactive Labs", "url": "https://academy.hackthebox.com", "free": True},
            {"title": "OWASP Official Documentation & Cheatsheets", "type": "Security Standards", "url": "https://owasp.org", "free": True},
            {"title": "Professor Messer Security+ Training Course", "type": "Video Course", "url": "https://www.professormesser.com", "free": True}
        ]
    },

    "data_scientist": {
        "key": "data_scientist",
        "title": "Data Scientist & Analytics Lead",
        "category": "Artificial Intelligence & Data",
        "badge": "High Demand",
        "icon": "chart-pie",
        "tagline": "Turn messy big data into strategic business breakthroughs and predictive intelligence.",
        "description": "Data Scientists uncover hidden trends, conduct rigorous statistical tests, and train machine learning models to solve complex strategic problems. They present actionable insights to executive leadership.",
        "salary_range": {"entry": "$90,000", "median": "$140,000", "senior": "$200,000+"},
        "growth_rate": "+35% through 2032 (Explosive growth)",
        "work_styles": ["Analytical", "Hypothesis-Driven", "Storytelling with Data", "Cross-functional"],
        "education_recommended": ["Degree in Statistics, CS, Economics, Math, or relevant data experience"],
        "core_skills": [
            "Python", "SQL", "Statistics & Probability", "Machine Learning", "Data Visualization", "Pandas & NumPy"
        ],
        "secondary_skills": [
            "R", "Tableau / PowerBI", "Scikit-Learn", "A/B Testing", "BigQuery / Snowflake", "Time Series Forecasting"
        ],
        "soft_skills": [
            "Executive Storytelling", "Critical Thinking", "Business Acumen", "Curiosity"
        ],
        "interests": [
            "Data Analysis", "Predictive Modeling", "Statistics", "Business Strategy", "Visualization"
        ],
        "roles": [
            "Data Scientist", "Lead Quantitative Analyst", "Decision Scientist",
            "Marketing Data Scientist", "People Analytics Lead"
        ],
        "roadmap": [
            {
                "phase": "Phase 1: Data Wrangling & SQL",
                "timeframe": "Months 1-2",
                "skills": ["Advanced SQL (Window functions, CTEs)", "Python (Pandas, NumPy)", "Data Cleaning", "Matplotlib / Seaborn"],
                "project": "Clean and explore an e-commerce transactional dataset with 1M+ rows."
            },
            {
                "phase": "Phase 2: Statistical Rigor & A/B Testing",
                "timeframe": "Months 3-4",
                "skills": ["Hypothesis Testing", "Confidence Intervals", "A/B Test Design", "Regression Analysis"],
                "project": "Design, simulate, and analyze an end-to-end A/B test with statistical significance testing."
            },
            {
                "phase": "Phase 3: Machine Learning & Modeling",
                "timeframe": "Months 5-6",
                "skills": ["Supervised & Unsupervised Learning", "Tree-based Models (XGBoost)", "Clustering", "Feature Importance"],
                "project": "Build a customer lifetime value (LTV) predictive model with hyperparameter tuning."
            },
            {
                "phase": "Phase 4: Production Insights & BI",
                "timeframe": "Months 7-8",
                "skills": ["Interactive Dashboards (Streamlit/Tableau)", "Snowflake/BigQuery", "Model Explainability (SHAP)"],
                "project": "Deploy an interactive executive intelligence portal with dynamic scenario forecasting."
            }
        ],
        "resources": [
            {"title": "Kaggle Learn: Free Micro-Courses in Data Science", "type": "Interactive Tutorials", "url": "https://www.kaggle.com/learn", "free": True},
            {"title": "StatQuest with Josh Starmer", "type": "Visual Math & Stats", "url": "https://statquest.org", "free": True},
            {"title": "Mode Analytics SQL Tutorial for Data Analysis", "type": "Hands-on SQL", "url": "https://mode.com/sql-tutorial", "free": True},
            {"title": "Coursera: Applied Data Science with Python (UMich)", "type": "Specialization", "url": "https://www.coursera.org", "free": False}
        ]
    },

    "ui_ux_designer": {
        "key": "ui_ux_designer",
        "title": "UI/UX & Product Designer",
        "category": "Design & User Experience",
        "badge": "Creative & Technical",
        "icon": "palette",
        "tagline": "Design intuitive user journeys, high-fidelity design systems, and delightful digital apps.",
        "description": "UI/UX Designers define how digital software looks, feels, and operates. They run user interviews, craft wireframes and design systems in Figma, and partner with developers to build accessible, high-converting interfaces.",
        "salary_range": {"entry": "$75,000", "median": "$115,000", "senior": "$170,000+"},
        "growth_rate": "+16% through 2032 (Steady demand for quality design)",
        "work_styles": ["Empathetic", "Visual & Creative", "Iterative", "Collaborative"],
        "education_recommended": ["Design degree, HCI, or strong portfolio showing problem-solving process"],
        "core_skills": [
            "Figma", "User Research & Usability Testing", "Wireframing & Prototyping", "Design Systems", "UI Visual Design"
        ],
        "secondary_skills": [
            "HTML & CSS basics", "Information Architecture", "Micro-interactions", "Accessibility (WCAG)", "Design Tokens"
        ],
        "soft_skills": [
            "Empathy", "Visual Communication", "Critique Receptivity", "Stakeholder Alignment"
        ],
        "interests": [
            "UI Design", "User Psychology", "Product Aesthetics", "Typography & Color Theory", "Accessibility"
        ],
        "roles": [
            "Product Designer", "UI/UX Designer", "Design Systems Engineer",
            "UX Researcher", "Interaction Designer"
        ],
        "roadmap": [
            {
                "phase": "Phase 1: Design Fundamentals & Figma",
                "timeframe": "Months 1-2",
                "skills": ["Figma Auto-layout & Components", "Color Theory & Typography", "Visual Hierarchy", "Heuristic Evaluation"],
                "project": "Redesign a complex checkout flow in Figma with responsive component variants."
            },
            {
                "phase": "Phase 2: User Research & Wireframing",
                "timeframe": "Months 3-4",
                "skills": ["User Personas", "Journey Mapping", "Low-fi Wireframes", "Information Architecture"],
                "project": "Conduct 5 user interviews and map out a comprehensive user onboarding journey."
            },
            {
                "phase": "Phase 3: Design Systems & Advanced Prototyping",
                "timeframe": "Months 5-6",
                "skills": ["Token-based Design Systems", "Interactive Figma Prototyping", "Micro-interactions", "WCAG 2.1 AA"],
                "project": "Build an enterprise multi-brand design system with documentation."
            },
            {
                "phase": "Phase 4: Portfolio & Dev Handoff",
                "timeframe": "Months 7-8",
                "skills": ["Design Tokens Handoff", "Case Study Writing", "Portfolio Review", "Live Usability Testing"],
                "project": "Publish a 3-case-study product design portfolio ready for senior interviews."
            }
        ],
        "resources": [
            {"title": "Figma Community & Official Tutorials", "type": "Interactive Guides", "url": "https://help.figma.com", "free": True},
            {"title": "Refactoring UI by Adam Wathan & Steve Schoger", "type": "Book & Guide", "url": "https://www.refactoringui.com", "free": False},
            {"title": "Nielsen Norman Group UX Articles", "type": "UX Research Standard", "url": "https://www.nngroup.com", "free": True},
            {"title": "Laws of UX by Jon Yablonski", "type": "Interactive Principles", "url": "https://lawsofux.com", "free": True}
        ]
    },

    "mobile_developer": {
        "key": "mobile_developer",
        "title": "Mobile App Developer (iOS & Android)",
        "category": "Software Engineering",
        "badge": "High Demand",
        "icon": "smartphone",
        "tagline": "Build fluid, native mobile applications for billions of smartphone users worldwide.",
        "description": "Mobile Developers engineer fast, responsive, battery-efficient mobile applications. They leverage Flutter, React Native, Swift, or Kotlin to deliver seamless native mobile experiences with offline caching and biometric security.",
        "salary_range": {"entry": "$85,000", "median": "$132,000", "senior": "$185,000+"},
        "growth_rate": "+23% through 2032 (Consistent mobile consumption)",
        "work_styles": ["Detail-Oriented", "Performance-Obsessed", "Iterative", "Autonomous"],
        "education_recommended": ["CS degree or hands-on published apps in App Store / Google Play"],
        "core_skills": [
            "Flutter / React Native", "Swift / Kotlin", "Mobile UI State Management", "REST APIs", "Git", "Mobile Performance"
        ],
        "secondary_skills": [
            "App Store & Play Store Deployment", "Offline SQLite / Realm", "Push Notifications", "Biometrics Auth", "CI/CD (Fastlane)"
        ],
        "soft_skills": [
            "User Centricity", "Device Fragmentation Patience", "Clean Code Architecture", "Collaboration"
        ],
        "interests": [
            "Mobile Apps", "Cross-Platform Development", "Native Hardware APIs", "Fluid Gestures", "App Ecosystems"
        ],
        "roles": [
            "iOS Engineer", "Android Engineer", "Cross-Platform Flutter Lead",
            "Mobile Architect", "React Native Developer"
        ],
        "roadmap": [
            {
                "phase": "Phase 1: Mobile UI & Language Basics",
                "timeframe": "Months 1-2",
                "skills": ["Dart/Flutter or Swift/SwiftUI", "Mobile Layouts & Widgets", "Navigation & Routing", "Local Assets"],
                "project": "Build an offline-first habits tracker with smooth gestures and animations."
            },
            {
                "phase": "Phase 2: State Management & Remote APIs",
                "timeframe": "Months 3-4",
                "skills": ["Bloc / Riverpod / Redux", "REST & GraphQL Client", "JSON Parsing", "Offline Caching"],
                "project": "Develop a real-time crypto & stock market tracker app with persistent watchlists."
            },
            {
                "phase": "Phase 3: Device Features & Security",
                "timeframe": "Months 5-6",
                "skills": ["Camera & Geolocation", "Biometric Authentication", "Push Notifications (FCM)", "Deep Links"],
                "project": "Create a geolocation-based fitness check-in app with push alerts."
            },
            {
                "phase": "Phase 4: CI/CD & App Store Release",
                "timeframe": "Months 7-8",
                "skills": ["Fastlane Automation", "App Store Guidelines & Review", "Crashlytics & Telemetry", "In-App Purchases"],
                "project": "Publish a live application to TestFlight and Google Play Open Testing."
            }
        ],
        "resources": [
            {"title": "Official Flutter Documentation & Codelabs", "type": "Interactive Guides", "url": "https://docs.flutter.dev", "free": True},
            {"title": "100 Days of SwiftUI by Paul Hudson", "type": "Complete Course", "url": "https://www.hackingwithswift.com/100/swiftui", "free": True},
            {"title": "Android Basics with Compose (Google)", "type": "Official Training", "url": "https://developer.android.com/courses", "free": True},
            {"title": "React Native Docs", "type": "Documentation", "url": "https://reactnative.dev", "free": True}
        ]
    },

    "product_manager": {
        "key": "product_manager",
        "title": "Technical Product Manager",
        "category": "Product & Strategy",
        "badge": "Leadership Track",
        "icon": "compass",
        "tagline": "Unite engineering, design, and business strategy to deliver high-impact digital products.",
        "description": "Technical Product Managers lead cross-functional teams to discover and build software that customers love. They define product roadmaps, prioritize engineering backlogs, run user discovery sprints, and measure KPI outcomes.",
        "salary_range": {"entry": "$95,000", "median": "$148,000", "senior": "$210,000+"},
        "growth_rate": "+20% through 2032 (High leadership demand)",
        "work_styles": ["Strategic", "Executive Communicator", "Data-Informed", "Organized"],
        "education_recommended": ["CS, Business, Engineering, or demonstrable product delivery track record"],
        "core_skills": [
            "Product Roadmap Strategy", "Agile / Scrum Methodologies", "User Discovery & Interviews",
            "PRD Writing", "KPI & Product Analytics"
        ],
        "secondary_skills": [
            "Basic SQL", "Wireframing (Figma / Miro)", "Go-to-Market (GTM) Strategy", "A/B Testing", "API Literacy"
        ],
        "soft_skills": [
            "Strategic Vision", "Conflict Resolution", "Decisiveness", "Empathetic Leadership", "Prioritization"
        ],
        "interests": [
            "Product Strategy", "User Psychology", "Business Models", "Market Trends", "Team Facilitation"
        ],
        "roles": [
            "Associate Product Manager (APM)", "Technical Product Manager", "Group Product Manager",
            "Director of Product", "Chief Product Officer (CPO)"
        ],
        "roadmap": [
            {
                "phase": "Phase 1: Product Discovery & User Needs",
                "timeframe": "Months 1-2",
                "skills": ["User Journey Mapping", "Customer Discovery Interviews", "Opportunity Solution Trees", "Competitive Analysis"],
                "project": "Conduct 10 user interviews on an existing SaaS friction point and present key findings."
            },
            {
                "phase": "Phase 2: Product Specs & Engineering Collaboration",
                "timeframe": "Months 3-4",
                "skills": ["Writing Detailed PRDs", "User Stories & Acceptance Criteria", "Jira / Linear Backlog Grooming", "API Flows"],
                "project": "Write a full technical PRD for an AI-powered onboarding feature."
            },
            {
                "phase": "Phase 3: Metrics, Analytics & Experimentation",
                "timeframe": "Months 5-6",
                "skills": ["North Star Metrics", "Cohort Retention Analysis", "Mixpanel / Amplitude", "A/B Experimentation"],
                "project": "Build an interactive funnel analysis and prioritize 3 conversion rate optimization experiments."
            },
            {
                "phase": "Phase 4: Go-to-Market & Executive Strategy",
                "timeframe": "Months 7-8",
                "skills": ["GTM Launch Playbooks", "Pricing Strategy", "Stakeholder Alignment", "Executive Presentations"],
                "project": "Develop a comprehensive 12-month product vision and roadmap deck."
            }
        ],
        "resources": [
            {"title": "Inspired: How to Create Tech Products Customers Love by Marty Cagan", "type": "Book", "url": "https://www.svpg.com/books", "free": False},
            {"title": "Lenny's Newsletter & Podcast", "type": "Industry Standard", "url": "https://www.lennysnewsletter.com", "free": True},
            {"title": "Reforge Product Strategy Series", "type": "Executive Training", "url": "https://www.reforge.com", "free": False},
            {"title": "Product School Resources & Templates", "type": "Templates & Guides", "url": "https://productschool.com", "free": True}
        ]
    },

    "data_engineer": {
        "key": "data_engineer",
        "title": "Data Engineer & Big Data Architect",
        "category": "Artificial Intelligence & Data",
        "badge": "High Demand",
        "icon": "database",
        "tagline": "Build reliable data pipelines, data warehouses, and streaming infrastructure.",
        "description": "Data Engineers construct robust data pipelines that extract, transform, and load petabytes of enterprise data. They ensure analytics engines, ML models, and business dashboards have accurate, low-latency data.",
        "salary_range": {"entry": "$95,000", "median": "$145,000", "senior": "$205,000+"},
        "growth_rate": "+30% through 2032 (Crucial foundational role)",
        "work_styles": ["Architectural", "Process-Oriented", "Reliability Mindset", "Deep Problem Solving"],
        "education_recommended": ["CS, Software Engineering, or Database administration background"],
        "core_skills": [
            "SQL Mastery", "Python", "Apache Spark / PySpark", "Data Modeling (Dimensional)", "Airflow / Prefect", "Snowflake / BigQuery"
        ],
        "secondary_skills": [
            "Kafka Streaming", "dbt (data build tool)", "Docker", "AWS S3 / Glue", "Data Quality & Testing", "PostgreSQL"
        ],
        "soft_skills": [
            "Architectural Foresight", "Data Integrity Passion", "Patience with Edge Cases", "Cross-team Support"
        ],
        "interests": [
            "Data Pipelines", "Big Data", "Distributed Computing", "Database Optimization", "Data Warehousing"
        ],
        "roles": [
            "Data Engineer", "Big Data Architect", "Analytics Engineer",
            "ETL Developer", "Data Platform Specialist"
        ],
        "roadmap": [
            {
                "phase": "Phase 1: Advanced SQL & Data Modeling",
                "timeframe": "Months 1-2",
                "skills": ["Kimball Star Schema", "Slowly Changing Dimensions (SCD)", "Window Functions", "PostgreSQL Optimization"],
                "project": "Design and normalize a multi-table analytical schema for a financial ledger."
            },
            {
                "phase": "Phase 2: Modern Transformation with dbt & Python",
                "timeframe": "Months 3-4",
                "skills": ["dbt Core", "Automated Data Testing", "Python Pipeline Scripts", "Parquet & S3 Storage"],
                "project": "Build an automated dbt modeling pipeline with documentation and tests."
            },
            {
                "phase": "Phase 3: Orchestration & Distributed Big Data",
                "timeframe": "Months 5-6",
                "skills": ["Apache Airflow DAGs", "PySpark", "Snowflake / BigQuery", "Delta Lake / Iceberg"],
                "project": "Build an Airflow DAG that processes 10M rows daily using PySpark."
            },
            {
                "phase": "Phase 4: Streaming & Data Governance",
                "timeframe": "Months 7-8",
                "skills": ["Kafka / Flink Streaming", "Data Lineage & Catalogs", "Great Expectations", "Cost Governance"],
                "project": "Implement an end-to-end event streaming architecture with real-time alerting."
            }
        ],
        "resources": [
            {"title": "Data Engineering Zoomcamp (Free)", "type": "Complete Bootcamp", "url": "https://github.com/DataTalksClub/data-engineering-zoomcamp", "free": True},
            {"title": "Fundamentals of Data Engineering by Joe Reis & Matt Housley", "type": "Book", "url": "https://www.oreilly.com", "free": False},
            {"title": "dbt Learn Free Courses", "type": "Interactive Labs", "url": "https://courses.getdbt.com", "free": True},
            {"title": "The Data Engineering Cookbook", "type": "Open Source Guide", "url": "https://github.com/andkret/Cookbook", "free": True}
        ]
    },

    "sre_engineer": {
        "key": "sre_engineer",
        "title": "Site Reliability Engineer (SRE)",
        "category": "Cloud & Infrastructure",
        "badge": "High Compensation",
        "icon": "server",
        "tagline": "Apply software engineering principles to infrastructure and maintain 99.999% uptime.",
        "description": "Site Reliability Engineers apply software engineering disciplines to operations. They define Service Level Objectives (SLOs), automate away operational toil, run chaos experiments, and build resilient auto-healing systems.",
        "salary_range": {"entry": "$102,000", "median": "$158,000", "senior": "$225,000+"},
        "growth_rate": "+24% through 2032 (Mission-critical in tech)",
        "work_styles": ["Calm Under Pressure", "Systems Thinker", "Analytical", "Automation-Driven"],
        "education_recommended": ["CS, Systems Engineering, or Senior Backend/DevOps background"],
        "core_skills": [
            "Linux Internals", "Go or Python", "Kubernetes", "Observability (Prometheus/Grafana)", "SLI/SLO Frameworks"
        ],
        "secondary_skills": [
            "Distributed Systems", "Incident Management", "Terraform", "Chaos Engineering", "gRPC & Networking", "eBPF"
        ],
        "soft_skills": [
            "Blameless Postmortem Facilitation", "Crisis Calmness", "Rigorous Documentation", "Automation First"
        ],
        "interests": [
            "System Reliability", "Uptime & High Availability", "Distributed Systems", "Automation", "Observability"
        ],
        "roles": [
            "Site Reliability Engineer", "Production Systems Lead", "Reliability Architect",
            "Performance Engineer", "Infrastructure Developer"
        ],
        "roadmap": [
            {
                "phase": "Phase 1: Deep Linux & Network Debugging",
                "timeframe": "Months 1-2",
                "skills": ["Linux kernel parameters", "strace, tcpdump, perf", "Systemd internals", "DNS troubleshooting"],
                "project": "Diagnose simulated high-latency Linux bottlenecks and profile CPU/memory spikes."
            },
            {
                "phase": "Phase 2: SRE Culture & Error Budgets",
                "timeframe": "Months 3-4",
                "skills": ["SLIs, SLOs, and SLAs", "Error Budgets calculation", "Blameless Post-Mortems", "Alerting fatigue reduction"],
                "project": "Draft an enterprise reliability contract and automated alert escalation policy."
            },
            {
                "phase": "Phase 3: High-Scale Orchestration & Automation",
                "timeframe": "Months 5-6",
                "skills": ["Kubernetes Operators in Go", "Service Mesh (Istio)", "Prometheus PromQL", "Distributed Tracing"],
                "project": "Write a custom Kubernetes controller in Go that enforces autoscaling based on custom latency metrics."
            },
            {
                "phase": "Phase 4: Chaos Engineering & Disaster Recovery",
                "timeframe": "Months 7-8",
                "skills": ["Chaos Mesh / LitmusChaos", "Multi-region Failover", "Load Testing with k6", "Capacity Planning"],
                "project": "Run controlled pod failure simulations and verify zero-downtime automated failover."
            }
        ],
        "resources": [
            {"title": "Google Site Reliability Engineering Books (Free)", "type": "Official Google Standard", "url": "https://sre.google/books", "free": True},
            {"title": "Brendan Gregg's Systems Performance Guide", "type": "Technical Resource", "url": "https://www.brendangregg.com", "free": True},
            {"title": "Prometheus Monitoring Documentation", "type": "Docs & Tutorials", "url": "https://prometheus.io/docs", "free": True},
            {"title": "SRE Weekly Newsletter", "type": "Industry News", "url": "https://sreweekly.com", "free": True}
        ]
    },

    "bi_analyst": {
        "key": "bi_analyst",
        "title": "Business Intelligence (BI) Analyst",
        "category": "Artificial Intelligence & Data",
        "badge": "High Business Impact",
        "icon": "trending-up",
        "tagline": "Transform raw business figures into interactive dashboards and executive KPI reports.",
        "description": "BI Analysts empower decision-makers with clear data visualizations, automated reporting, and trend modeling. They sit between business operations and technical data teams to drive revenue growth and operational efficiency.",
        "salary_range": {"entry": "$70,000", "median": "$98,000", "senior": "$140,000+"},
        "growth_rate": "+21% through 2032 (Consistent growth across all industries)",
        "work_styles": ["Communicative", "Visual Thinker", "Business Mindset", "Detail-Oriented"],
        "education_recommended": ["Business, Finance, Economics, IT, or Statistics degree"],
        "core_skills": [
            "SQL", "Power BI / Tableau", "Excel / Sheets Modeling", "Data Warehousing Basics", "KPI Definition"
        ],
        "secondary_skills": [
            "Python basics", "DAX / Power Query", "Data Storytelling", "Statistical Analysis", "ETL concepts"
        ],
        "soft_skills": [
            "Business Translation", "Active Listening", "Presentation Skills", "Clarity"
        ],
        "interests": [
            "Business Strategy", "Data Visualization", "Financial Analysis", "Metrics", "Dashboard Design"
        ],
        "roles": [
            "Business Intelligence Analyst", "Tableau Developer", "Commercial Analytics Manager",
            "Reporting Specialist", "Operations Analyst"
        ],
        "roadmap": [
            {
                "phase": "Phase 1: Advanced Excel & SQL Foundations",
                "timeframe": "Months 1-2",
                "skills": ["Advanced Excel (Index/Match, PowerPivot)", "SQL Joins, Aggregations, Grouping", "Data Hygiene"],
                "project": "Build a financial revenue reconciliation model using SQL queries."
            },
            {
                "phase": "Phase 2: Modern BI Dashboards (Power BI / Tableau)",
                "timeframe": "Months 3-4",
                "skills": ["Power BI DAX measures", "Tableau Calculated Fields", "Visual Best Practices", "Interactivity"],
                "project": "Create a multi-page interactive executive sales performance dashboard."
            },
            {
                "phase": "Phase 3: Data Warehousing & Semantic Modeling",
                "timeframe": "Months 5-6",
                "skills": ["Star Schemas", "Connecting to Snowflake / BigQuery", "Scheduled Refresh Strategies"],
                "project": "Connect Power BI directly to a cloud data warehouse and configure incremental refreshes."
            },
            {
                "phase": "Phase 4: Advanced Storytelling & Business Strategy",
                "timeframe": "Months 7-8",
                "skills": ["Executive Presentations", "Root Cause Discovery", "Ad-hoc Modeling", "Automated Email Alerts"],
                "project": "Deliver an executive video presentation explaining a simulated quarterly revenue drop."
            }
        ],
        "resources": [
            {"title": "Microsoft Learn: Power BI Data Analyst Associate (PL-300)", "type": "Official Certification Path", "url": "https://learn.microsoft.com", "free": True},
            {"title": "Storytelling with Data by Cole Nussbaumer Knaflic", "type": "Book", "url": "https://www.storytellingwithdata.com", "free": False},
            {"title": "SQL for Business Intelligence on Coursera", "type": "Course", "url": "https://www.coursera.org", "free": False},
            {"title": "Tableau Public Community & Workout Wednesday", "type": "Challenges & Community", "url": "https://public.tableau.com", "free": True}
        ]
    },

    "blockchain_engineer": {
        "key": "blockchain_engineer",
        "title": "Web3 & Blockchain Engineer",
        "category": "Emerging Tech & Systems",
        "badge": "Cutting-Edge",
        "icon": "cpu",
        "tagline": "Develop decentralized smart contracts, cryptographic protocols, and secure Web3 applications.",
        "description": "Blockchain Engineers design decentralized protocols and write gas-optimized, tamper-resistant smart contracts. They navigate cryptography, tokenomics, and consensus mechanisms to pioneer the next generation of decentralized finance and digital sovereignty.",
        "salary_range": {"entry": "$100,000", "median": "$160,000", "senior": "$240,000+"},
        "growth_rate": "+22% through 2032 (Specialized high-reward field)",
        "work_styles": ["Security-Obsessed", "Cryptographic Mindset", "Autonomous", "Research-Oriented"],
        "education_recommended": ["CS, Cryptography, or proven smart contract audit portfolio"],
        "core_skills": [
            "Solidity / Rust", "Smart Contract Security", "EVM Architecture", "Web3.js / Ethers.js", "Foundry / Hardhat"
        ],
        "secondary_skills": [
            "Cryptography (Zero Knowledge Proofs)", "DeFi Protocols", "IPFS", "TypeScript", "Gas Optimization", "Go"
        ],
        "soft_skills": [
            "Extreme Security Paranoia", "Autonomous Problem Solving", "Adversarial Code Review", "Continuous Learning"
        ],
        "interests": [
            "Decentralization", "Cryptography", "Smart Contracts", "DeFi", "Consensus Algorithms"
        ],
        "roles": [
            "Smart Contract Engineer", "Solidity Auditor", "Protocol Developer",
            "Web3 Full-Stack Developer", "Zero-Knowledge Cryptographer"
        ],
        "roadmap": [
            {
                "phase": "Phase 1: Blockchain Principles & Cryptography",
                "timeframe": "Months 1-2",
                "skills": ["Hashing algorithms & Merkle trees", "Public-Key Cryptography", "EVM Basics", "MetaMask & Wallets"],
                "project": "Build a simple decentralized voting contract on an Ethereum testnet."
            },
            {
                "phase": "Phase 2: Solidity Mastery with Foundry",
                "timeframe": "Months 3-4",
                "skills": ["Solidity (ERC-20, ERC-721)", "Foundry Fuzz Testing", "Gas Optimization Techniques", "Events & Storage"],
                "project": "Create a staking and reward smart contract system with full unit test coverage in Foundry."
            },
            {
                "phase": "Phase 3: Smart Contract Security & Audits",
                "timeframe": "Months 5-6",
                "skills": ["Reentrancy Attacks", "Flash Loans", "Slither Static Analyzer", "Formal Verification Basics"],
                "project": "Complete security audits on Damn Vulnerable DeFi challenges."
            },
            {
                "phase": "Phase 4: Production DApp Integration & L2s",
                "timeframe": "Months 7-8",
                "skills": ["Ethers.js / Viem", "Arbitrum / Optimism / Base L2s", "The Graph Subgraphs", "Zero Knowledge basics"],
                "project": "Deploy a complete decentralized lending protocol DApp with responsive frontend."
            }
        ],
        "resources": [
            {"title": "Cyfrin Updraft: Free Web3 & Smart Contract Courses", "type": "Interactive Curriculum", "url": "https://updraft.cyfrin.io", "free": True},
            {"title": "SpeedRunEthereum by Austin Griffith", "type": "Hands-on Challenges", "url": "https://speedrunethereum.com", "free": True},
            {"title": "Damn Vulnerable DeFi (Security Challenges)", "type": "Security CTF", "url": "https://www.damnvulnerabledefi.xyz", "free": True},
            {"title": "Ethereum.org Developer Docs", "type": "Official Documentation", "url": "https://ethereum.org/developers", "free": True}
        ]
    }
}


def get_all_careers():
    """Return all career catalog dictionaries."""
    return list(CAREERS_DATABASE.values())


def get_career_by_key(career_key: str):
    """Retrieve single career details by key, or None."""
    return CAREERS_DATABASE.get(career_key)
