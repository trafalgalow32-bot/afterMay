# routers/attend_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from service.attend_service import (get_attend_list, create_attend_service)
from schemas.attend_schema import (AttendCreate, AttendResponse)

router = APIRouter()

# 출석 등록
@router.post("/attend")
def create_attend(attend: AttendCreate, db: Session = Depends(get_db)):
    create_attend_service(attend, db)
    return {"message": "출석 데이터 저장 완료"}

# 출석 목록 조회
@router.get("/attend", response_model=list[AttendResponse])
def get_attend(db: Session = Depends(get_db)):
    return get_attend_list(db)