from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Boolean
from sqlalchemy.types import Date
from database import Base


class StorageAcounts(Base):
    __tablename__ = "StorageAccount"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
    public = Column(Boolean)
    tls = Column(String(255), index=True)
    https = Column(String(255), index=True)

