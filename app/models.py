from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

# Create user model
class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  email = db.Column(db.String(150), unique=True, nullable=False)
  password = db.Column(db.String(100), nullable=False)
  user_type = db.Column(db.Enum('normal_user', 'company_user', name='user_type_enum'), nullable=False)
  role = db.Column(db.Enum('admin', 'user', name='role_enum'), nullable=True)

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
  subscription_status = db.Column(
     db.Enum('trial', 'active', 'expired', 'blocked',name='subscription_status_enum'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.utcnow)

  def __repr__(self):
        return f"<Company {self.name} | {self.subscription_status}>"


