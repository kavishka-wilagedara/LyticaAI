from enum import Enum

class UserTypeEnum(Enum):
  SUPER_ADMIN = "super_admin"
  COMPANY_ADMIN = "company_admin"
  COMPANY_USER = "company_user"
  NORMAL_USER = "normal_user"
  
class SubscriptionStatusEnum(Enum):
  TRIAL = "trial"
  ACTIVE = "active"
  EXPIRED = "expired"
  BLOCKED = "blocked"
