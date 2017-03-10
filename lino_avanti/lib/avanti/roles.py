# Copyright 2017 Luc Saffre
# License: BSD (see file COPYING for details)
"""User roles for this plugin."""

from lino.core.roles import UserRole

   
class ClientsUser(UserRole):
    """A user who has access to clients functionality.

    """


class ClientsStaff(ClientsUser):
    """A user who can configure clients functionality.

    """

