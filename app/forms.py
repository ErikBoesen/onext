from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL
from app.models import Link


class LinkForm(FlaskForm):
    id = StringField('Shortlink', validators=[DataRequired(), Length(min=3, max=30)])

    chrome_url  = StringField('Chrome Extension')
    firefox_url = StringField('Mozilla Add-on')
    safari_url  = StringField('Safari Extension')
    opera_url   = StringField('Opera Extension')
    edge_url    = StringField('Edge Extension')

    fallback_url = StringField('Fallback URL', validators=[DataRequired()])

    submit = SubmitField('Submit')
