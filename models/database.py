from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine("sqlite:///gssoa.db")
SessionLocal = sessionmaker(bind=engine)

class RegistroQueda(Base):
    __tablename__ = "quedas"

    id = Column(Integer, primary_key=True, index=True)
    bairro = Column(String, index=True)
    tempo_estimado = Column(Integer)

def create_db_and_table():
    Base.metadata.create_all(bind=engine)
