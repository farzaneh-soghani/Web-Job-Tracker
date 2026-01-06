# 💼 Web-Job-Tracker 📊
**Bewerbungen im Überblick halten:** Speichere Firmen, Positionen, Status & Deadlines. **Bringe Ordnung in deine Jobsuche** - filtere, sortiere, tracke **alles auf einem Bildschirm!** 🎯

*Flask Web-App für Bewerbungs-Management (MVC Pattern)* 

## 🌐 Live Demo 
[![Live Demo](https://img.shields.io/badge/Live-Coming%20Soon-blue)](https://web-job-tracker.onrender.com)

## 🚀 Features
- ✅ Vollständiges CRUD (Create, Read, Update, Delete)
- 📱 Responsive Design (max-width: 1000px)
- 💾 JSON Persistence (bewerbungen.json)
- 📈 Live Statistics Dashboard
- ⏱️ Automatischer Tage-Zähler
- 🎨 Clean UI (Flexbox + versteckte Scrollbar)

## 🏗️ MVC Architektur  
- Model: job.py (Daten + Business-Logik)
- Service: job_manager.py (CRUD + JSON)
- Controller: app.py (Flask Routes)
- View: templates/ (Jinja2 + HTML5)

## 🏁 Quick Start
```bash
pip install -r requirements.txt
python app.py
```
→ Browser öffnet automatisch! 🎉

## 📸 Screenshots
| Dashboard | Statistics | Edit Form |
|-----------|------------|-----------|
| ![Dashboard](screenshots/dashboard.png "Hauptseite") | ![Stats](screenshots/stats.png "Statistiken") | ![Edit](screenshots/edit.png "Bearbeiten") |  

## 🛠️ Tech Stack  
- Frontend:  HTML5 + Jinja2 + Vanilla CSS (Flexbox)
- Backend:   Flask 3.0.0 + Python 3.x
- Database:  JSON File Storage (bewerbungen.json)
- Deployment: GitHub + Render ready

## 📁 Projektstruktur

**Auflistung der Ordnerpfade**  
*(Automatisch generiert mit `tree /f` command)*  
C:.  
│&nbsp;&nbsp;&nbsp;&nbsp; .gitignore  
│&nbsp;&nbsp;&nbsp;&nbsp; app.py  
│&nbsp;&nbsp;&nbsp;&nbsp; bewerbungen.json  
│&nbsp;&nbsp;&nbsp;&nbsp; job.py  
│&nbsp;&nbsp;&nbsp;&nbsp; job_manager.py  
│&nbsp;&nbsp;&nbsp;&nbsp; LICENSE  
│&nbsp;&nbsp;&nbsp;&nbsp; Procfile  
│&nbsp;&nbsp;&nbsp;&nbsp; README.md  
│&nbsp;&nbsp;&nbsp;&nbsp; requirements.txt  
│&nbsp;&nbsp;&nbsp;&nbsp; struktur.txt  
│     
├───screenshots  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; dashboard.png  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; edit.png  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; stats.png  
│         
├───templates  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; base.html  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; edit.html  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; index.html  
│&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; stats.html  
│         
└───__pycache__  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; job.cpython-311.pyc  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; job_manager.cpython-311.pyc

**💼 Made with ❤️ in Hamburg | [🔗 LinkedIn](https://www.linkedin.com/in/farzaneh-soghani/)**
