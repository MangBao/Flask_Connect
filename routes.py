from flask import Flask, Blueprint
from app.controller.StudentController import get_all_user, get_user, create_user, update_user, delete_user


student_blueprint = Blueprint('student', __name__)

student_blueprint.route('/students/').get(get_all_user)
student_blueprint.route('/students/<int:id>').get(get_user)
student_blueprint.route('/students/').post(create_user)
student_blueprint.route('/students/<int:id>').put(update_user)
student_blueprint.route('/students/<int:id>').delete(delete_user)