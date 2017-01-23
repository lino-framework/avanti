# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)


"""
The :xfile:`models.py` module for this plugin.

"""


from django.utils.translation import ugettext_lazy as _
from django.utils.translation import pgettext_lazy as pgettext

from lino_xl.lib.courses.models import *
from lino_xl.lib.courses.roles import CoursesUser

contacts = dd.resolve_app('contacts')


class CourseProvider(contacts.Company):

    """
    A CourseProvider is a Company that offers Courses. 
    """
    class Meta:
        verbose_name = _("Course provider")
        verbose_name_plural = _("Course providers")

    def disable_delete(self, ar=None):
        # skip the is_imported_partner test
        return super(contacts.Partner, self).disable_delete(ar)


class CourseProviderDetail(contacts.CompanyDetail):
    """Same as CompanyDetail, except that we add a tab
    :guilabel:`Courses`.

    """
    box5 = "remarks"
    main = "general courses.LinesByProvider"


class CourseProviders(contacts.Companies):
    """Table of all course providers

    """
    required_roles = dd.required(CoursesUser)
    model = 'courses.CourseProvider'
    detail_layout = CourseProviderDetail()



class Course(Course):
    
    class Meta(Course.Meta):
        # app_label = 'courses'
        abstract = dd.is_abstract_model(__name__, 'Course')
        verbose_name = _("Course")
        verbose_name_plural = _('Courses')

class Line(Line):
    
    class Meta(Line.Meta):
        # app_label = 'courses'
        abstract = dd.is_abstract_model(__name__, 'Course')
        verbose_name = pgettext("singular form", "Course line")
        verbose_name_plural = pgettext("plural form", 'Course lines')

    provider = dd.ForeignKey(
        'courses.CourseProvider', blank=True, null=True)
    
