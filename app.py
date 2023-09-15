from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)

@app.route('/')
def index():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs)

@app.route('/api/jobs')
def list_jobs():
    jobs = load_jobs_from_db()

    jobs_list = [dict(job) for job in jobs]
    
    return jsonify(jobs_list)

if __name__ == '__main__':
    app.run(port=3000, debug=True)