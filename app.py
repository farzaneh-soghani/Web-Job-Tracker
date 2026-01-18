import os
from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import timedelta, datetime

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret')
app.permanent_session_lifetime = timedelta(days=365)

@app.before_request
def make_session_permanent():
    session.permanent = True

def get_user_file():
    """ULTIMATIVER Browser-Fingerprint"""
    # ALLE verfügbaren Headers kombinieren
    headers = [
        request.headers.get('User-Agent', ''),
        request.headers.get('Accept-Language', ''),
        request.headers.get('Accept-Encoding', ''),
        request.remote_addr or 'localhost'
    ]
    fingerprint = '_'.join(headers)
    browser_id = str(hash(fingerprint))[-15:]
    return f"browser_{browser_id}_jobs.json"

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
        if not isinstance(jobs, list):  
            jobs = []
        jobs.append({
            'firma': request.form['firma'],
            'position': request.form['position'],
            'status': request.form['status'],
            'datum': datetime.now().strftime('%d.%m.%Y'),
            'notes': ''
        })
        save_jobs(jobs)
        flash('✅ Bewerbung hinzugefügt!')
        return redirect(url_for('index'))
    
    return render_template('index.html', jobs=jobs)

@app.route('/stats')
def stats():
    jobs = load_jobs()
    total = len(jobs)
    offen = len([j for j in jobs if j['status'] == 'offen'])
    offen_prozent = round((offen/total*100), 1) if total > 0 else 0
    return render_template('stats.html', total=total, offen=offen, offen_prozent=offen_prozent)

@app.route('/delete/<int:index>')
def delete_job(index):
    jobs = load_jobs()
    if 0 <= index < len(jobs):
        del jobs[index]
        save_jobs(jobs)
        flash('🗑️ Bewerbung gelöscht!')
    else:
        flash('❌ Bewerbung nicht gefunden!')
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_job(index):
    jobs = load_jobs()
    if request.method == 'POST':
        if 0 <= index < len(jobs):
            jobs[index]['firma'] = request.form['firma']
            jobs[index]['position'] = request.form['position']
            jobs[index]['status'] = request.form['status']
            save_jobs(jobs)
            flash('✏️ Aktualisiert!')
            return redirect(url_for('index'))
    if 0 <= index < len(jobs):
        return render_template('edit.html', job=jobs[index], index=index)
    flash('❌ Bewerbung nicht gefunden!')
    return redirect(url_for('index'))

@app.route('/notes/<int:index>', methods=['GET', 'POST'])
def notes(index):
    jobs = load_jobs()
    if 0 <= index < len(jobs):
        if request.method == 'POST':
            jobs[index]['notes'] = request.form.get('notes', '')
            save_jobs(jobs)
            flash('📝 Notizen gespeichert!')
            return redirect(url_for('index'))
        return render_template('notes.html', job=jobs[index], index=index)
    flash('❌ Bewerbung nicht gefunden!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    import webbrowser, threading, time
    threading.Thread(target=lambda: (time.sleep(1.2), webbrowser.open('http://127.0.0.1:5000')), daemon=True).start()
    app.run(debug=True, use_reloader=False)
