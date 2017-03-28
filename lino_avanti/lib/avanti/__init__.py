# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)

"""
The main plugin for Lino Avanti.

See :doc:`/specs/avanti`.

.. autosummary::
   :toctree:

    models
    migrate
    user_types
    layouts
    choicelists

"""


from lino.api import ad, _


class Plugin(ad.Plugin):
    "See :class:`lino.core.plugin.Plugin`."

    verbose_name = _("Master")

    needs_plugins = ['lino_xl.lib.countries']

    def setup_main_menu(self, site, profile, m):
        mg = site.plugins.contacts
        m = m.add_menu(mg.app_label, mg.verbose_name)
        m.add_action('avanti.Clients')
        m.add_action('avanti.MyClients')
        # m.add_action('avanti.Translators')
        # m.add_action('courses.CourseProviders')
        # m.add_action('coachings.CoachedClients')
        # m.add_action('coachings.MyCoachings')

    # def setup_config_menu(self, site, profile, m):
    #     m = m.add_menu(self.app_label, self.verbose_name)
    #     m.add_action('contacts.CompanyTypes')

    def setup_explorer_menu(self, site, profile, m):
        mg = site.plugins.contacts
        m = m.add_menu(mg.app_label, mg.verbose_name)
        m.add_action('avanti.AllClients')



