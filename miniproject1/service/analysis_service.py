# analysis_service.py

from fastapi import HTTPException

from models.student import Student
from models.attend import Attend
from models.score import Score

# 위험, 우수 학생
def get_student_status_service(db):
    students = db.query(Student).all()

    danger_std=[]
    excellent_std=[]

    for std in students:
        score = db.query(Score).filter(Score.student_id == std.id_)\
                    .first()
        attend = db.query(Attend).filter(Attend.student_id == std.id)\
                    .first()
        if score is None: continue
        if attend is None: continue

        avg = ( # 학생 한 명의 평균값
            score.python_score + score.numpy_score + 
            score.pandas_score + score.java_score + 
            score.project_score
        )/5
        
        tot_cnt = ( # 학생의 출석률
            attend.attend + attend.late + attend.absent +
            attend.early_leave
        )

        rate = (attend.attend / tot_cnt) * 100

        data = {
            "name": std.name,
            "avg_score": avg,
            "attend_rate": rate            
        }     
        if ( avg < 60 or rate < 70 ): # 관리 학생 분류
            data["status"]="관리필요"
            danger_std.append(data)
        elif ( avg >= 90 and rate >= 90): # 우수 학생
            data["status"]="우수"
            excellent_std.append(data)

    return {
        "danger_std": danger_std,
        "excellent_std": excellent_std
    }            

# 반전체 통계 - ClassSummaryPage
def get_class_summary(db):
    total_student = db.query(Student).count()
    if total_student ==0:
        raise HTTPException(
            status_code=404,
            message="등록된 학생이 없습니다."
        )
    # 전체 성적 조회
    scores = db.query(Score).all()

    # 전체 출석 조회
    attends = db.query(Attend).all()

    temp_avg_score = 0 # 전체 평균 계산 위한 임시 변수
    for score in scores:
        avg = (
            score.python_score + score.numpy_score + 
            score.pandas_score + score.java_score + 
            score.project_score
        )/5
        temp_avg_score += avg
    # 전체 평균값
    avg_score = temp_avg_score / total_student

    # 과목별 최고점 최저점
    python_scores = [ score.python_score for score in scores]
    numpy_scores = [ score.numpy_score for score in scores]
    pandas_scores = [ score.pandas_score for score in scores]
    java_scores = [ score.java_score for score in scores]
    project_scores = [ score.project_score for score in scores]

    # 전체 출석률
    total_rate = 0.0

    for att in attends:
        tot_cnt = (
            att.attend + att.late + att.absent +
            att.early_leave
        )
        rate = (att.attend / tot_cnt)* 100
        total_rate += rate
    avg_attend_rate = round(total_rate / total_student, 1)

    return {
        "total_student":total_student,
        "avg_score":avg_score,
        "avg_attend_rate":avg_attend_rate,
        "python_max":max(python_scores),
        "python_min":min(python_scores),
        "numpy_max":max(numpy_scores),
        "numpy_min":min(numpy_scores),
        "pandas_max":max(pandas_scores),
        "pandas_min":min(pandas_scores),
        "java_max":max(java_scores),
        "java_min":min(java_scores),
        "project_max":max(project_scores),
        "project_min":min(project_scores)
    }