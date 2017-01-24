# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)

"""The choicelists for this plugin.

"""

from lino.api import dd, _


class TranslatorTypes(dd.ChoiceList):

    """
    Types of registries for the Belgian residence.
    
    """
    verbose_name = _("Translator")

add = TranslatorTypes.add_item
add('10', _("SETIS"))
add('20', _("Other"))
add('30', _("Private"))



class StartingReasons(dd.ChoiceList):

    verbose_name = _("Starting reason")

add = StartingReasons.add_item
add('100', _("Voluntarily"))
add('200', _("Mandatory"))

class EndingReasons(dd.ChoiceList):

    verbose_name = _("Ending reason")

add = EndingReasons.add_item
add('100', _("Return to home country"))
add('200', _("Illness"))
add('300', _("Familiar reasons"))
add('400', _("Missing motivation"))
add('900', _("Other"))

