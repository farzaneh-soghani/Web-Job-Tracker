from datetime import date, timedelta

class Job:
    def __init__(self, firma, position, status="offen"):
        self.firma = firma
        self.position = position
        self.status = status.lower()
        self.datum = date.today()
    
    def days_open(self):
        return (date.today() - self.datum).days
    
    def to_dict(self):
        return {
            'firma': self.firma,
            'position': self.position,
            'status': self.status,
            'datum': self.datum.isoformat()
        }
