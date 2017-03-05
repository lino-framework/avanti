# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""General demo data for Lino Avanti.

- Course providers and courses

"""

from __future__ import unicode_literals

# from django.conf import settings
# from lino.utils import mti
from lino.utils import Cycler  # join_words
# from lino.utils.instantiator import create_row
from lino.api import rt, dd, _

from lino.modlib.users.choicelists import UserTypes
from lino_xl.lib.cal.choicelists import Recurrencies
from lino_xl.lib.courses.choicelists import EnrolmentStates

def objects():

    Line = rt.models.courses.Line
    Teacher = dd.plugins.courses.teacher_model
    Course = rt.models.courses.Course
    Enrolment = rt.models.courses.Enrolment
    ClientContactType = rt.models.coachings.ClientContactType
    CoachingType = rt.models.coachings.CoachingType
    User = rt.models.users.User
    EventType = rt.modules.cal.EventType
    GuestRole = rt.modules.cal.GuestRole
    Person = rt.models.contacts.Person
    CommentType = rt.models.comments.CommentType
    
    def named(model, name, **kwargs):
        kwargs = dd.str2kw('name', name, **kwargs)
        return model(**kwargs)

    kw = dd.str2kw('name', _("Lesson"))
    kw.update(dd.str2kw('event_label', _("Lesson")))
    event_type = EventType(**kw)
    yield event_type

    pupil = named(GuestRole, _("Pupil"))
    yield pupil
    yield named(GuestRole, _("Assistant"))

    kw = dict(event_type=event_type, guest_role=pupil)

    yield named(Line, _("Citizen"), **kw)
    alpha = named(Line, _("Alphabetisation"), **kw)
    yield alpha
    yield named(Line, _("German for beginners"), **kw)
    yield named(Line, _("German A1+"), **kw)
    yield named(Line, _("German A2"), **kw)
    yield named(Line, _("German A2 (women)"), **kw)
        
    yield named(ClientContactType, _("Health insurance"))
    yield named(ClientContactType, _("School"))
    yield named(ClientContactType, _("Pharmacy"))
    
    yield named(CoachingType, _("Parcours"))
    yield named(CoachingType, _("GSS"))
    yield named(CoachingType, _("ISS"))
    
    yield named(CommentType, _("Phone call"))
    yield named(CommentType, _("Visit"))
    yield named(CommentType, _("Individual consultation"))
    yield named(CommentType, _("Internal meeting"))
    yield named(CommentType, _("Meeting with partners"))
    
    tom = Teacher(first_name="Tom", last_name="Thess-Thönnes")
    yield tom
    yield User(username="tom", profile=UserTypes.teacher,
               partner=tom)
    
    yield User(username="nathalie", profile=UserTypes.user)
    yield User(username="audrey", profile=UserTypes.auditor)
    yield User(username="martina", profile=UserTypes.coordinator)

    USERS = Cycler(User.objects.all())
    
    kw = dict(monday=True, tuesday=True, thursday=True, friday=True)
    kw.update(
        line=alpha,
        start_date=dd.demo_date(-20),
        start_time="9:00", end_time="12:00",
        max_date=dd.demo_date(10),
        every_unit=Recurrencies.daily,
        user=USERS.pop(),
        teacher=tom,
        max_places=5)
    
    yield Course(**kw)

    kw.update(start_time="14:00", end_time="17:00", user=USERS.pop())
    yield Course(**kw)

    
    PUPILS = Cycler(dd.plugins.courses.pupil_model.objects.all())
    # print(20170302, dd.plugins.courses.pupil_model.objects.all())
    COURSES = Cycler(Course.objects.all())
    STATES = Cycler(EnrolmentStates.objects())

    def fits(course, pupil):
        if course.max_places and course.get_free_places() == 0:
            return False
        if Enrolment.objects.filter(course=course, pupil=pupil).count():
            return False
        return True
    for i in range(10):
        course = COURSES.pop()
        pupil = PUPILS.pop()
        while not fits(course, pupil):
            course = COURSES.pop()
        kw = dict(user=USERS.pop(), course=course, pupil=pupil)
        kw.update(request_date=dd.demo_date(-i))
        kw.update(state=STATES.pop())
        yield Enrolment(**kw)


    ar = rt.login('robin')
    for obj in Course.objects.all():
        obj.update_reminders(ar)
