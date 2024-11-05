from fastapi import APIRouter, HTTPException, Request, status
from sqlalchemy import delete, select
from database import *
from schemas import *
from sqlalchemy.exc import IntegrityError

router = APIRouter(prefix="/api")

@router.post(
    "/createjob",
    response_model=GetJobData,
    status_code=status.HTTP_200_OK,
)
def create_job(request: Request, data: CreateJobData):
    with new_session() as session:
        field = JobModel(
            job_name=data.job_name,
        )
        session.add(field)
        try:
            session.flush()
        except IntegrityError:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                "Can't create: bad request",
            )
        session.commit()
        return GetJobData(**field.__dict__)


@router.post(
    "/createfinhelpclause",
    response_model=GetFinhelpClauseData,
    status_code=status.HTTP_200_OK,
)
def create_finhelp_clause(request: Request, data: CreateFinhelpClauseData):
    with new_session() as session:
        data_dict = data.model_dump()
        field = FinhelpClauseModel(**data_dict)
        session.add(field)
        try:
            session.flush()
        except IntegrityError:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                "Can't create: bad request",
            )
        session.commit()
        return GetFinhelpClauseData(**field.__dict__)


@router.post(
    "/createworker",
    response_model=GetWorkerData,
    status_code=status.HTTP_200_OK,
)
def create_worker(request: Request, data: CreateWorkerData):
    with new_session() as session:
        data_dict = data.model_dump()
        field = WorkerModel(**data_dict)
        session.add(field)
        try:
            session.flush()
        except IntegrityError:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                "Can't create: bad request",
            )
        session.commit()
        return GetWorkerData(**field.__dict__)


@router.post(
    "/createstudent",
    response_model=GetStudentData,
    status_code=status.HTTP_200_OK,
)
def create_student(request: Request, data: CreateStudentData):
    with new_session() as session:
        data_dict = data.model_dump()
        field = StudentModel(**data_dict)
        session.add(field)
        try:
            session.flush()
        except IntegrityError:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                "Can't create: bad request",
            )
        session.commit()
        return GetStudentData(**field.__dict__)


@router.post(
    "/createfinhelpapplicant",
    response_model=GetFinhelpApplicantData,
    status_code=status.HTTP_200_OK,
)
def create_finhelp_applicant(request: Request, data: CreateFinhelpApplicantData):
    with new_session() as session:
        data_dict = data.model_dump()
        field = FinhelpApplicantModel(**data_dict)
        session.add(field)
        try:
            session.flush()
        except IntegrityError:
            raise HTTPException(
                status.HTTP_400_BAD_REQUEST,
                "Can't create: bad request",
            )
        session.commit()
        return GetFinhelpApplicantData(**field.__dict__)


@router.get(
    "/getfinhelpapplicant",
    response_model=GetFinhelpApplicantData,
    status_code=status.HTTP_200_OK,
)
def get_finhelp_applicant(request: Request, id: int):
    with new_session() as session:
        query = select(FinhelpApplicantModel).filter_by(finhelp_applicant_id=id)
        result = session.execute(query)
        field = result.scalars().first()
        if field is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Field with this ID does not exist",
            )
        return field


@router.get(
    "/getfinhelpclause",
    response_model=GetFinhelpClauseData,
    status_code=status.HTTP_200_OK,
)
def get_finhelp_clause(request: Request, id: int):
    with new_session() as session:
        query = select(FinhelpClauseModel).filter_by(finhelp_clause_id=id)
        result = session.execute(query)
        field = result.scalars().first()
        if field is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Field with this ID does not exist",
            )
        return field


@router.get(
    "/getworker",
    response_model=GetWorkerData,
    status_code=status.HTTP_200_OK,
)
def get_worker(request: Request, id: int):
    with new_session() as session:
        query = select(WorkerModel).filter_by(worker_id=id)
        result = session.execute(query)
        field = result.scalars().first()
        if field is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Field with this ID does not exist",
            )
        return field


@router.get(
    "/getstudent",
    response_model=GetStudentData,
    status_code=status.HTTP_200_OK,
)
def get_student(request: Request, id: int):
    with new_session() as session:
        query = select(StudentModel).filter_by(student_id=id)
        result = session.execute(query)
        field = result.scalars().first()
        if field is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Field with this ID does not exist",
            )
        return field


@router.get(
    "/getjob",
    response_model=GetJobData,
    status_code=status.HTTP_200_OK,
)
def get_job(request: Request, id: int):
    with new_session() as session:
        query = select(JobModel).filter_by(job_id=id)
        result = session.execute(query)
        field = result.scalars().first()
        if field is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Field with this ID does not exist",
            )
        return field


@router.put(
    "/updatejob",
    response_model=GetJobData,
    status_code=status.HTTP_200_OK,
)
def update_job(request: Request, id: int, data: CreateJobData):
    with new_session() as session:
        query = select(JobModel).filter_by(job_id=id)
        result = session.execute(query)
        field = result.scalars().first()
        if field is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User with this user id does not exist",
            )
        field.job_name = data.job_name
        session.flush()
        session.commit()
        return {}


@router.delete(
    "/deletefinhelpapplicant",
    response_model=GetFinhelpApplicantData,
    status_code=status.HTTP_200_OK,
)
def update_finhelp_applicant(request: Request, id: int):
    with new_session() as session:
        query = delete(FinhelpApplicantModel).filter_by(finhelp_applicant_id=id)
        session.execute(query)
        session.flush()
        session.commit()
        return {}
