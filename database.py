from sqlalchemy import create_engine, text
import os
db_connection_string = os.environ['DB_CONNECTION_STRING']
engine = create_engine(
  db_connection_string,
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  }
)

def load_jobs_from_db():
  with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))
  jobs = []
  for row in result.all():
    jobs.append(dict(row._mapping))
  return jobs
def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"),{'val': id})
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return rows[0]._asdict()

def add_application_to_db(job_id,data,resume):
  parameters = {
    "job_id": job_id,
    "full_name": data['full_name'],
    "email": data['email'],
    "LinkedIn": data['LinkedIn'],
    "education": data['education'],
    "work_experience": data['work_experience'],
    "resume": resume
  }
  with engine.connect() as conn:
    query = text("INSERT INTO applications (job_id, full_name, email, LinkedIn, education, work_experience, resume) VALUES (:job_id, :full_name, :email, :LinkedIn, :education, :work_experience, :resume)")
    conn.execute(query,parameters)

