from sqlalchemy import ForeignKey
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import Optional

engine = create_async_engine("sqlite+aiosqlite:///./site.db")
new_session = async_sessionmaker(engine, expire_on_commit=False)


class Model(DeclarativeBase):
    pass


class WorkerModel(Model):
    __tablename__ = "worker"

    worker_id: Mapped[int] = mapped_column(primary_key=True)
    worker_last_name: Mapped[str]
    worker_first_name: Mapped[str]
    worker_middle_name: Mapped[Optional[str]]
    job_id: Mapped[int] = mapped_column(ForeignKey("job.job_id", ondelete="CASCADE"))

    job: Mapped["JobModel"] = relationship()
    finhelp_applications: Mapped[list["FinhelpApplicantModel"]] = relationship()


class JobModel(Model):
    __tablename__ = "job"

    job_id: Mapped[int] = mapped_column(primary_key=True)
    job_name: Mapped[str]


class FinhelpApplicantModel(Model):
    __tablename__ = "finhelp_applicant"

    finhelp_applicant_id: Mapped[int] = mapped_column(primary_key=True)
    student_id: Mapped[int] = mapped_column(ForeignKey("student.student_id", ondelete="CASCADE"))
    finhelp_clause_id: Mapped[int] = mapped_column(ForeignKey("finhelp_clause.finhelp_clause_id", ondelete="CASCADE"))
    worker_id: Mapped[int] = mapped_column(ForeignKey("worker.worker_id", ondelete="CASCADE"))

    worker: Mapped["WorkerModel"] = relationship()
    student: Mapped["StudentModel"] = relationship()
    finhelp_clause: Mapped["FinhelpClauseModel"] = relationship()

class FinhelpClauseModel(Model):
    __tablename__ = "finhelp_clause"

    finhelp_clause_id: Mapped[int] = mapped_column(primary_key=True)
    finhelp_clause_name: Mapped[str]
    finhelp_clause_payment_amount: Mapped[float]


class StudentModel(Model):
    __tablename__ = "student"

    student_id: Mapped[int] = mapped_column(primary_key=True)
    student_last_name: Mapped[str]
    student_first_name: Mapped[str]
    student_middle_name: Mapped[Optional[str]]

    finhelp_applications: Mapped[list["FinhelpApplicantModel"]] = relationship()


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)
