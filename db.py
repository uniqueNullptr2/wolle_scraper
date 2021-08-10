from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    db.init_app(app)
    db.create_all(app=app)

class Wolle(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hersteller = db.Column(db.String(25), nullable=False)
    produkt = db.Column(db.String(25), nullable=False)
    preis = db.Column(db.String(25), nullable=False)
    lieferzeit = db.Column(db.String(25), nullable=False)
    nadelstaerke = db.Column(db.String(25), nullable=False)
    zusammenstellung = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"<Hersteller: {self.hersteller}, Produkt: {self.produkt}, Preis: {self.preis}, Lieferzeit: {self.lieferzeit}, Nadelstärke: {self.nadelstaerke}, Zusammenstellung: {self.zusammenstellung}>"