# 💼 **JobTracker** - Bewerbungs-Tracker 📊

## 🎯 Bewerbungen im Überblick  

**Flask Web-App für Bewerbungs-Management (Single-File Architektur)**  
> **Speichere Firmen, Positionen, Status & Deadlines.**  
> **Bringe Ordnung in deine Jobsuche** - filtere, sortiere, tracke **alles auf einem Bildschirm!**

📱 **Auch unterwegs? KEIN Problem!** Responsiv für **Handy + Desktop** - deine Bewerbungen immer dabei! 🚀  
> **Im Handy direkt im Browser eingeben: [https://web-job-tracker-3.onrender.com](https://web-job-tracker-3.onrender.com)**

Oder für Desktop unten auf **"Live Deployed"** Button klicken  

## 🌐 Live Demo

[![Live Demo](https://img.shields.io/badge/Live-Deployed-brightgreen?logo=render)](https://web-job-tracker-3.onrender.com)  

## 🚀 Features

- ✅ Vollständiges **CRUD** (Create, Read, Update, Delete)
- 📱 **Responsive Design** (max-width: 1000px, @media 768px)
- 💾 **Session + Browser-Fingerprint** Storage (365 Tage persistent)
- 📈 **Live Statistics Dashboard** (`/stats`)
- ⏱️ **Automatisches Bewerbungserstellungsdatum** (DD.MM.YYYY)
- 🎨 **Clean Flexbox UI** + Mobile-First Design  

## 🏁 Quick Start

```bash
pip install -r requirements.txt
python app.py
```

→ Browser öffnet automatisch! 🎉

## 📸 Screenshots  

| Desktop Dashboard                 | Mobile Dashboard                | Statistics                    | Edit Form                   |
|-----------------------------------|---------------------------------|-------------------------------|-----------------------------|
|![Desktop](screenshots/desktop.png)|![Mobile](screenshots/mobile.png)|![Stats](screenshots/stats.png)|![Edit](screenshots/edit.png)|

## 🛠️ Tech Stack  

- Frontend: HTML5 + CSS3 Flexbox + Media Queries
- Backend:   Backend: Python + Flask + Jinja2
- Storage: Session + Browser-Fingerprint
- Features: Flash-Messages + Live Stats + CRUD
- Deployment: GitHub + Render ready

## 📁 Projektstruktur

**Auflistung der Ordnerpfade**  
*(Automatisch generiert mit `tree /f` command)*  

```txt
C:.
│   .gitignore
│   app.py
│   LICENSE
│   Procfile
│   README.md
│   requirements.txt
│   struktur.txt
│   
├───screenshots
│       desktop.png
│       edit.png
│       mobile.png
│       stats.png
│
└───templates
        base.html
        edit.html
        index.html
        stats.html
```  

**💼 Made with ❤️ in Hamburg | [🔗 LinkedIn](https://www.linkedin.com/in/farzaneh-soghani/)**
