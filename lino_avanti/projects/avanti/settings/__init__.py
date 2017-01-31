# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)

"""

.. autosummary::
   :toctree:

   doctests
   demo
   memory
   fixtures



"""

from __future__ import print_function
from __future__ import unicode_literals

from lino.projects.std.settings import *
from lino.api.ad import _


class Site(Site):

    verbose_name = "Lino Avanti!"
    version = '2017.1.0'
    url = "http://avanti.lino-framework.org/"
    demo_fixtures = ['std', 'all_languages', 'demo', 'demo2']
    user_types_module = 'lino_avanti.lib.avanti.roles'
    # user_types_module = 'lino_noi.lib.noi.roles'
    workflows_module = 'lino_noi.lib.noi.workflows'
    migration_class = 'lino_avanti.lib.avanti.migrate.Migrator'

    project_model = 'avanti.Client'
    textfield_format = 'html'

    def setup_plugins(self):
        super(Site, self).setup_plugins()
        self.plugins.cv.configure(
            person_model = 'avanti.Client')
        self.plugins.humanlinks.configure(
            person_model = 'avanti.Client')
        self.plugins.households.configure(
            person_model='avanti.Client')
        self.plugins.cal.configure(
            partner_model='avanti.Client')
        self.plugins.tickets.configure(
            end_user_model='avanti.Client')
        self.plugins.courses.configure(
            teacher_model='users.User',
            pupil_model='avanti.Client',
            pupil_name_fields='pupil__last_name pupil__first_name')
        self.plugins.coachings.configure(client_model='avanti.Client')

    def get_installed_apps(self):
        """Implements :meth:`lino.core.site.Site.get_installed_apps`.

        """
        yield super(Site, self).get_installed_apps()
        yield 'lino.modlib.users'
        yield 'lino_xl.lib.countries'
        yield 'lino_avanti.lib.contacts'
        yield 'lino_avanti.lib.avanti'
        yield 'lino_xl.lib.households'
        # yield 'lino_welfare.modlib.households'
        yield 'lino_xl.lib.humanlinks'
        yield 'lino_xl.lib.lists'
        yield 'lino_xl.lib.notes'
        yield 'lino_xl.lib.beid'
        yield 'lino_xl.lib.coachings'
        yield 'lino_xl.lib.cv'
        
        # yield 'lino_avanti.lib.courses' # seems that course providers
        #                                 # are not needed.
        yield 'lino_xl.lib.courses'
        # yield 'lino_xl.lib.rooms'
        
        yield 'lino.modlib.plausibility'
        yield 'lino.modlib.export_excel'
        yield 'lino.modlib.tinymce'
        yield 'lino.modlib.weasyprint'
        yield 'lino_xl.lib.excerpts'
        yield 'lino_xl.lib.appypod'
        
        yield 'lino_noi.lib.faculties'
        yield 'lino_noi.lib.votes'
        yield 'lino_avanti.lib.tickets'
        # yield 'lino_noi.lib.tickets'
        

    def setup_quicklinks(self, user, tb):
        super(Site, self).setup_quicklinks(user, tb)
        a = self.actors.users.MySettings.default_action
        tb.add_instance_action(
            user, action=a, label=_("My settings"))

        Clients = self.actors.avanti.Clients
        tb.add_action(Clients)
        tb.add_action(
            Clients.insert_action,
            label=_("New {}").format(
                Clients.model._meta.verbose_name))
        tb.add_action(Clients, 'find_by_beid')
        
        # tb.add_action(self.modules.tickets.MyTickets)
        # tb.add_action(self.modules.tickets.TicketsToTriage)
        # tb.add_action(self.modules.tickets.TicketsToTalk)
        # tb.add_action(self.modules.tickets.TicketsToDo)
        tb.add_action(self.modules.tickets.AllTickets)
        tb.add_action(
            self.modules.tickets.MyTickets.insert_action,
            label=_("Submit a ticket"))


# the following line should not be active in a checked-in version
# DATABASES['default']['NAME'] = ':memory:'

USE_TZ = True
TIME_ZONE = 'UTC'

