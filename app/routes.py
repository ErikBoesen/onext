import requests
from flask import render_template, flash, redirect, url_for, request, abort, make_response
from app import app, db
from app.forms import LinkForm
from app.models import Link
import random
import string


def random_string():
    return ''.join([random.choice(string.ascii_letters) for i in range(8)])


@app.route('/', methods=['GET', 'POST'])
def index():
    form = LinkForm()
    if form.validate_on_submit():
        link = Link(id=form.id.data,
                    chrome_url=form.chrome_url.data,
                    firefox_url=form.firefox_url.data,
                    safari_url=form.safari_url.data,
                    opera_url=form.opera_url.data,
                    edge_url=form.edge_url.data,
                    fallback_url=form.fallback_url.data)
        db.session.add(link)
        db.session.commit()
        flash('Created link ' + link.id + '!')
        return render_template('success.html', id=link.id)
    return render_template('index.html', form=form, id=random_string())


@app.route('/about')
def about():
    return render_template('about.html')
