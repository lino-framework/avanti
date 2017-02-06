# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)

"""The :xfile:`models.py` module for this plugin.

"""
from lino.api import dd, rt, _
from django.db import models
from django.conf import settings

from lino.utils import ssin
from lino.mixins import Phonable, Contactable
from lino_xl.lib.beid.mixins import BeIdCardHolder

# from lino.modlib.notify.mixins import ChangeObservable
# from lino_xl.lib.notes.choicelists import SpecialTypes
from lino_xl.lib.notes.mixins import Notable
from lino_xl.lib.coachings.mixins import Coachable

from lino.mixins import ObservedPeriod

from lino_xl.lib.coachings.choicelists import ClientEvents, ClientStates

from .choicelists import TranslatorTypes, StartingReasons, EndingReasons

contacts = dd.resolve_app('contacts')


@dd.python_2_unicode_compatible
class Client(contacts.Person, BeIdCardHolder, Coachable, Notable):
    """
    A **client** is a person using our services.

    .. attribute:: overview

        A panel with general information about this client.

    .. attribute:: client_state
    
        Pointer to :class:`ClientStates`.

    .. attribute:: unemployed_since

       The date when this client got unemployed and stopped to have a
       regular work.

    .. attribute:: seeking_since

       The date when this client registered as unemployed and started
       to look for a new job.

    .. attribute:: work_permit_suspended_until

    """
    class Meta:
        app_label = 'avanti'
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")
        abstract = dd.is_abstract_model(__name__, 'Client')
        #~ ordering = ['last_name','first_name']

    validate_national_id = True
    # workflow_state_field = 'client_state'

    in_belgium_since = models.DateField(
        _("Lives in Belgium since"), blank=True, null=True)
    
    starting_reason = StartingReasons.field(blank=True)
    ending_reason = EndingReasons.field(blank=True)
    
    translator_type = TranslatorTypes.field(blank=True)
    translator_notes = dd.RichTextField(
        _("Translator"), blank=True, format='plain')
    # translator = dd.ForeignKey(
    #     "avanti.Translator",
    #     blank=True, null=True)

    unemployed_since = models.DateField(
        _("Unemployed since"), blank=True, null=True,
        help_text=_("Since when the client has not been employed "
                    "in any regular job."))
    seeking_since = models.DateField(
        _("Seeking work since"), blank=True, null=True,
        help_text=_("Since when the client is seeking for a job."))
    needs_work_permit = models.BooleanField(
        _("Needs work permit"), default=False)
    work_permit_suspended_until = models.DateField(
        blank=True, null=True, verbose_name=_("suspended until"))

    declared_name = models.BooleanField(_("Declared name"), default=False)

    # is_seeking = models.BooleanField(_("is seeking work"), default=False)
    # removed in chatelet, maybe soon also in Eupen (replaced by seeking_since)

    unavailable_until = models.DateField(
        blank=True, null=True, verbose_name=_("Unavailable until"))
    unavailable_why = models.CharField(
        _("reason"), max_length=100,
        blank=True)

    family_notes = models.TextField(
        _("Family situation"), blank=True, null=True)
    
    residence_notes = models.TextField(
        _("Residential situation"), blank=True, null=True)
    
    health_notes = models.TextField(
        _("Health situation"), blank=True, null=True)
    
    financial_notes = models.TextField(
        _("Financial situation"), blank=True, null=True)
    
    integration_notes = models.TextField(
        _("Integration notes"), blank=True, null=True)
    
    # obstacles = models.TextField(
    #     _("Other obstacles"), blank=True, null=True)
    # skills = models.TextField(
    #     _("Other skills"), blank=True, null=True)

    # client_state = ClientStates.field(
    #     default=ClientStates.newcomer.as_callable)


    def __str__(self):
        return "%s %s (%s)" % (
            self.last_name.upper(), self.first_name, self.pk)

    @dd.displayfield(_("Name"))
    def name_column(self, request):
        return str(self)

    def get_overview_elems(self, ar):
        elems = super(Client, self).get_overview_elems(ar)
        # elems.append(E.br())
        elems.append(ar.get_data_value(self, 'eid_info'))
        # notes = []
        # for note in rt.modules.notes.Note.objects.filter(
        #         project=self, important=True):
        #     notes.append(E.b(ar.obj2html(note, note.subject)))
        # if len(notes):
        #     notes = join_elems(notes, " / ")
        #     elems += E.p(*notes, class_="lino-info-red")
        return elems

    def update_owned_instance(self, owned):
        owned.project = self
        super(Client, self).update_owned_instance(owned)

    # def full_clean(self, *args, **kw):
    #     if self.national_id:
    #         ssin.ssin_validator(self.national_id)
    #     super(Client, self).full_clean(*args, **kw)

    def properties_list(self, *prop_ids):
        """Yields a list of the :class:`PersonProperty
        <lino_welfare.modlib.cv.models.PersonProperty>` properties of
        this person in the specified order.  If this person has no
        entry for a requested :class:`Property`, it is simply skipped.
        Used in :xfile:`cv.odt`.  `

        """
        return rt.models.cv.properties_list(self, *prop_ids)


class ClientDetail(dd.DetailLayout):

    main = "general contact person family \
    coaching career courses misc "

    general = dd.Panel("""
    overview:30 general2:40 image:15
    
    tickets.TicketsByEndUser cal.EventsByProject
    """, label=_("General"))

    general2 = """
    id:10 gender:10  age:10
    national_id:15 birth_date 
    starting_reason 
    client_state primary_coach
    ending_reason
    # workflow_buttons 
    """

    translator_left = """
    language 
    translator_type
    """

    contact = dd.Panel("""
    translator_left translator_notes
    address general3
    coachings.ContactsByClient
    """, label=_("Contact"))

    general3 = """
    email
    phone
    fax
    gsm
    """

    address = """
    country city zip_code:10
    addr1
    street:25 street_no #street_box
    addr2
    """

    family = dd.Panel("""
    family_notes:50 households.MembersByPerson:20
    #humanlinks.LinksByHuman:30
    households.SiblingsByPerson
    """, label=_("Family"))

    person = dd.Panel("""
    first_name middle_name last_name declared_name 
    nationality:15 birth_country birth_place 
    in_belgium_since needs_work_permit
    # uploads.UploadsByClient
    ResidencesByPerson residence_notes
    """, label=_("Person"))

    coaching = dd.Panel("""
    notes.NotesByProject
    coachings.CoachingsByClient
    """,label = _("Coaching"))

    courses = dd.Panel("""
    courses.EnrolmentsByPupil
    """,label = _("Courses"))

    misc = dd.Panel("""
    # unavailable_until:15 unavailable_why:30
    financial_notes health_notes integration_notes
    plausibility.ProblemsByOwner excerpts.ExcerptsByProject
    """, label=_("Miscellaneous"))

    career = dd.Panel("""
    unemployed_since seeking_since work_permit_suspended_until
    cv.StudiesByPerson cv.LanguageKnowledgesByPerson 
    # cv.TrainingsByPerson
    cv.ExperiencesByPerson:40
    """, label=_("Career"))

    # competences = dd.Panel("""
    # skills
    # obstacles
    # """, label=_("Competences"))


# Client.hide_elements('street_prefix', 'addr2')


class Clients(contacts.Persons):
    """Base class for most lists of clients.

    .. attribute:: client_state

        If not empty, show only Clients whose `client_state` equals
        the specified value.

    """
    model = 'avanti.Client'
    # params_panel_hidden = True

    # insert_layout = dd.InsertLayout("""
    # first_name last_name
    # national_id
    # gender language
    # """, window_size=(60, 'auto'))

    column_names = "name_column:20 client_state national_id:10 \
    gsm:10 address_column age:10 email phone:10 id language:10"

    detail_layout = ClientDetail()

    parameters = ObservedPeriod(
        nationality=dd.ForeignKey(
            'countries.Country', blank=True, null=True,
            verbose_name=_("Nationality")),
        observed_event=ClientEvents.field(blank=True),
        client_state=ClientStates.field(blank=True))
    params_layout = """
    aged_from aged_to gender nationality 
    client_state start_date end_date observed_event 
    """

    @classmethod
    def get_request_queryset(self, ar):
        """This converts the values of the different parameter panel fields to
        the query filter.


        """
        qs = super(Clients, self).get_request_queryset(ar)

        pv = ar.param_values
        period = [pv.start_date, pv.end_date]
        if period[0] is None:
            period[0] = period[1] or dd.today()
        if period[1] is None:
            period[1] = period[0]

        ce = pv.observed_event
        if ce:
            qs = ce.add_filter(qs, pv)

        # if ce is None:
        #     pass
        # elif ce == ClientEvents.active:
        #     pass
        # elif ce == ClientEvents.isip:
        #     flt = has_contracts_filter('isip_contract_set_by_client', period)
        #     qs = qs.filter(flt).distinct()
        # elif ce == ClientEvents.jobs:
        #     flt = has_contracts_filter('jobs_contract_set_by_client', period)
        #     qs = qs.filter(flt).distinct()
        # elif dd.is_installed('immersion') and ce == ClientEvents.immersion:
        #     flt = has_contracts_filter(
        #         'immersion_contract_set_by_client', period)
        #     qs = qs.filter(flt).distinct()

        # elif ce == ClientEvents.available:
        #     # Build a condition "has some ISIP or some jobs.Contract
        #     # or some immersion.Contract" and then `exclude` it.
        #     flt = has_contracts_filter('isip_contract_set_by_client', period)
        #     flt |= has_contracts_filter('jobs_contract_set_by_client', period)
        #     if dd.is_installed('immersion'):
        #         flt |= has_contracts_filter(
        #             'immersion_contract_set_by_client', period)
        #     qs = qs.exclude(flt).distinct()


        if pv.client_state:
            qs = qs.filter(client_state=pv.client_state)

        if pv.nationality:
            qs = qs.filter(nationality__exact=pv.nationality)

        # print(20150305, qs.query)

        return qs

    @classmethod
    def get_title_tags(self, ar):
        for t in super(Clients, self).get_title_tags(ar):
            yield t
        pv = ar.param_values

        if pv.observed_event:
            yield unicode(pv.observed_event)

        if pv.client_state:
            yield unicode(pv.client_state)

        if pv.start_date is None or pv.end_date is None:
            period = None
        else:
            period = daterange_text(
                pv.start_date, pv.end_date)

    @classmethod
    def apply_cell_format(self, ar, row, col, recno, td):
        if row.client_state == ClientStates.newcomer:
            td.attrib.update(bgcolor="green")

    @classmethod
    def get_row_classes(cls, obj, ar):
        if obj.client_state == ClientStates.newcomer:
            yield 'green'
        elif obj.client_state in (ClientStates.refused, ClientStates.former):
            yield 'yellow'
        #~ if not obj.has_valid_card_data():
            #~ return 'red'


class AllClients(Clients):
    column_names = "name_column:20 client_state national_id:10 \
    gsm:10 address_column age:10 email phone:10 id *"
    required_roles = dd.required(dd.SiteStaff)


class ClientsByNationality(Clients):
    master_key = 'nationality'
    order_by = "city name".split()
    column_names = "city street street_no street_box addr2 name_column country language *"


# class ClientsByTranslator(Clients):
#     master_key = 'translator'

from lino_xl.lib.countries.mixins import CountryCity
from lino_xl.lib.cv.mixins import PersonHistoryEntry, HistoryByPerson

    
class Residence(PersonHistoryEntry, CountryCity):

    class Meta:
        app_label = 'avanti'
        verbose_name = _("Residence")
        verbose_name_plural = _("Residences")

    reason = models.CharField(_("Reason"), max_length=200, blank=True)



class Residences(dd.Table):
    model = 'avanti.Residence'
    
class ResidencesByPerson(HistoryByPerson, Residences):
    column_names = 'country city start_date end_date reason *'
    auto_fit_column_widths = True
