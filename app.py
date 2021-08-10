import scrape
import csv
from flask import Flask, render_template
from db import db, init_db, Wolle
from apscheduler.schedulers.background import BackgroundScheduler
import atexit
# Hahh kann ich momentan auf der seite gernicht finden
static_wolle = {
    "DMC":  [
        "Natura XL"
    ],
    "Drops": [
        "Safran",
        "Baby Merino Mix"
    ],
    "Stylecraft": [
        "Special DK"
    ]
}
def scrape_job():
    print("scraping")
    with app.app_context():
        for hersteller in static_wolle:
            for produkt in static_wolle[hersteller]:
                wolle_neu = scrape.scrape_wool_data(hersteller, produkt)
                wolle_alt = Wolle.query.filter(Wolle.hersteller==wolle_neu.hersteller, Wolle.produkt==wolle_neu.produkt).first()
                if wolle_alt is None:
                    print("entry not found yo")
                    db.session.add(wolle_neu)
                else:
                    wolle_alt.preis = wolle_neu.preis
                    wolle_alt.lieferzeit = wolle_neu.lieferzeit
                    wolle_alt.zusammenstellung = wolle_neu.zusammenstellung
                    wolle_alt.nadelstaerke = wolle_neu.nadelstaerke
        db.session.commit()
    print("done")

app = Flask(__name__)
app.config.from_pyfile("config.cfg")
init_db(app)

scheduler = BackgroundScheduler()
scheduler.add_job(func=scrape_job, trigger="interval", seconds=60*60)
scheduler.add_job(func=scrape_job)
scheduler.start()
atexit.register(lambda: scheduler.shutdown())


@app.route("/")
def wolle():
    wolle = Wolle.query.all();
    return render_template("wolle.html", wolle_collection=wolle)

# scrape_job()
app.run("localhost", 8080)
