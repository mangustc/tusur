from pydantic import BaseModel


class GetByID(BaseModel):
    id: int = 1

class CreateWorkerData(BaseModel):
    worker_last_name: str = "mueoaueoa"
    worker_first_name: str = "aoeuidhtn"
    worker_middle_name: str = "aoeuidhtn"
    job_id: int = 1


class CreateJobData(BaseModel):
    job_name: str = "job"


class CreateFinhelpClauseData(BaseModel):
    finhelp_clause_name: str = "clause_name"
    finhelp_clause_payment_amount: int = 10000


class CreateFinhelpApplicantData(BaseModel):
    student_id: int = 1
    finhelp_clause_id: int = 1
    worker_id: int = 1


class CreateStudentData(BaseModel):
    student_last_name: str = "mueoaueoa"
    student_first_name: str = "aoeuidhtn"
    student_middle_name: str = "aoeuidhtn"


class GetWorkerData(BaseModel):
    worker_id: int = 1
    worker_last_name: str = "mueoaueoa"
    worker_first_name: str = "aoeuidhtn"
    worker_middel_name: str = "aoeuidhtn"
    job_id: int = 1


class GetJobData(BaseModel):
    job_id: int = 1
    job_name: str = "job"


class GetFinhelpClauseData(BaseModel):
    finhelp_clause_id: int = 1
    finhelp_clause_name: str = "clause_name"
    finhelp_clause_payment_amount: int = 10000


class GetFinhelpApplicantData(BaseModel):
    finhelp_applicant_id: int = 1
    student_id: int = 1
    finhelp_clause_id: int = 1
    worker_id: int = 1


class GetStudentData(BaseModel):
    student_id: int = 1
    student_last_name: str = "mueoaueoa"
    student_first_name: str = "aoeuidhtn"
    student_middle_name: str = "aoeuidhtn"

