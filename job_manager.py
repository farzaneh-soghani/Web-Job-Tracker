import json
from operator import index
from job import Job
from datetime import date 

class JobManager:
    def __init__(self, filename="bewerbungen.json"):
        self.filename = filename
        self.jobs = self.load_jobs()
        
    def load_jobs(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                jobs = []
                for d in data:
                    # String-Datum → date-Objekt
                    if 'datum' in d:
                        datum_parts = d['datum'].split('.')
                        job_datum = date(int(datum_parts[2]), int(datum_parts[1]), int(datum_parts[0]))
                    else:
                        job_datum = date.today()
                    
                    job = Job(d['firma'], d['position'], d['status'], job_datum)
                    jobs.append(job)
                return jobs
        except:
            return []
    
    def save_jobs(self):
        data = [job.to_dict() for job in self.jobs]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    
    def add_job(self, firma, position, status="offen"):
        job = Job(firma, position, status)
        self.jobs.append(job)
        self.save_jobs()
        return job
    
    def delete_job(self, index):
        #Löscht Job an gegebener Position
        if 0 <= index < len(self.jobs):
            deleted_job = self.jobs.pop(index)
            self.save_jobs()
            return True
        return False
    
    def update_job(self, index, firma=None, position=None, status=None):
        #Aktualisiert Job an gegebener Position
        if 0 <= index < len(self.jobs):
            if firma: self.jobs[index].firma = firma
            if position: self.jobs[index].position = position  
            if status: self.jobs[index].status = status.lower()
            self.jobs[index].datum = date.today()  # Reset Timer
            self.save_jobs()
            return True
        return False


