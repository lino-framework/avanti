.. _avanti.specs.general:

===============================
General overview of Lino Avanti
===============================

The goal of Lino Avanti is 

.. How to test just this document:

    $ python setup.py test -s tests.SpecsTests.test_general
    
    doctest init:

    >>> import lino
    >>> lino.startup('lino_avanti.projects.avanti.settings.doctests')
    >>> from lino.api.doctest import *


Lino Noi uses both :mod:`lino_noi.lib.tickets` (Ticket management) and
:mod:`lino_noi.lib.clocking` (Worktime tracking).

.. contents::
  :local:

List of demo users:

>>> rt.show(rt.actors.users.Users)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
========== =============== ============ ===========
 Username   User type       First name   Last name
---------- --------------- ------------ -----------
 robin      Administrator   Robin        Rood
 rolf       Administrator   Rolf         Rompen
 romain     Administrator   Romain       Raffault
========== =============== ============ ===========
<BLANKLINE>


