from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap
from sqlalchemy import func

from playwithme.config import WEB_SECRET, CHAN, TITLE
from playwithme.model import StorageModel, session

web = Flask(__name__)
web.config['SECRET_KEY'] = WEB_SECRET
Bootstrap(web)

admin = Admin(web)
admin.add_views(ModelView(StorageModel, session()))


@web.route("/")
def index():
    title = "{}: {}".format(TITLE, CHAN)
    print(web.template_folder)
    ses = session()

    ids = [x[0] for x in ses.query(func.max(StorageModel.id)).group_by(StorageModel.twitch, StorageModel.game).all()]
    ids.sort()
    data = ses.query(StorageModel).filter(StorageModel.id.in_(ids)).all()

    return render_template('table.html', data=data, title=title)
