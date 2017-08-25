# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)

"""See :doc:`/specs/avanti/courses`.


"""


from lino_xl.lib.courses import Plugin


class Plugin(Plugin):

    extends_models = ['Course', 'Enrolment']
    
    def setup_main_menu(self, site, user_type, main):
        super(Plugin, self).setup_main_menu(site, user_type, main)
        m = main.add_menu(self.app_label, self.verbose_name)
        m.add_action('courses.CoursesPlanning')
