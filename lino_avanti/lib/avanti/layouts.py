# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre

"""The default :attr:`custom_layouts_module
<lino.core.site.Site.custom_layouts_module>` for Lino Avanti.

"""

from lino.api import dd, rt

rt.actors.system.SiteConfigs.detail_layout = dd.DetailLayout("""
site_company next_partner_id:10
default_build_method simulate_today
site_calendar default_event_type #pupil_guestrole
max_auto_events hide_events_before
""", size=(60, 'auto'))

