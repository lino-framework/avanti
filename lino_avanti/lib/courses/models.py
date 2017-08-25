# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)



from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext_lazy as pgettext

from lino_xl.lib.courses.models import *
from lino_xl.lib.courses.roles import CoursesUser
from lino.modlib.plausibility.choicelists import Checker
from lino.core.gfks import gfk2lookup

# contacts = dd.resolve_app('contacts')


# class CourseProvider(contacts.Company):

#     """
#     A CourseProvider is a Company that offers Courses. 
#     """
#     class Meta:
#         app_label = 'courses'
#         verbose_name = _("Course provider")
#         verbose_name_plural = _("Course providers")

#     def disable_delete(self, ar=None):
#         # skip the is_imported_partner test
#         return super(contacts.Partner, self).disable_delete(ar)


# class CourseProviderDetail(contacts.CompanyDetail):
#     """Same as CompanyDetail, except that we add a tab
#     :guilabel:`Courses`.

#     """
#     box5 = "remarks"
#     main = "general courses.LinesByProvider"


# class CourseProviders(contacts.Companies):
#     """Table of all course providers

#     """
#     required_roles = dd.login_required(CoursesUser)
#     model = 'courses.CourseProvider'
#     detail_layout = CourseProviderDetail()



class Course(Course):
    
    class Meta(Course.Meta):
        # app_label = 'courses'
        abstract = dd.is_abstract_model(__name__, 'Course')
        # verbose_name = _("Course")
        # verbose_name_plural = _('Courses')

    @dd.virtualfield(models.IntegerField(_("Bus")))
    def bus_needed(self, ar):
        return self.get_places_sum(
            state=EnrolmentStates.requested, needs_bus=True)

    @dd.virtualfield(models.IntegerField(_("Childcare")))
    def childcare_needed(self, ar):
        return self.get_places_sum(
            state=EnrolmentStates.requested, needs_childcare=True)

    @dd.virtualfield(models.IntegerField(_("Evening")))
    def evening_needed(self, ar):
        return self.get_places_sum(
            state=EnrolmentStates.requested, needs_evening=True)

    @dd.virtualfield(models.IntegerField(_("School")))
    def school_needed(self, ar):
        return self.get_places_sum(
            state=EnrolmentStates.requested, needs_school=True)

    
# class Line(Line):
    
#     class Meta(Line.Meta):
#         # app_label = 'courses'
#         abstract = dd.is_abstract_model(__name__, 'Course')
#         verbose_name = pgettext("singular form", "Course line")
#         verbose_name_plural = pgettext("plural form", 'Course lines')

#     provider = dd.ForeignKey(
#         'courses.CourseProvider', blank=True, null=True)
    

class Enrolment(Enrolment):
   
    class Meta(Enrolment.Meta):
        abstract = dd.is_abstract_model(__name__, 'Enrolment')

    needs_childcare = models.BooleanField(_("Childcare"), default=False)
    needs_bus = models.BooleanField(_("Bus"), default=False)
    needs_school = models.BooleanField(_("School"), default=False)
    needs_evening = models.BooleanField(_("Evening"), default=False)
        



class EnrolmentChecker(Checker):
    verbose_name = _("Check for unsufficient presences")
    model = Enrolment
    messages = dict(
        msg_absent=_("More than 2 times absent."),
        msg_missed=_("Missed more than 10% of meetings."),
    )
    
    def get_plausibility_problems(self, obj, fix=False):
        Guest = rt.models.cal.Guest
        GuestStates = rt.models.cal.GuestStates
        Event = rt.models.cal.Event
        EntryStates = rt.models.cal.EntryStates
        eflt = gfk2lookup(Event.owner, obj.course)
        gflt = { 'event__'+k: v for k, v in eflt.items() }
        qs = Guest.objects.filter(partner=obj.pupil, **gflt)
        # qs = qs.filter(**gfk2lookup(Guest.course, obj.course))
        absent = qs.filter(state=GuestStates.absent).count()
        if absent > 2:
            yield (False, self.messages['msg_absent'])
            return
        events = Event.objects.filter(**eflt)
        events = events.filter(state=EntryStates.took_place)
        ecount = events.count()
        if ecount > 9:
            excused = qs.filter(state=GuestStates.excused).count()
            missing = absent + excused
            max_missing = ecount / 10 - 1
            if missing > max_missing:
                yield (False, self.messages['msg_missed'])
                return
    

EnrolmentChecker.activate()
    
