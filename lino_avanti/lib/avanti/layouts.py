# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre

"""The default :attr:`custom_layouts_module
<lino.core.site.Site.custom_layouts_module>` for Lino Avanti.

"""

from lino.api import dd, rt, _

rt.actors.system.SiteConfigs.detail_layout = dd.DetailLayout("""
site_company next_partner_id:10
default_build_method simulate_today
site_calendar default_event_type #pupil_guestrole
max_auto_events hide_events_before
""", size=(60, 'auto'))

rt.actors.courses.AllEnrolments.column_names = \
'id #request_date #start_date #end_date #user course \
pupil__birth_date pupil__age pupil__country pupil__city \
pupil__gender state'

dd.update_field(
    rt.models.contacts.Partner, 'language',
    verbose_name=_("Contact language"))

# rt.actors.cv.LanguageKnowledgesByPerson.slave_grid_format = 'grid'
