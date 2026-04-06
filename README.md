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



📂 Project Structure
Plaintext
/ai-ticketing-system
  ├── main.py            # FastAPI application entry point & routes
  ├── ai_engine.py       # Gemini AI prompt engineering & integration
  ├── database.py        # SQLAlchemy engine & session configuration
  ├── models.py          # Database schemas for Tickets & Employees
  ├── requirements.txt   # Project dependencies
  ├── runtime.txt        # Environment specification for Railway
  └── templates/         
       └── index.html    # Single-page application frontend
⚙️ Installation & Local Setup
Clone the Repository:

Bash
git clone https://github.com/manishamindala/ai-ticketing-system.git
cd ai-ticketing-system
Environment Setup:
Create a .env file in the root directory:

Bash
GEMINI_API_KEY='your_api_key_here'
Install Dependencies:

Bash
pip install -r requirements.txt
Run Locally:

Bash
python main.py
The application will be available at http://127.0.0.1:8000.
