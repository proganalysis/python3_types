import uuid

from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.schema import Column
from sqlalchemy.sql.sqltypes import (Integer,
                                     String,
                                     DateTime)

from .base import Base


class Parameter(Base):
    __tablename__ = 'simulations_parameters'

    id = Column(Integer(),
                primary_key=True)
    group_id = Column(UUID(as_uuid=True),
                      nullable=False)
    name = Column(String(),
                  nullable=False)
    value = Column(String(),
                   nullable=False)
    created_timestamp = Column(DateTime(),
                               server_default=func.now())

    def __init__(self,
                 group_id: uuid.UUID,
                 name: str,
                 value: str):
        self.group_id = group_id
        self.name = name
        self.value = value
