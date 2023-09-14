from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text('select * from jobs'))
        jobs = []
        for row in result.all():
            jobs.append(row._mapping)

    return jobs

@app.route('/')
def index():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(port=3000, debug=True)