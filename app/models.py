from sqlalchemy import Column, Integer, DECIMAL, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import uuid
from fastapi_users.db import (
    SQLAlchemyBaseOAuthAccountTableUUID,
    SQLAlchemyBaseUserTableUUID,
)



class User(SQLAlchemyBaseUserTableUUID, Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False, index=True)
    email = Column(String, index=True)
    date_of_born = Column(Date, nullable=True)
    
    oauth_accounts = relationship("OAuthAccount", back_populates="user")
    tasks = relationship('Task', back_populates='executor_user')

    
class OAuthAccount(SQLAlchemyBaseOAuthAccountTableUUID, Base):
    __tablename__ = "oauth_accounts"
    
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="oauth_accounts")
    
    
class Task(Base):
    __tablename__='tasks'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, index=True)
    
    executor_id = Column(Integer, ForeignKey('users.id'))
    executor_user = relationship("User", back_populates="tasks")