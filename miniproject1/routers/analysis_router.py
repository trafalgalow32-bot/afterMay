# analysis_router.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.db import get_db
from service.analysis_service import (
    get_class_summary, get_student_status_service)

router = APIRouter()

@router.get("/analysis/student-status")
def get_student_status(db: Session = Depends(get_db)):
    return get_student_status_service(db)

@router.get("/analysis/class-summary")
def get_class_summary_res(db:Session = Depends(get_db)):
    return get_class_summary(db)