from wtforms import Form, FloatField, validators, StringField, ValidationError, IntegerField
from wtforms.validators import NumberRange
from math import pi


class InputForm(Form):
    A = FloatField(
        label='Population', default=396488,
        validators=[validators.InputRequired()])
    b = FloatField(
        label='Recovered', default=0,
        validators=[validators.InputRequired()])
    w = FloatField(
        label='Days', default=150,
        validators=[validators.InputRequired()])
    T = FloatField(
        label='Days to Recovery', default=5,
        validators=[validators.InputRequired()])
    R_0 = FloatField(
        label='Rate of Reproduction', default=2.9,
        validators=[validators.InputRequired()])
    D = FloatField(
        label='Deaths', default=22,
        validators=[validators.InputRequired()])
    C = FloatField(
        label='Cases', default=380,
        validators=[validators.InputRequired()])


class StateInputForm(Form):
    S = StringField(
        label='State', default='Wisconsin',
        validators=[validators.InputRequired()])


class CountyInputForm(Form):
    S = StringField(
        label='State', default='Illinois',
        validators=[validators.InputRequired()])
    C = StringField(
        label='County', default='Cook',
        validators=[validators.InputRequired()])


class ContactInputForm(Form):
    A = FloatField(
        label='Population', default=396488,
        validators=[validators.InputRequired()])
    b = FloatField(
        label='Recovered', default=0,
        validators=[validators.InputRequired()])
    w = FloatField(
        label='Days', default=150,
        validators=[validators.InputRequired()])
    T = FloatField(
        label='Days to Recovery', default=5,
        validators=[validators.InputRequired()])
    R_0 = FloatField(
        label='Rate of Reproduction', default=2.9,
        validators=[validators.InputRequired(), validators.NumberRange(min=1, max=10, message='Must be between 1 and 10')])
    D = FloatField(
        label='Deaths', default=22,
        validators=[validators.InputRequired()])
    C = FloatField(
        label='Cases', default=380,
        validators=[validators.InputRequired()])
    CO = FloatField(
        label='Percentage of Normal Contact', default=.25,
        validators=[validators.InputRequired()])
    PP = FloatField(
        label='Percentage of Isolators', default=.5,
        validators=[validators.InputRequired()])


class ContactInputForm2(Form):
    A = FloatField(
        label='Population', default=396488,
        validators=[validators.InputRequired()])
    b = FloatField(
        label='Recovered', default=0,
        validators=[validators.InputRequired()])
    w = FloatField(
        label='Days', default=150,
        validators=[validators.InputRequired()])
    T = FloatField(
        label='Days to Recovery', default=5,
        validators=[validators.InputRequired()])
    R_0 = FloatField(
        label='Rate of Reproduction', default=2.9,
        validators=[validators.InputRequired(), validators.NumberRange(min=1, max=10, message='Must be between 1 and 10')])
    D = FloatField(
        label='Deaths',
        validators=[validators.InputRequired()])
    CA = FloatField(
        label='Cases',
        validators=[validators.InputRequired()])
    CO = FloatField(
        label='Percentage of Normal Contact', default=.25,
        validators=[validators.InputRequired()])
    PP = FloatField(
        label='Percentage of Isolators', default=.5,
        validators=[validators.InputRequired()])


class DataGenForm(Form):
    A = IntegerField(
        label='Total Records', default=10,
        validators=[validators.InputRequired(), validators.NumberRange(min=5, max=1000, message='Must be between 5 and 1000')])
    MA = IntegerField(
        label='Maximum Age', default=75,
        validators=[validators.InputRequired(), validators.NumberRange(min=20, max=100, message='Must be between 5 and 1000')])
    P = FloatField(
        label='Percentage of Positive Records', default=.5,
        validators=[validators.InputRequired()])
    PF = FloatField(
        label='Percentage of Positive Records that are Female', default=.5,
        validators=[validators.InputRequired()])
    NF = FloatField(
        label='Percentage of Negative Records that are Female', default=.5,
        validators=[validators.InputRequired()])

