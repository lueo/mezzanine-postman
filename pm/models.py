
from django.db import models
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable

class Message(Displayable):
    """
    A message.
    """

    class Meta:
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

