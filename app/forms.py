from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL
from app.models import Link


class LinkForm(FlaskForm):
    id = StringField('Shortlink', validators=[DataRequired(), Length(min=3, max=30)])

    chrome_url  = StringField('Chrome Web Store URL')
    firefox_url = StringField('Mozilla Add-ons URL')
    safari_url  = StringField('Safari Extension URL')
    opera_url   = StringField('Opera Extension URL')
    edge_url    = StringField('MS Edge Extension URL')

    fallback_url = StringField('Fallback URL', validators=[DataRequired()])

    submit = SubmitField('Submit')
