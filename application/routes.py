from flask import Blueprint
from flask import render_template
from application.control import Search, nutrition_api_call

app_bp = Blueprint('app_bp', __name__)


@app_bp.route('/', methods=['GET', 'POST'])
def home():
    form = Search()
    if form.validate_on_submit():
        res = nutrition_api_call(form)
        return render_template('home.html', form=form, result=res)
    return render_template('home.html', form=form)
