.. _avanti.changes.coming: 

==============
Coming version
==============

Not yet scheduled.

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
  
