# service/attend_service.py

from fastapi import HTTPException

from models.attend import Attend
from models.student import Student
from schemas.attend_schema import AttendResponse


def create_attend_service(attend, db):
    attendData = [attend.attend, attend.late, attend.absent, attend.early_leave]
    fields = ("attend", "late", "absent", "early_leave")

    # 1) 값 범위 검증 (0 미만 / 지나치게 큰 값)
    for i, v in enumerate(attendData):
        if v < 0:
            raise HTTPException(
                status_code=400,
                detail=fields[i] + " 값은 0 이상 입력 가능합니다."
            )
        if v > 365:
            raise HTTPException(
                status_code=400,
                detail=fields[i] + " 값이 정상 범위를 초과했습니다."
            )

    # 2) 전체 출석 데이터가 0인 경우
    if sum(attendData) == 0:
        raise HTTPException(
            status_code=400,
            detail="출석 데이터를 입력해주세요."
        )

    # 3) 학생 존재 여부 확인
    student = db.query(Student).filter(Student.id == attend.student_id).first()
    if student is None:
        raise HTTPException(
            status_code=404,
            detail="학생 정보를 찾을 수 없습니다."
        )

    # 4) 저장
    new_attend = Attend(
        student_id=attend.student_id,
        attend=attend.attend,
        late=attend.late,
        absent=attend.absent,
        early_leave=attend.early_leave
    )

    db.add(new_attend)
    db.commit()
    db.refresh(new_attend)


def get_attend_list(db):
    attend_list = db.query(Attend, Student)\
        .join(Student, Attend.student_id == Student.id)\
        .all()

    result = []
    for attend, std in attend_list:
        total_days = (attend.attend + attend.late +
                      attend.absent + attend.early_leave)
        # 분모 0 방어 (DB에 과거 데이터가 0,0,0,0 으로 들어가 있을 경우 대비)
        if total_days > 0:
            attendance_rate = round(attend.attend / total_days * 100, 1)
        else:
            attendance_rate = 0.0

        result.append(AttendResponse(
            id=attend.id,
            student_id=std.id,
            student_name=std.name,
            attend=attend.attend,
            late=attend.late,
            absent=attend.absent,
            early_leave=attend.early_leave,
            total_days=total_days,
            attendance_rate=attendance_rate,
            create_at=attend.create_at
        ))
    return result