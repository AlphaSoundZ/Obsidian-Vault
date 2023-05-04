# Drohne - Akkuwechselstation

# Ablauf des Wechsels

1. FLIGHT_STATUS = manual
2. Input der Fernbedienung, um den Wechsel zu starten
    - Manuelle Steuerung wird deaktiviert
    - Arm Schalter bleibt aktiv
    - FLIGHT_STATUS = battery_change_start
3. Drohne richtet sich aus, landet, und Motoren schalten sich ab
    - FLIGHT_STATUS = battery_change_pending
4. Akku wird gewechselt
5. Drohne geht an
    - FLIGHT_STATUS wird überprüft: Wenn FLIGHT_STATUS = battery_change_pending, dann füge Delay ein, bevor die Drohne fortfährt (Kalibrierung etc.)
    - Motoren der Drohne schalten sich an und werden kalibriert
6. Drohne startet, und steigt auf eine bestimmte Höhe
7. FLIGHT_STATUS = batter_change_finished
8. Warte auf Änderung des Throttles bzw. warte auf Mindestwert und arm muss an, um Absturz zu vermeiden
9. FLIGHT_STATUS = manual

# Probleme

- Woher weiß die Drohne, dass sie starten darf, da ja die Drohne immer an bleibt
    - Strom messen, ob an dem Konnektor für die Wechselstation
- Wie werden die Konnektoren des Akkus mit der Drohne verbunden
- Mechanismus zum Einrasten des Akkus

# Material

- Pixy2 CMUcam5 Sensor: zum Erkennen der Markierungen
- Ultraschall Sensor: zum Messen der Entfernung zum Boden