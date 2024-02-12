import requests
from requests.structures import CaseInsensitiveDict

url = "https://api.openai.com/v1/chat/completions"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Bearer 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"

data = """
{
  "model": "gpt-4-vision-preview",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "Bitte verwende die folgenden Informationen darueber, wie man eine Bildanalyse schreibt: © Ernst Klett Verlag GmbH, Stuttgart 2013. Alle Rechte vorbehalten. ISBN 978-3-12-205119-8 Thema KUNST: Farbe (Schülerheft, Oberstufe) Autor: Torsten Krämer, Schwäbisch Gmünd Ein allgemeines Werkbetrachtungsmodell unter dem Aspekt der Farbe Bei einem Bildvergleich erscheint es sinnvoll, wenn die Werke im Sinne der Aufgabenstellung getrennt bearbeitet werden. Zum Schluss bietet sich dann eine vergleichende Gegenüberstellung an. Einleitung zu 1.1: Der erste Eindruck schildert den subjektiven Eindruck, die spontan individuelle Emp- findung vor dem Werk unter Verwendung treffender Adjektive und unter der Leitfrage: Wie wirkt das Werk auf den ersten Blick? zu 1.2: Bestandsaufnahme Die Beschreibung des Werkes unter der Leitfrage: Was sehe ich? Was ist auf dem Werk zu sehen? geschieht in einer dem Werk an- gemessenen Ordnung (vom Wichtigen zum Unwichtigen; vom Vor- der- über den Mittel- zum Hintergrund; vom Zentrum nach außen oder umgekehrt ...) Hier werden auch Sachinformationen (Daten) aufgenommen: Format (Hoch-, Querformat, Tondo, Oval ...); Bildträger (Holz, Leinwand, Aluminium ...); Technik (Malerei, Collage, Montage, Fotografie, Plastik, Objekt, Projektion, Installation; gesteuerte oder aleatorische, analoge oder digitale Verfahren ...); Material (Rohpigment, Tempera-, Öl- oder Acrylfarbe, andere Materialien, farbiges Licht ...); Thematik; Bildgattung (gegenständlich: Porträt, Figur, Stillleben, Interieur, Landschaft ...; ungegenständlich, abs- trakt). Hauptteil (Analyse und Interpretation) Die bildnerischen/gestalterischen Mittel (= formale Analyse) wer- den nach ihrer qualitativen Bedeutung ausgewählt und mit der Interpretation verzahnt. Bezüglich der formalen Analyse wird kei- ne Vollständigkeit erwartet, sondern in Verbindung mit der Inter- pretation eine begründete Tiefe. Die Analyse dient keinem Selbst- zweck, sondern bereitet die Deutung des Werkes vor. Leitfrage: Wie wurde das Werk gestaltet und wie wirkt das bildne- rische Mittel Farbe im Einzelnen? Formale Analyse (das bildnerische Mittel Farbe) Leitfrage: Wie wurde das bildnerische Mittel Farbe eingesetzt? zu 2.1: Farbwahl Farbtöne, deren Unterscheidung nach ihrer Eigenhelle ( Farbhel- ligkeit) und Buntanteil (Buntheit, Intensität) charakterisiert (S. 28) werden (vgl. S. 28) zu 2.2: Farbauftrag kann beschrieben werden als: lasierend, deckend, pastos form- beschreibend, pastos formauflösend, aleatorische Verfahren (ge- spachtelt, gerakelt, gestupft, gewischt, getropft, geschüttet, ge- siebt, gespritzt usw.); Duktus (sichtbare Pinselspur) oder flächig, ohne Pinsel- ooder Werkzeugspur; Arbeitsprozess (Lasur- bzw. Schichtenmalerei, Primamalerei, Mischtechnik ...) (vgl. S. 39) zu 2.2: Malkonzept linearer oder malerischer Malstil (vgl. S. 40) Seite 1/2 zu 2.3: Farbkonzept mögliche Einordnung als: chromatisch, koloristisch, valeuristisch (Tonwertmalerei), monochrom oder Claire-obscur, Grisaille ... (vgl. S. 44-47) zu 2.4: Licht Beleuchtungsart (sakrale, künstliche oder natürliche Lichtquelle); Beleuchtungslicht: Körper plastisch modellierend; Zeigelicht: ge- bündeltes Licht (welches eine Szene gezielt ausleuchtet); indiffe- rentes, diffuses Streulicht, allgemeine Tageshelligkeit; Glanz- oder Reflexlicht; Eigenlicht oder Sendelicht (v.a. im Mittelalter); Bild- licht (meint die allgemein von den Malfarben ausgehende Licht- wirkung im Bild); Beleuchtungsrichtung ... zu 2.5: Farbbeziehungen und Beziehung von Farbe und Gegenstand Beziehungen der Farben untereinander: Gegenfarben (Komple- mentär-Kontrast; Hell-Dunkel-Gegensatz, Qualitäts-Kontrast, Kalt- Warm-Kontrast, Inversion ... (vgl. S. 34) Wirkung, die emotionale Wahrnehmung von Farbe: warm - kühl, ruhig - unruhig, harmonisch oder disharmonisch ... Beziehung zum Gegenstand: Lokal-, Erscheinungs-, Ausdrucks-, Symbolfarbe, autonome Farbe; auch: Lokal- oder Gegenstandsfar- be expressiv gesteigert u.ä. (vgl. S. 48-52) zu 2.5: Beziehung von Farbe und Raum Raum illusionistisch beschreibend (Tiefenraum, Raumillusion durch Farbperspektive); Raum andeutend; Raum verneinend (z.B. Farbfeldmalerei) (vgl. S. 38) Interpretation zu 3: Interpretation Welche inhaltliche Bedeutung hat das Werk? Unter welchen Bedin- gungen entstand es? Welche Funktion hat es? ... Dabei geht es immer um das Verhältnis von Gegenstand/Thematik und seiner Gestaltung, von der künstlerischen Gestaltung und ih- rer Aussage. Alle zusammengetragenen Erkenntnisse ergeben in ihrer Gesamtschau eine erste Interpretation des Werkes in seiner Ganzheit. Schon unter dem Aspekt der Untersuchung der Farbe gelingt ein erster Zugang zum Werk, der sich allein auf die vom Künstler an- gewandten bildnerischen Mittel bezieht. Der werkimmanente Zusammenhang (in Bezug zur formalen Analyse) Wie ist das Thema dargestellt? In welchem Verhältnis steht die Farbe zum Inhalt? Zum Beispiel beschreiben Begriffe wie naturnah, realistisch, ide- alisiert, abstrahiert, verfremdet, deformiert ... das Verhältnis von Gegenstand (Thematik) und seiner Gestaltung oder die Wirkung der gesamten Farbkomposition; die Absicht und Aussage kann Form beschreibend, informierend (religiös, mythologisch, histo- risch, ...), emotional (Ausdruck einer subjektiven Stimmung) oder rein ästhetisch sein (allein die Wirkung der Farbe); Es geht immer um Abbild, Sinnbild oder Ausdruck. Ein direkter Ver- gleich zwischen Form und Inhalt ist sinnvoll.\n\n\nBitte schreibe die Analyse fuer das gegebene Bild mit den folgendem Inhalt: - Vertikale und horizontale Linien, keine Diagonalen -> Stabilität - Gleichmäßige Verteilung von hell und dunkel - Die vier Frauen sind hervorgehoben, da sie die einzigen Personen sind, die in einem Hell-Dunkel-Kontrast zum Hintergrund stehen. -> Befinden beim goldener Schnitt (x und y-Achse) - Weniger Farben aufgrund von Schwarzweiß -> ruhiger - Wenig bis keine Bewegung der Elemente im Bild - Wenig verschiedene Bildelemente - Blätter und Wiese bilden Farbfläche haben wenig Tiefe - Bruch der Diagonale durch den Mann mit dem Gehstock ist aufgehoben, da er im Hintergrund verschwindet (wenig Kontrast) - Weiche Schatten -> sanftes Erscheinungsbild - Köpfe befinden sich auf der gleiche Höhe, die Hand des stehenden Mannes befindet sich auch auf dieser Linie. Da der Kopf des stehenden Mannes im geringen Kontrast zum Hintergrund steht, fällt es nicht so stark ins Gewicht, dass er nicht auf dieser Linie ist. - Trennung links/rechts durch Kontrast in der Kleidung der Personen; Trennung oben/unten durch dunklen Hintergrund und hellen Vordergrund"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://img.artlogic.net/w_660,h_660,c_limit/exhibit-e/62f52bf90af321abff00fe82/76069c6ff25e75ed70cf3e060f45e72e.jpeg"
          }
        }
      ]
    }
  ],
  "max_tokens": 700
}
"""


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)


