from app import app, db


class Link(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.String, primary_key=True)

    chrome_url = db.Column(db.String)
    firefox_url = db.Column(db.String)
    safari_url = db.Column(db.String)
    opera_url = db.Column(db.String)
    edge_url = db.Column(db.String)

    fallback_url = db.Column(db.String)
