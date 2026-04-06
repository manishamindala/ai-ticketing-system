from fastapi import FastAPI, Depends, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
import uvicorn
import os
import models, ai_engine, database

app = FastAPI()

# Create Database tables on startup
models.Base.metadata.create_all(bind=database.engine)
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
def seed_data():
    db = database.SessionLocal()
    # Check if employees exist, if not, add them for the demo
    if db.query(models.Employee).count() == 0:
        employees = [
            models.Employee(name="Manish", department="Engineering", skills="Server, DB", current_load=0),
            models.Employee(name="Anjali", department="IT Support", skills="Access", current_load=0),
            models.Employee(name="Ruthvika", department="HR Ops", skills="HR", current_load=0)
        ]
        db.add_all(employees)
        db.commit()
    db.close()

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit-ticket/")
async def create_ticket(title: str, description: str, db: Session = Depends(database.get_db)):
    # 1. Analyze with AI
    analysis = ai_engine.analyze_ticket(description)
    
    # 2. Create Ticket Object
    new_ticket = models.Ticket(
        title=title, 
        description=description, 
        category=analysis['category'], 
        severity=analysis['severity'], 
        ai_summary=analysis['ai_summary']
    )
    
    # 3. Smart Routing Logic based on AI suggested tag
    tag = analysis['suggested_tag']
    emp = db.query(models.Employee).filter(models.Employee.skills.contains(tag)).order_by(models.Employee.current_load.asc()).first()
    
    if emp:
        new_ticket.assignee_id = emp.id
        emp.current_load += 1
    
    db.add(new_ticket)
    db.commit()
    return {"analysis": analysis}

# --- RENDER DEPLOYMENT BLOCK ---
if __name__ == "__main__":
    # Render uses the PORT environment variable
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)