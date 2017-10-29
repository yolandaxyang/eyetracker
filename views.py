from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class Page1(Page):
    form_model = models.Player
    form_fields = ['identity', 'age', 'gender']


class Page2(Page):
    form_model = models.Player
    form_fields = ['options']


class Page3(Page):
    pass


page_sequence = [
    Page1,
    Page2,
    Page3
]
