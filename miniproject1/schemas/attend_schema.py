# schemas/attend_schema.py
# 출석 데이터 응답, 요청 구조 정의

from pydantic import BaseModel
from datetime import datetime

# 출석 등록 요청 데이터 구조
class AttendCreate(BaseModel):
    student_id: int
    attend: int
    late: int
    absent: int
    early_leave: int

# 출석 목록 응답 데이터 구조
class AttendResponse(BaseModel):
    id: int
    student_id: int
    student_name: str
    attend: int
    late: int
    absent: int
    early_leave: int
    total_days: int          # 전체 수업일수 (attend+late+absent+early_leave)
    attendance_rate: float   # 출석률 (%)
    create_at: datetime

    class Config:
        from_attributes = True