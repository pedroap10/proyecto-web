from app import db

class CarsModel(db.Model):
    _tablename_ = "cars"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    model = db.Column(db.String())
    doors = db.Column(db.Integer())
    def _init_(self, name, model, doors):
        self.name = name
        self.model = model
        self.doors = doors
    def _repr_(self):
        return f"<Cars {self.name}>"