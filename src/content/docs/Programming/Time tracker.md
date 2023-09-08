---
title: Time tracker
---
# Time Tracker

# BUGS

1. Bug wenn man gerade trackt und dann den Titel ändert, dann verschwindet einmal kurz der Titel und taucht wieder auf (liegt daran, dass beim rausklicken erst der eingegebene Titel aktualisiert wird und danach dann den, den man im Dropdown menü ausgewählt hat
2. beide trackings a sollten hier zusammengefasst sein
4. Sync updates: Wenn man auf starten geht, dann ist es synced, aber beim stoppen nicht. Genauso geht es mit den Tags nicht, aber die Titel funktionieren
5. Tags Auswahl aktualisieren (sind noch vom Sessionstorage abhängig)
6. clear sessionStorage after signing out

# Zeitplan

1. Setup zwischen Frontend und Backend
2. User Login / Google Sign-in

# Features

- Pomodoro
- Titel
- Gleiche Titel gruppieren
- Tags
- Client
- Manual time
- Reports
- Bills
- Change current Tracking time (holding shift down, to in-/decrease by ten)
    
    ![Untitled](Time%20tracker/Untitled%201.png)
    
- schon bezahlte Rechnungen und noch nicht bezahlte Rechnungen

# Tools

- Database: Supabase
- Host: Nestlify?
- Login: via Google
- Frontend Framework: VueJs
- Language: JavaScript / Typescript