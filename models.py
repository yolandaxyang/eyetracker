from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)

author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'eyetracker'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    identity = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    gender = models.CharField(choices=["M", "F"])
    options = models.CharField()
    time = models.PositiveIntegerField()
