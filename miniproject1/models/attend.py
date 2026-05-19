# models/attend.py (entity)와 같은 것!

from sqlalchemy import Column, Integer, ForeignKey, DateTime
from datetime import datetime

from database.db import Base

class Attend(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("student.id"))
    attend = Column(Integer)         # 출석 횟수
    late = Column(Integer)           # 지각 횟수
    absent = Column(Integer)         # 결석 횟수
    early_leave = Column(Integer)    # 조퇴 횟수
    create_at = Column(DateTime, default=datetime.now)