from datetime import date

from pydantic import BaseModel


# Creating pydantic schemes. You can inherit attrubutes
# This helps when thinking about what data to return to a user. You may want password to be passed when create something but not when reading.
class StorageBase(BaseModel):
    id: int
    name: str
    public: str
    tls: str
    https: str


class StorageCreate(StorageBase):
    pass


class StorageRead(StorageBase):
    pass

    class Config:
        orm_mode = True
