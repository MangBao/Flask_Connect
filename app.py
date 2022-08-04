# from flask_sqlalchemy import SQLAlchemy
# import os
# from flask import Flask, Blueprint
# from app.controller.StudentController import get_all_user, get_user, create_user, update_user, delete_user

# basedir = os.path.abspath(os.path.dirname(__file__))

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] =\
#         'sqlite:///' + os.path.join(basedir, 'database.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# student_blueprint = Blueprint('student', __name__)

# student_blueprint.route('/students/').get(get_all_user)
# student_blueprint.route('/students/<int:id>').get(get_user)
# student_blueprint.route('/students/').post(create_user)
# student_blueprint.route('/students/<int:id>').put(update_user)
# student_blueprint.route('/students/<int:id>').delete(delete_user)

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')
from app.models.Student import db
from routes import student_blueprint

db.init_app(app)
# migrate = Migrate(app, db)
app.register_blueprint(student_blueprint, url_prefix='/student')
@app.route('/')
def index():
    return render_template('index.html')
if __name__ == '__main__':
    app.debug = True
    app.run()


