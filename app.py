import json, os, glob, uuid
from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import timedelta, datetime

app = Flask(__name__)
app.secret_key = 'dev-secret'
app.permanent_session_lifetime = timedelta(days=365)

@app.before_request
def make_session_permanent():
    session.permanent = True

def get_user_file():
    """Intelligente User-Datei Erkennung"""
    # 1. Session User-ID?
    if 'user_id' in session:
        user_file = f"bewerbungen_{session['user_id']}.json"
        if os.path.exists(user_file):
            return user_file
    
    # 2. Suche nach EINZIGER Datei
    user_files = glob.glob("bewerbungen_*.json")
    if len(user_files) == 1:
        session['user_id'] = os.path.basename(user_files[0]).replace("bewerbungen_", "").replace(".json", "")
        return user_files[0]
    
    # 3. Neuer Benutzer
    session['user_id'] = str(uuid.uuid4())
    return f"bewerbungen_{session['user_id']}.json"

def load_jobs(user_file):
    """Jobs aus JSON laden"""
    if os.path.exists(user_file):
        try:
            with open(user_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    return []

def save_jobs(user_file, jobs):
    """Jobs in JSON speichern"""
    with open(user_file, 'w', encoding='utf-8') as f:
        json.dump(jobs, f, indent=2, ensure_ascii=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    user_file = get_user_file()
    jobs = load_jobs(user_file)
    
    if request.method == 'POST':
        jobs.append({
            'firma': request.form['firma'],
            'position': request.form['position'],
            'status': request.form['status'],
            'datum': datetime.now().strftime('%d.%m.%Y')
        })
        save_jobs(user_file, jobs)
        flash('✅ Bewerbung hinzugefügt!')
        return redirect(url_for('index'))
    
    return render_template('index.html', jobs=jobs)

@app.route('/stats')
def stats():
    user_file = get_user_file()
    jobs = load_jobs(user_file)
    total = len(jobs)
    offen = len([j for j in jobs if j['status'] == 'offen'])
    offen_prozent = round((offen/total*100), 1) if total > 0 else 0
    return render_template('stats.html', total=total, offen=offen, offen_prozent=offen_prozent)

@app.route('/delete/<int:index>')
def delete_job(index):
    user_file = get_user_file()
    jobs = load_jobs(user_file)
    if 0 <= index < len(jobs):
        del jobs[index]
        save_jobs(user_file, jobs)
        flash('🗑️ Bewerbung gelöscht!')
    else:
        flash('❌ Job nicht gefunden!')
    return redirect(url_for('index'))

@app.route('/edit/<int:index>', methods=['GET', 'POST'])
def edit_job(index):
    user_file = get_user_file()
    jobs = load_jobs(user_file)
    
    if request.method == 'POST':
        if 0 <= index < len(jobs):
            jobs[index] = {
                'firma': request.form['firma'],
                'position': request.form['position'],
                'status': request.form['status'],
                'datum': datetime.now().strftime('%d.%m.%Y')
            }
            save_jobs(user_file, jobs)
            flash('✏️ Aktualisiert!')
            return redirect(url_for('index'))
    
    if 0 <= index < len(jobs):
        return render_template('edit.html', job=jobs[index], index=index)
    flash('❌ Job nicht gefunden!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    import webbrowser, threading, time
    threading.Thread(target=lambda: (time.sleep(1.2), webbrowser.open('http://127.0.0.1:5000')), daemon=True).start()
    app.run(debug=True, use_reloader=False)
