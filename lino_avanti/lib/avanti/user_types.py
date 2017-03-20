# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)


"""Defines the standard user roles for Lino Avanti."""


from django.utils.translation import ugettext_lazy as _

# from lino.core.roles import UserRole, SiteAdmin, SiteUser, SiteStaff
# from lino.core.roles import UserRole, SiteAdmin, SiteStaff
from lino.core.roles import UserRole, Explorer, SiteAdmin
from lino.modlib.users.choicelists import UserTypes
from lino.modlib.comments.roles import CommentsUser, CommentsStaff
from lino.modlib.office.roles import OfficeUser, OfficeStaff
from lino_xl.lib.contacts.roles import ContactsUser, ContactsStaff
# from lino_xl.lib.cal.roles import CalendarUser, CalendarStaff
from lino_xl.lib.coachings.roles import CoachingsUser, CoachingsStaff
from lino_xl.lib.excerpts.roles import ExcerptsUser, ExcerptsStaff
from lino_xl.lib.courses.roles import CoursesTeacher, CoursesUser
from .roles import ClientsNameUser, ClientsUser, ClientsStaff
from lino_xl.lib.cv.roles import CareerUser, CareerStaff
from lino_xl.lib.beid.roles import BeIdUser
from lino_xl.lib.tickets.roles import TicketsUser, TicketsStaff
from lino_xl.lib.trends.roles import TrendsStaff, TrendsUser


class Auditor(CoursesUser, OfficeUser, Explorer):
    pass

class Teacher(CoursesTeacher, OfficeUser, ClientsNameUser):
    pass

class Coordinator(CoursesUser, OfficeUser):
    pass

class SocialWorker(CoachingsUser, CoursesUser, ContactsUser,
                   OfficeUser, ExcerptsUser, CareerUser, BeIdUser,
                   TicketsUser, CommentsUser, TrendsUser, ClientsUser,
                   Explorer):
    pass

class SiteStaff(SocialWorker, CoachingsStaff, CoursesUser,
                ContactsStaff, OfficeStaff, ExcerptsStaff,
                CareerStaff, BeIdUser, TicketsStaff, CommentsStaff,
                TrendsStaff, ClientsStaff, Explorer):
    pass

class Administrator(SiteAdmin, SiteStaff):
    pass

UserTypes.clear()
add = UserTypes.add_item
add('000', _("Anonymous"), UserRole, 'anonymous',
    readonly=True, authenticated=False)
add('100', _("Teacher"), Teacher, name='teacher')
add('200', _("Social worker"), SocialWorker, name='user')
add('300', _("Auditor"), Auditor, name='auditor', readonly=True)
add('400', _("Coordinator"), Coordinator, name='coordinator')
add('800', _("Staff"), SiteStaff, name='staff')
add('900', _("Administrator"), Administrator, name='admin')
