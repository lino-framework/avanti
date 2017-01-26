# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""General demo data for Lino Avanti.

- Course providers and courses

"""

# from __future__ import unicode_literals
# from django.conf import settings
# from lino.utils import mti
# from lino.utils import Cycler, join_words
# from lino.utils.instantiator import create_row
from lino.api import rt, dd, _


def objects():

    Line = rt.models.courses.Line
    
    def series(name, **kwargs):
        return Line(name=name, **kwargs)

    yield series(_("Citizen"))
    yield series(_("Alphabetisation"))
    yield series(_("German for beginners"))
    yield series(_("German A1+"))
    yield series(_("German A2"))
    yield series(_("German A2 (women)"))
        
