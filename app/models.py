import datetime

from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql.sqltypes import Boolean

from database import Base


class StorageAccounts(Base):
    __tablename__ = "StorageAccount"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    public = Column(Boolean)
    tls = Column(String(255), index=True)
    https = Column(String(255), index=True)
    subscription = Column(String(255), index=True)
    resource_group = Column(String(255), index=True)
    report_date = Column(DateTime, default=datetime.datetime.utcnow)
