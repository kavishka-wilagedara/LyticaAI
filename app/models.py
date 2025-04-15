from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db
from app.enums import UserTypeEnum, SubscriptionStatusEnum
from sqlalchemy.dialects.postgresql import ENUM
from sqlalchemy import Enum as SQLAEnum  

# Create user model
class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(150), unique=True, nullable=False)
  password = db.Column(db.String(100), nullable=False)
  user_type = db.Column(SQLAEnum(UserTypeEnum), nullable=False)

  company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=True)
  is_active = db.Column(db.Boolean)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
    return f"<User {self.email}>"
  
class Company(db.Model):
  __tablename__ = 'companies'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(150), unique=True, nullable=False)
  stripe_customer_id = db.Column(db.String(255))
  is_trial_active = db.Column(db.Boolean)
  subscription_status = db.Column(SQLAEnum(SubscriptionStatusEnum), nullable=False, default=SubscriptionStatusEnum.TRIAL)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
        return f"<Company {self.name} | {self.subscription_status}>"


