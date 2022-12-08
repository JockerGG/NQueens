from sqlalchemy import Column, Integer, String
from ..database import Base

class Solutions(Base):
    __tablename__ = "Solutions"

    id = Column(Integer, primary_key = True, index = True)
    solutions = Column(String, index = True)
    number_of_queens = Column(Integer)