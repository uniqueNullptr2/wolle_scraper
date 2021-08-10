from os.path import dirname, abspath
import scrape

def test_parse():
    """teste anhand einer html-Datei, dass das parsen grundsätzlich funktioniert"""
    p = dirname(abspath(__file__)) + "/../c.html"
    with open(p, "r") as f:
        contents = f.read()
        w = scrape.parse_html(contents)
        assert w.preis == "1,47"
        assert w.lieferzeit == "Lieferbar"
        assert w.nadelstaerke == "3 mm"
        assert w.zusammenstellung == "100% Baumwolle"

def test_scrape():
    """Teste ob der link richtig funktioniert und die Daten geparsed werden können"""
    scrape.scrape_wool_data("DMC", "Natura XL")