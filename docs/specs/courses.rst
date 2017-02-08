.. _avanti.specs.courses:

======================
Courses in Lino Avanti
======================

.. How to test just this document:

    $ python setup.py test -s tests.SpecsTests.test_courses
    
    doctest init:

    >>> import lino
    >>> lino.startup('lino_avanti.projects.avanti.settings.doctests')
    >>> from lino.api.doctest import *


.. contents::
  :local:

Note that Laura can modify the afternoon course, but not the morning
course.  That's because for the afternoon course she is also the
author.  while the morning course is managed by Nathalie.

>>> rt.login('laura').show('courses.MyCoursesGiven')
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
========================================================== =========== ============= ====== ==========================================
 overview                                                   When        Times         Room   Actions
---------------------------------------------------------- ----------- ------------- ------ ------------------------------------------
 `Alphabetisation (03/05/2015) <Detail>`__ / *Laura Lang*   Every day   14:00-17:00          **Draft** → [Active] [Inactive] [Closed]
 `Alphabetisation (03/05/2015) <Detail>`__ / *Laura Lang*   Every day   09:00-12:00          **Draft**
========================================================== =========== ============= ====== ==========================================
<BLANKLINE>


Note that even though Nathalie is author of the morning course, it is
Laura (the teacher) who is responsible for the individual events.


>>> rt.login('laura').show('cal.MyEvents')
... #doctest: +NORMALIZE_WHITESPACE -REPORT_UDIFF
=========================================== ======== =================================
 overview                                    Client   Actions
------------------------------------------- -------- ---------------------------------
 `Lesson 12 (26.05.2015 09:00) <Detail>`__            [▽] **Suggested** → [☐] [☑] [☒]
 `Lesson 12 (26.05.2015 14:00) <Detail>`__            [▽] **Suggested** → [☐] [☑] [☒]
 `Lesson 13 (28.05.2015 09:00) <Detail>`__            [▽] **Suggested** → [☐] [☑] [☒]
 `Lesson 13 (28.05.2015 14:00) <Detail>`__            [▽] **Suggested** → [☐] [☑] [☒]
 `Lesson 14 (29.05.2015 09:00) <Detail>`__            [▽] **Suggested** → [☐] [☑] [☒]
 `Lesson 14 (29.05.2015 14:00) <Detail>`__            [▽] **Suggested** → [☐] [☑] [☒]
 `Lesson 15 (01.06.2015 09:00) <Detail>`__            [▽] **Suggested** → [☐] [☑] [☒]
 `Lesson 15 (01.06.2015 14:00) <Detail>`__            [▽] **Suggested** → [☐] [☑] [☒]
 `Lesson 16 (02.06.2015 09:00) <Detail>`__            [▽] **Suggested** → [☐] [☑] [☒]
 `Lesson 16 (02.06.2015 14:00) <Detail>`__            [▽] **Suggested** → [☐] [☑] [☒]
=========================================== ======== =================================
<BLANKLINE>
