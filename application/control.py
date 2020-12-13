from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import InputRequired
import requests
from urllib.parse import quote
from application.config import Config


class Search(FlaskForm):
    quantity = IntegerField('Quantity', validators=[InputRequired()], render_kw={"placeholder": "e.g. 1"})
    measure = StringField('Measure', validators=[InputRequired()], render_kw={"placeholder": "e.g. cup"})
    food = StringField('Food', validators=[InputRequired()], render_kw={"placeholder": "e.g. rice"})
    submit = SubmitField()


def nutrition_api_call(form):
    query = quote(f'{form.quantity.data} {form.measure.data} {form.food.data}')
    url = f'https://api.edamam.com/api/nutrition-data?app_id={Config.APP_ID}&app_key={Config.APP_KEY}&ingr={query}'
    res = requests.get(url=url)
    return res.json()
