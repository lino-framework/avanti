# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)


"""Defines the standard user roles for Lino Avanti."""


from lino.core.roles import UserRole, SiteAdmin, SiteUser, SiteStaff
from lino.modlib.users.choicelists import UserTypes
from django.utils.translation import ugettext_lazy as _

from lino_xl.lib.contacts.roles import ContactsUser, ContactsStaff
from lino_xl.lib.excerpts.roles import ExcerptsUser, ExcerptsStaff
from lino_xl.lib.courses.roles import CoursesUser
from lino.modlib.office.roles import OfficeUser, OfficeStaff

UserTypes.clear()
add = UserTypes.add_item
add('000', _("Anonymous"), UserRole, 'anonymous',
    readonly=True, authenticated=False)
add('100', _("User"),
    (SiteUser, CoursesUser, ContactsUser, OfficeUser, ExcerptsUser),
    name='user')
add('500', _("Staff"),
    (SiteStaff, CoursesUser, ContactsStaff, OfficeStaff, ExcerptsStaff),
    name='staff')
add('900', _("Administrator"),
    (SiteAdmin, CoursesUser, ContactsStaff, OfficeStaff, ExcerptsStaff),
    name='admin')
