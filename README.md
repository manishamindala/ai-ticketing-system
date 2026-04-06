🎫 AI-Powered Smart Ticketing System
An Intelligent Helpdesk Solution with Automated Routing and Sentiment Analysis.

This project is a high-performance web application built with FastAPI and Google Gemini AI. It automates the lifecycle of support tickets by analyzing natural language to categorize severity, suggest technical tags, and intelligently route tasks to specific team members based on their skill sets and current workload.

🚀 Live Demo
URL: https://ai-ticketing-system-production-9254.up.railway.app/

✨ Key Features
AI Metadata Extraction: Leverages Google Gemini Pro to parse unstructured ticket descriptions into structured JSON (Severity, Category, Tags).

Dynamic Workload Routing: Automatically assigns tickets to employees (Manish, Anjali, Ruthvika) based on a "Least-Loaded-First" algorithm for optimized resource management.

Real-time Feedback: A sleek, responsive "Elite UI" dashboard that provides instant AI analysis results upon submission.

Automated Database Seeding: The system self-initializes with a default organizational structure on the first launch.

CI/CD Pipeline: Fully containerized and deployed via Railway with automated builds triggered by GitHub commits.

🛠️ Tech Stack
Backend: FastAPI (Python)

AI Engine: Google Gemini Pro API (google-generativeai)

Database: SQLite with SQLAlchemy ORM

Frontend: JavaScript (Fetch API), HTML5, CSS3 (Custom Theme)

Infrastructure: Railway (Cloud Hosting), GitHub (Version Control)
