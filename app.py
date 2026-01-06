from flask import Flask, render_template, request, redirect, url_for, flash
from job_manager import JobManager 
import time
import webbrowser 
import threading   

app = Flask(__name__)
app.secret_key = 'simple123'

job_manager = JobManager() 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        job_manager.add_job( 
            request.form['firma'], 
            request.form['position'], 
            request.form['status']
        )
        flash('✅ Bewerbung gespeichert!')
        return redirect(url_for('index'))
    
    jobs_dict = [job.to_dict() for job in job_manager.jobs]
    return render_template('index.html', jobs=jobs_dict)

@app.route('/stats')
def stats():
    total = len(job_manager.jobs)  
    offen = len([j for j in job_manager.jobs if j.status == 'offen'])
    offen_prozent = round((offen/total*100), 1) if total > 0 else 0
    return render_template('stats.html', total=total, offen=offen, offen_prozent=offen_prozent)

@app.route('/delete/<int:job_id>')
def delete_job(job_id):
    if job_manager.delete_job(job_id):
        flash('🗑️ Bewerbung gelöscht!')
    else:
        flash('❌ Job nicht gefunden!')
    return redirect(url_for('index'))

@app.route('/edit/<int:job_id>', methods=['GET', 'POST'])
def edit_job(job_id):
    if request.method == 'POST':
        job_manager.update_job(
            job_id,
            request.form['firma'],
            request.form['position'], 
            request.form['status']
        )
        flash('✏️ Bewerbung aktualisiert!')
        return redirect(url_for('index'))
    
    # GET: Edit-Form anzeigen
    if 0 <= job_id < len(job_manager.jobs):
        job = job_manager.jobs[job_id]
        return render_template('edit.html', job=job.to_dict(), job_id=job_id)
    flash('❌ Job nicht gefunden!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    
    def open_browser():
        # 0.8 Sekunden warten, dann öffnen
        time.sleep(0.8)
        webbrowser.open('http://127.0.0.1:5000')
    
    # Browser im Hintergrund öffnen
    threading.Timer(1.0, open_browser).start()
    
    app.run(debug=True, use_reloader=False)
   
