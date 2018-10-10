.. _avanti.changes.coming: 

==============
Coming version
==============

TALK:

- Auditor sieht Vornamen der Klienten (:ticket:`2501`).
  Müsste behoben sein, aber nachzuprüfen.

DONE:

- Ab September 2018 soll der Zustand „Entschuldigt“ nicht mehr
  ausgewählt werden können. In den alten Daten soll er aber bestehen
  bleiben. Zustand „Abwesend“ ändern nach „Fehlt“.

  Die Datenproblemmeldungen "Mehr als 2x abwesend" und "Mehr als 10%
  verpasst" werden durch die Liste im folgenden Punkt ersetzt.

  Siehe :ref:`avanti.specs.cal`.

- Pro Einschreibung ein neues Feld „% Abwesenheiten“, das sowohl der
  Kursleiter als auch der Sozi sehen kann. Dieses Feld wird jeden
  Abend automatisch aktualisiert sowie ggf. manuell pro Kurs auf
  Knopfdruck.

  Siehe
  :attr:`lino_avanti.lib.courses.Enrolment.missing_rate` und
  :meth:`lino_avanti.lib.courses.Course.update_missing_rates`.

- Die Sozis kriegen eine neue Liste "Schwänzkontrolle", in
  der alle aktiven Einschreibungen gezeigt werden, die mehr als 10%
  Abwesenheit haben (und deren Kurs aktiv ist)

  Siehe :class:`lino_avanti.lib.courses.DitchingEnrolments`.
  
- Abmahnungen werden ab September nicht mehr geschrieben. Die
  bestehenden Abmahnungen dürfen aber weiter sichtbar bleiben.

- Neue Auswahlmöglichkeit "Arbeitsunfähig" im Feld Berufliche
  Situation.
   
  Siehe :class:`lino_avanti.lib.avanti.ProfessionalStates`.

- Neues Feld "Abwesenheitsgrund" pro Abwesenheit.

  Siehe :attr:`lino_avanti.lib.cal.Guest.absence_reason`
  und :class:`lino_avanti.lib.cal.AbsenceReasons`.
  
Ungefragte Änderungen:

- :ticket:`2441` : "Intelligente" Übersicht der Termine pro Kurs.

  Siehe Detail auf einem Kurs, Reiter "Kalender".

- Reihenfolge der Menübefehle : "Kalender" jetzt vor "Büro"
  
  Siehe :ref:`avanti.specs.roles`.

TODO:  

- Es kommt vor, dass zwei Benutzer auf dem gleichen Klienten arbeiten,
  z.B. einer den Bericht Sprachtest eingibt und anderswo jemand ein
  anderes Feld ändert. Da kann es passieren, dass die Änderungen des
  einen verloren gehen. Wenn die Zeit reicht, könnten wir die
  Klientenstammdaten standardmäßig auf schreibgeschützt stellen und
  nur freigeben wenn man vorher auf einen Button "Bearbeiten" klickt.

  
