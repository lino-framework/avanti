# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
#
# License: BSD (see file COPYING for details)

"""Default workflows for Lino Avanti.

This can be used as :attr:`workflows_module
<lino.core.site.Site.workflows_module>`

"""

from __future__ import unicode_literals

# calendar events and presences:
from lino_xl.lib.cal.workflows.voga import *
# from lino_xl.lib.cal.workflows import feedback


# courses and enrolments:
from lino_xl.lib.courses.workflows import *
from lino_noi.lib.noi.workflows import *

from lino.api import _, pgettext
from lino_xl.lib.coachings.choicelists import ClientStates
ClientStates.clear()
add = ClientStates.add_item
add('10', _("Newcomer"), 'newcomer')  # "first contact" in Avanti
add('20', pgettext("client state", "Registered"), 'coached')
add('30', _("Ended"), 'former')
add('40', _("Abandoned"), 'refused')

# alias
# ClientStates.coached = ClientStates.newcomer
