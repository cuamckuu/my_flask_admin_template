from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, JSON, TIMESTAMP, Text, Boolean, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database import Base


class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    something = Column(String)
    created = Column(
        TIMESTAMP(timezone=True),
        default=func.now(),
        server_default=func.now()
    )

    def __repr__(self):
        return f"<Test ({self.id}, {self.name})>"
