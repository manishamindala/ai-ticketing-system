from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    department = Column(String)
    skills = Column(String)  # Skills like 'DB', 'Server', 'HR'
    current_load = Column(Integer, default=0)
    is_available = Column(Boolean, default=True)

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    category = Column(String)
    severity = Column(String)
    status = Column(String, default="New")
    assignee_id = Column(Integer, ForeignKey("employees.id"), nullable=True)
    ai_summary = Column(String)