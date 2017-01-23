# -*- coding: UTF-8 -*-
# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""General demo data for Lino Avanti.

"""

from __future__ import unicode_literals
from django.conf import settings
from lino.utils import mti
from lino.utils.ssin import generate_ssin
from lino.utils import Cycler, join_words
from lino.api import rt, dd
from lino_xl.lib.contacts.management.commands.garble_persons import BelgianDistribution

def objects():

    Person = rt.models.contacts.Person
    Client = rt.models.avanti.Client
    ClientStates = rt.actors.avanti.ClientStates

    def person2client(p, **kw):
        c = mti.insert_child(p, Client)
        for k, v in kw.items():
            setattr(c, k, v)
        c.save()
        return Client.objects.get(pk=p.pk)

    dist = BelgianDistribution()
    
    count = 0
    for person in Person.objects.exclude(gender=''):
        if not person.birth_date:  # not those from humanlinks
            birth_date = settings.SITE.demo_date(-170 * count - 16 * 365)
            national_id = generate_ssin(birth_date, person.gender)

            client = person2client(person,
                                   national_id=national_id,
                                   birth_date=birth_date)
            # youngest client is 16; 170 days between each client

            count += 1
            if count % 2:
                client.client_state = ClientStates.coached
            elif count % 5:
                client.client_state = ClientStates.newcomer
            else:
                client.client_state = ClientStates.former

            # Dorothée is three times in our database
            if client.first_name == "Dorothée":
                client.national_id = None
                client.birth_date = ''
            else:
                p = client
                p.last_name = dist.LAST_NAMES.pop()
                if p.gender == dd.Genders.male:
                    p.first_name = dist.MALES.pop()
                    dist.FEMALES.pop()
                else:
                    p.first_name = dist.FEMALES.pop()
                    dist.MALES.pop()
                p.name = join_words(p.last_name, p.first_name)
                dist.before_save(p)

            # client.full_clean()
            # client.save()
            yield client

