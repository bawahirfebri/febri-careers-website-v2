from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Analyst',
        'location': 'Cilegon',
        'salary': 'Rp. 3.000.000'
    },
    {
        'id': 2,
        'title': 'Data Scientist',
        'location': 'Serang',
        'salary': 'Rp. 4.000.000'
    },
    {
        'id': 1,
        'title': 'Frontend Engineer',
        'location': 'Remote'
    },
    {
        'id': 1,
        'title': 'Backend Engineer',
        'location': 'Bogor',
        'salary': 'Rp. 5.000.000'
    }
]

@app.route('/')
def index():
    return render_template('home.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(port=3000, debug=True)