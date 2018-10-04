.. _avanti.changes: 

========================
Changes in Lino Avanti
========================

Coming version
===============

1. Ab September 2018 soll der Zustand „Entschuldigt“ nicht mehr
   ausgewählt werden können. In den alten Daten soll er aber bestehen
   bleiben. Zustand „Abwesend“ ändern nach „Fehlt“.

2. Pro Einschreibung ein neues Feld „% Abwesenheiten“, das sowohl der
   Kursleiter als auch der Sozi sehen kann. Dieses Feld wird jeden
   Abend automatisch aktualisiert sowie ggf. manuell pro Kurs auf
   Knopfdruck.

3. Abmahnungen werden ab September nicht mehr geschrieben. Die
   bestehenden Abmahnungen dürfen aber weiter sichtbar bleiben.

4. Die Datenproblemmeldungen "Mehr als 2x abwesend" und "Mehr als 10%
   verpasst" werden durch die Liste im folgenden Punkt ersetzt.

5. Die Sozis kriegen eine neue Liste "Meine Pappenheimer" (genauer
   Name noch offen), in der alle aktiven Einschreibungen gezeigt
   werden, die mehr als 10% Abwesenheit haben (und deren Kurs aktiv
   ist)

6. Neue Auswahlmöglichkeit "Arbeitsunfähig" im Feld Berufliche
   Situation.
   
7. Es kommt bei euch vor, dass zwei Benutzer auf dem gleichen Klienten
   arbeiten, z.B. einer den Bericht Sprachtest eingibt und anderswo
   jemand ein anderes Feld ändert. Da kann es passieren, dass die
   Änderungen des einen verloren gehen. Wenn die Zeit reicht, könnten
   wir die Klientenstammdaten standardmäßig auf schreibgeschützt
   stellen und nur freigeben wenn man vorher auf einen Button
   "Bearbeiten" klickt.

- Neues Feld "Abwesenheitsgrund" pro Abwesenheit.

Ungefragt:

- :ticket:`2441` : "Intelligente" Übersicht der Termine pro Kurs.


2018-01-24
==========

- Der neue Klientenzustand "Empfangsbestätigung" fehlte noch.

Abmahnungen :

- Feld "Ausgestellt am" umbenennen nach "Situation am", und dieses
  Feld automatisch ausfüllen mit dem Datum der "letzten Stunde, für
  die der Kursleiter seine Anwesenheiten erfasst hat". Die Lehrer
  erfassen die Anwesenheiten manchmal verspätet, aber Mahnungen können
  nicht warten.

- Neuer ReminderState "Storniert" für wenn eine gültige Entschuldigung
  erst nach Verschicken der Mahnung eingereicht wird.

Verwaltung der Erstkontakte:

- Neuer Klientenzustand "Empfangsbestätigung"
- insert_layout in EntriesByClient : Eintragsart rein, Enddatum raus
- Unbestätigte Termine : (1) default 1 Woche vorher und (2) ins
  Dashboard rein


  

Version 0.0.1
=============

This project was first publised on 2016-08-07.
