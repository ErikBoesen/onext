import requests
from flask import render_template, flash, redirect, url_for, request, abort, make_response
from app import app, db
from app.forms import LinkForm
from app.models import Link
import random


@app.route('/')
def index():
    return render_template('index.html',
                           bots=bots.items)


@app.route('/about')
def about():
    return render_template('about.html')


def random_string():
    return ''.join([random.choice(string.ascii_letters) for i in range(8)])


@app.route('/create_bot', methods=['GET', 'POST'])
@login_required
def create_link():
    form = BotForm()
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
        return redirect(url_for('edit_bot', slug=bot.slug))
    return render_template('edit_bot.html',
                           title='Create new bot',
                           form=form)
