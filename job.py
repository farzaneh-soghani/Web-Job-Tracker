from datetime import date, datetime

class Job:
    def __init__(self, firma, position, status, datum=None):
        self.firma = firma
        self.position = position
        self.status = status.lower()
        self.datum = date.today()
        self.datum = datum or datetime.now().strftime("%d.%m.%Y")
    
    def days_open(self):
        return (date.today() - self.datum).days
    
    def to_dict(self):
        return {
            'firma': self.firma,
            'position': self.position,
            'status': self.status,
            'datum': str(self.datum) 
        }
