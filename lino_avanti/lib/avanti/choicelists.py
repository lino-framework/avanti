# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)

"""The choicelists for this plugin.

"""

from django.db import models

from lino.api import dd, _
from lino.modlib.system.choicelists import ObservedEvent

class Translators(dd.ChoiceList):

    """
    Types of registries for the Belgian residence.
    
    """
    verbose_name = _("Translator")

add = Translators.add_item
add('10', _("SETIS"))
add('20', _("Other"))
add('30', _("Private"))


class ClientEvents(dd.ChoiceList):
    """A choicelist of observable client events.

    """
    verbose_name = _("Observed event")
    verbose_name_plural = _("Observed events")
    max_length = 50


# class ClientIsActive(ObservedEvent):
#     text = _("Active")

#     def add_filter(self, qs, pv):
#         period = (pv.start_date, pv.end_date)
#         qs = only_coached_on(qs, period)
#         return qs

# ClientEvents.add_item_instance(ClientIsActive("active"))


class ClientHasCoaching(ObservedEvent):
    text = _("Coaching")

    def add_filter(self, qs, pv):
        period = (pv.start_date, pv.end_date)
        qs = only_coached_on(qs, period)
        return qs

ClientEvents.add_item_instance(ClientHasCoaching("active"))


class ClientCreated(ObservedEvent):
    """The choice for :class:`ClientEvents` which
    selects clients whose record has been *created* during the observed
    period.
    """
    text = _("Created")

    def add_filter(self, qs, pv):
        if pv.start_date:
            qs = qs.filter(created__gte=pv.start_date)
        if pv.end_date:
            qs = qs.filter(created__lte=pv.end_date)
        return qs

ClientEvents.add_item_instance(ClientCreated("created"))


class ClientModified(ObservedEvent):
    """The choice for :class:`ClientEvents` which selects clients whose
    main record has been *modified* during the observed period.

    """
    text = _("Modified")

    def add_filter(self, qs, pv):
        if pv.start_date:
            qs = qs.filter(modified__gte=pv.start_date)
        if pv.end_date:
            qs = qs.filter(modified__lte=pv.end_date)
        return qs

ClientEvents.add_item_instance(ClientModified("modified"))


class ClientHasDispense(ObservedEvent):
    text = _("Dispense")

    def add_filter(self, qs, pv):
        qs = qs.filter(
            dispense__end_date__gte=pv.start_date,
            dispense__start_date__lte=pv.end_date).distinct()
        return qs

ClientEvents.add_item_instance(ClientHasDispense("dispense"))


class ClientHasPenalty(ObservedEvent):
    text = _("Penalty")

    def add_filter(self, qs, pv):
        qs = qs.filter(
            dispense__end_date__gte=pv.start_date,
            dispense__start_date__lte=pv.end_date).distinct()
        return qs

ClientEvents.add_item_instance(ClientHasPenalty("penalty"))


class ClientHasNote(ObservedEvent):
    text = _("Note")

    def add_filter(self, qs, pv):
        if pv.start_date:
            qs = qs.filter(
                notes_note_set_by_project__date__gte=pv.start_date)
        if pv.end_date:
            qs = qs.filter(
                notes_note_set_by_project__date__lte=pv.end_date)
        qs = qs.annotate(
            num_notes=models.Count('notes_note_set_by_project'))
        qs = qs.filter(num_notes__gt=0)
        # print(20150519, qs.query)
        return qs

ClientEvents.add_item_instance(ClientHasNote("note"))


class ClientStates(dd.Workflow):
    required_roles = dd.required(dd.SiteStaff)
    verbose_name_plural = _("Client states")

add = ClientStates.add_item
add('10', _("New"), 'newcomer')
add('20', _("First contact"), 'refused')
add('30', _("Active"), 'coached')
add('50', _("Ended"), 'former')
