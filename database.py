from sqlalchemy import create_engine, text

db_connetion_string = "mysql+pymysql://e6vd8bm43h3wxw4y9sg7:pscale_pw_IcKJrdGFSX115UH9bdFD8SXvI775onZtctnh0AJHn4y@aws.connect.psdb.cloud/febricareers?charset=utf8mb4"

engine = create_engine(
    db_connetion_string,
    connect_args = {
        'ssl': {
            'ca': '/etc/ssl/cert.pem'
        }
    }
)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM jobs'))
        jobs = [row._asdict() for row in result.all()]

    return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text('SELECT * FROM jobs WHERE id=:id'), {'id': id})

        job = [row._asdict() for row in result.all()]
        
        if len(job) == 0: return None
        else: return job[0]

def add_application_to_db(job_id, data):
    with engine.connect() as conn:

        query = text('INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)')

        conn.execute(query, {
            'job_id': job_id,
            'full_name': data['full_name'],
            'email': data['email'],
            'linkedin_url': data['linkedin_url'],
            'education': data['education'],
            'work_experience': data['work_experience'],
            'resume_url': data['resume_url']
        })