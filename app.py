from flask import Flask, render_template, request, redirect, url_for
from parser import parse_resume
from matcher import rank_resumes
from db import init_db, insert_candidate, get_all_candidates
import os

UPLOAD_FOLDER = 'uploads'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_desc = request.form['job_description']
        files = request.files.getlist('resumes')
        resume_texts = []

        for file in files:
            path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(path)
            resume_text = parse_resume(path)
            resume_texts.append(resume_text)

        rankings = rank_resumes(job_desc, resume_texts)

        for idx, score in rankings:
            insert_candidate(f"Candidate {idx+1}", f"email{idx}@example.com", resume_texts[idx], round(score, 2))

        return redirect(url_for('results'))

    return render_template('index.html')

@app.route('/results')
def results():
    candidates = get_all_candidates()
    return render_template('results.html', candidates=candidates)

if __name__ == '__main__':
    app.run(debug=True)
