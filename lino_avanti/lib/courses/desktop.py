# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)




from lino_xl.lib.courses.desktop import *

# class LinesByProvider(Lines):
#     master_key = 'provider'

AllEnrolments.column_names = "id request_date start_date end_date \
user course pupil pupil__birth_date pupil__age pupil__country \
pupil__city pupil__gender"

class EnrolmentsByCourse(EnrolmentsByCourse):
    column_names = 'request_date pupil pupil__gender ' \
                   'needs_childcare needs_school needs_bus needs_evening '\
                   'remark workflow_buttons *'

    
