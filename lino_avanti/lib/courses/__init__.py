# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)

"""Extends :mod:`lino_xl.lib.courses` for :ref:`avanti`.

.. autosummary::
   :toctree:

    models

"""


from lino_xl.lib.courses import Plugin


class Plugin(Plugin):

    extends_models = ['Course']
