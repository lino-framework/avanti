# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)

"""See :doc:`/specs/avanti/courses`.


"""


from lino_xl.lib.courses import Plugin


class Plugin(Plugin):

    extends_models = ['Course', 'Enrolment']
