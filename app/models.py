from sqlalchemy import Column, Integer, DECIMAL, String, Date, Null, ForeignKey
from sqlalchemy.orm import relationship
from passlib.context import CryptContext
from app.database import Base
import bcrypt

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String, index=True)
    date_of_born = Column(Date, nullable=True, index=True)
    
    tasks = relationship('Task', back_populates='executor_user')
    
    async def set_password(self, password: str):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    async def verify_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())
    
    
class Task(Base):
    __tablename__='tasks'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    status = Column(String, index=True)
    
    executor_id = Column(Integer, ForeignKey('users.id'))
    executor_user = relationship("User", back_populates="tasks")