from flask import Flask, render_template,jsonify
app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Atlanta, Georgia',
    'Employment Type': 'FullTime'
  },
  {
    'id': 2,
    'title': 'Electrical Engineer',
    'location': 'Atlanta, Georgia',
    'Employment Type': 'Full-Time'
  },
  {
    'id': 3,
    'title': 'Software Engineer Intern',
    'location': 'Dallas, Texas',
    'Employment Type': 'Intern'
  },
  {
    'id': 4,
    'title': 'Project Manager',
    'location': 'Raleigh, North Carolina',
    'Employment Type': 'Full-Time'
  }
]
@app.route("/")
def hello_world():
  return render_template('home.html',jobs=JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)