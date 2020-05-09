from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, URL
from app.models import User


class BotForm(FlaskForm):
    chrome_url  = StringField('Chrome Web Store URL')
    firefox_url = StringField('Mozilla Add-ons URL')
    safari_url  = StringField('Safari Extension URL')
    opera_url   = StringField('Opera Extension URL')
    edge_url    = StringField('MS Edge Extension URL')

    fallback_url = StringField('Fallback URL', validators=[DataRequired()])

    submit = SubmitField('Submit')
