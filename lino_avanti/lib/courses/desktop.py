# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)


from lino_xl.lib.courses.desktop import *
from lino.api import _

from lino.core.gfks import gfk2lookup
from lino.utils import join_elems
from lino.utils.xmlgen.html import E


# Courses.required_roles = dd.login_required(Explorer)


# class LinesByProvider(Lines):
#     master_key = 'provider'

AllEnrolments.column_names = "id request_date start_date end_date \
user course pupil pupil__birth_date pupil__age pupil__country \
pupil__city pupil__gender"

class EnrolmentsByCourse(EnrolmentsByCourse):
    column_names = 'id request_date pupil pupil__gender ' \
                   'needs_childcare needs_school needs_bus needs_evening '\
                   'remark workflow_buttons *'

class PresencesByEnrolment(dd.Table):
    model = 'cal.Guest'
    master = 'courses.Enrolment'
    column_names = "event event__state workflow_buttons remark *"
    slave_grid_format = "summary"

    @classmethod
    def get_filter_kw(self, ar, **kw):
        Event = rt.models.cal.Event
        enr = ar.master_instance
        if enr is None:
            return None
        for k, v in gfk2lookup(Event.owner, enr.course).items():
            kw['event__'+k] = v
        kw.update(partner=enr.pupil)
        return super(PresencesByEnrolment, self).get_filter_kw(ar, **kw)

    @classmethod
    def get_slave_summary(self, obj, ar):
        if ar is None:
            return ''
        sar = self.request_from(ar, master_instance=obj)

        coll = {}
        for obj in sar:
            if obj.state in coll:
                coll[obj.state] += 1
            else:
                coll[obj.state] = 1
                
        ul = []
        for st in rt.models.cal.GuestStates.get_list_items():
            ul.append(_("{} : {}").format(st, coll.get(st, 0)))
        # elems = join_elems(ul, sep=', ')
        elems = join_elems(ul, sep=E.br)
        return ar.html_text(E.div(*elems))
        # return E.div(class_="htmlText", *elems)

# class CourseDetail(CourseDetail):
#     main = "general cal_tab enrolments"
    
#     general = dd.Panel("""
#     line teacher start_date end_date start_time end_time
#     room #slot workflow_buttons id:8 user
#     name
#     description
#     """, label=_("General"))
    
#     cal_tab = dd.Panel("""
#     max_events max_date every_unit every
#     monday tuesday wednesday thursday friday saturday sunday
#     cal.EntriesByController
#     """, label=_("Calendar"))

#     enrolments_top = 'enrolments_until max_places:10 confirmed free_places:10 print_actions:15'

#     enrolments = dd.Panel("""
#     enrolments_top
#     EnrolmentsByCourse
#     """, label=_("Enrolments"))

    
Enrolments.detail_layout = """
request_date user start_date end_date
course pupil
needs_childcare needs_school needs_bus needs_evening
remark workflow_buttons
confirmation_details PresencesByEnrolment
"""

class CoursesPlanning(Activities):
    required_roles = dd.login_required(CoursesUser)
    label = _("Course planning")
    column_names = \
        "overview state "\
        "max_places requested confirmed trying free_places " \
        "school_needed childcare_needed bus_needed evening_needed *"
