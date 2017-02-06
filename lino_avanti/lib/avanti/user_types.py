# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)


"""Defines the standard user roles for Lino Avanti."""


# from lino.core.roles import UserRole, SiteAdmin, SiteUser, SiteStaff
# from lino.core.roles import UserRole, SiteAdmin, SiteStaff
from lino.core.roles import UserRole, SiteAdmin
from lino.modlib.users.choicelists import UserTypes
from django.utils.translation import ugettext_lazy as _

from lino_xl.lib.contacts.roles import ContactsUser, ContactsStaff
# from lino_xl.lib.cal.roles import CalendarUser, CalendarStaff
from lino_xl.lib.coachings.roles import CoachingsUser, CoachingsStaff
from lino_xl.lib.excerpts.roles import ExcerptsUser, ExcerptsStaff
from lino_xl.lib.courses.roles import CoursesTeacher, CoursesUser
from lino_xl.lib.cv.roles import CareerUser, CareerStaff
from lino_xl.lib.beid.roles import BeIdUser
from lino.modlib.office.roles import OfficeUser, OfficeStaff


class Teacher(CoursesTeacher, ExcerptsUser, OfficeUser):
    pass

class SocialWorker(CoachingsUser, CoursesUser, ContactsUser, OfficeUser,
                   ExcerptsUser, CareerUser, BeIdUser):
    pass

class SiteStaff(SocialWorker, CoachingsStaff, CoursesUser,
                ContactsStaff, OfficeStaff, ExcerptsStaff,
                CareerStaff, BeIdUser):
    pass

class Administrator(SiteAdmin, SiteStaff):
    pass

UserTypes.clear()
add = UserTypes.add_item
add('000', _("Anonymous"), UserRole, 'anonymous',
    readonly=True, authenticated=False)
add('100', _("Teacher"), Teacher, name='teacher')
add('200', _("Social worker"), SocialWorker, name='user')
add('800', _("Staff"), SiteStaff, name='staff')
add('900', _("Administrator"), Administrator, name='admin')
