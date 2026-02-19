import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import timedelta, datetime
from uuid import uuid4

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret')
app.permanent_session_lifetime = timedelta(days=365)

@app.before_request
def make_session_permanent():
    session.permanent = True

def load_jobs():
    """Jobs aus SESSION laden"""
    return session.get('jobs', [])

def save_jobs(jobs):
    """Jobs in SESSION speichern"""
    session['jobs'] = jobs
    session.modified = True

@app.route('/', methods=['GET', 'POST'])
def index():
    jobs = load_jobs()
    
    if request.method == 'POST':
        return redirect(url_for('index'))
    
    return render_template('index.html', jobs=jobs)

@app.route('/stats')
def stats():
    jobs = load_jobs()
    return render_template('stats.html', jobs=jobs)

@app.route('/edit')
def edit_job_by_id():
    jobs = load_jobs()
    return render_template('edit.html', jobs=jobs)

@app.route('/notes')
def notes_by_id():
    jobs = load_jobs()
    return render_template('notes.html', jobs=jobs)

@app.route('/delete/<int:index>')
def delete_job(index):
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_job(index):
    jobs = load_jobs()
    if 0 <= index < len(jobs):
        job_id = jobs[index].get('id')
        if job_id:
            return redirect(url_for('edit_job_by_id', id=job_id))
        return redirect(url_for('edit_job_by_id'))
    flash('❌ Bewerbung nicht gefunden!')
    return redirect(url_for('index'))

@app.route('/notes/<int:index>', methods=['GET', 'POST'])
def notes(index):
    jobs = load_jobs()
    if 0 <= index < len(jobs):
        job_id = jobs[index].get('id')
        if job_id:
            return redirect(url_for('notes_by_id', id=job_id))
        return redirect(url_for('notes_by_id'))
    flash('❌ Bewerbung nicht gefunden!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    import webbrowser, threading, time
    threading.Thread(target=lambda: (time.sleep(1.2), webbrowser.open('http://127.0.0.1:5000')), daemon=True).start()
    app.run(debug=True, use_reloader=False)
