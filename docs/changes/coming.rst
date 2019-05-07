.. _avanti.changes.coming: 

==============
Coming version
==============

Not yet scheduled.

- NB : Lehrer haben die Kalenderansicht auch. Zu prüfen, ob sie das dürfen

- Sektretäre und Sozialarbeiter können jetzt die Termine ihrer Kollegen
  bearbeiten.  Nebenwirkung: diese Benutzer haben jetzt auch Zugriff auf diverse
  Tabellen in Konfigurierung --> Kalender.

- "Tagesplaner" ersetzt durch "Kalenderansicht". Die "Kalenderansicht" soll
  irgendwann den "Kalender" ersetzen.

- The merge button is no longer available on many models
  (:ticket:`2191`).

- Im Workflow eines Termins (Stunde) stimmten die Bezeichnungen des
  Zustands nicht mit den Symbolen überein.

    ============= ============== ============ ============== ================================
     Action name   Verbose name   Help text    Target state   Required states
    ------------- -------------- ------------ -------------- --------------------------------
     reset_event   Reset          Suggested    Suggested      suggested took_place cancelled
     wf2           ☐              Draft        Draft          suggested cancelled took_place
     wf3           Took place     Took place   Took place     suggested draft cancelled
     wf4           ☒              Cancelled    Cancelled      suggested draft took_place
    ============= ============== ============ ============== ================================
  
