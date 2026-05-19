# database.db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "mysql+pymysql://hkkim:1234@localhost:3306/hkkim"

engine = create_engine(DB_URL, echo=True)

# DB 쿼리문 실행 시킬 객체
SessionLocal = sessionmaker( autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()