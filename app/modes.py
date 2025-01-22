from sqlalchemy import Column, Integer, DECIMAL, String, Date, Null, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, nullable=True, index=True)
    password = Column(String, index=True)
    date_of_born = Column(Date, nullable=True, index=True)
    
    tasks = relationship('Task', back_populates='executor_user')
    
    
class Task(Base):
    __tablename__='tasks'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, index=True)
    
    executor_id = Column(Integer, ForeignKey('users.id'))
    executor_user = relationship("User", back_populates="tasks")