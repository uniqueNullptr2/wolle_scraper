import requests
from bs4 import BeautifulSoup
from db import Wolle


# Lieferzeit: Lieferbar, Begrenzter Vorrat: X, Halten Sie mich auf dem Laufenden (nicht lieferbar), 

base_link = "https://www.wollplatz.de/wolle"
def scrape_wool_data(hersteller, produkt):
    """Gibt ein Wolle Objekt zurück"""
    hersteller = hersteller.lower().replace(" ", "-")
    produkt = produkt.lower().replace(" ", "-")
    text = requests.get(f"{base_link}/{hersteller}/{hersteller}-{produkt}").content
    return parse_html(hersteller, produkt, text)

def parse_html(hersteller, produkt, text):
    """parses html und gibt ein Wolle Objekt zurück"""
    soup = BeautifulSoup(text, "html.parser")
    preis = soup.select_one(".product-price > span:nth-child(2)").get_text()
    #TODO funktioniert das auch bei den anderen varianten?
    lieferzeit = soup.select_one("#ContentPlaceHolder1_upStockInfoDescription").findChildren("span")[0].get_text()
    zusammenstellung=""
    nadelstaerke = ""
    tmp = soup.select_one("#pdetailTableSpecs")
    data_table = tmp.table
    for row in data_table.find_all("tr"):
        columns = row.find_all("td");
        if columns[0].get_text() == "Zusammenstellung":
            zusammenstellung = columns[1].get_text()
        if columns[0].get_text() == "Nadelstärke":
            nadelstaerke = columns[1].get_text()
    return Wolle(hersteller=hersteller, produkt=produkt, preis=preis, lieferzeit=lieferzeit, nadelstaerke=nadelstaerke, zusammenstellung=zusammenstellung)