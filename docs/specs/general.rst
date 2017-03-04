.. _avanti.specs.general:

===============================
General overview of Lino Avanti
===============================

The goal of Lino Avanti is 

.. How to test just this document:

    $ python setup.py test -s tests.SpecsTests.test_general
    
    doctest init:

    >>> import lino
    >>> lino.startup('lino_avanti.projects.adg.settings.doctests')
    >>> from lino.api.doctest import *


.. contents::
  :local:

List of demo users:

>>> rt.show(rt.actors.users.Users)
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
========== =============== ============ ===============
 Username   User type       First name   Last name
---------- --------------- ------------ ---------------
 janina     Auditor
 martina    Coordinator
 nathalie   Social worker
 robin      Administrator   Robin        Rood
 rolf       Administrator   Rolf         Rompen
 romain     Administrator   Romain       Raffault
 tom        Teacher         Tom          Thess-Thönnes
========== =============== ============ ===============
<BLANKLINE>


>>> dd.plugins.beid.holder_model
<class 'lino_avanti.lib.avanti.models.Client'>
