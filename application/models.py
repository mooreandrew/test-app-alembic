from sqlalchemy import Column, Integer, String, DateTime
from application import db
from sqlalchemy.orm import relationship
from flask.ext.login import UserMixin

class Projects(db.Model):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True)
    project_name = Column(String(100), nullable=False)
    project_code = Column(Integer, nullable=False)

    def __init__(self, project_name, project_code):
        self.project_name = project_name
        self.project_code = project_code
