from flask import jsonify, request
from app.models.Student import Student
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# @app.route('/students/')
def get_all_user():
    return jsonify([
        {
        'id': student.id,
        'name': student.firstname,
        'lastname': student.lastname,
        'email': student.email,
        'age': student.age,
        'bio': student.bio
        }
        for student in Student.query.all()])

# @app.route('/students/<id>')
def get_user(id):
    
    print(id)
    student = Student.query.filter_by(id=id).first_or_404()
    
    return jsonify([{
            'id': student.id,
            'firstname': student.firstname,
            'lastname': student.lastname,
            'email': student.email,
            'bio': student.bio
        }])
    
# @app.route('/students/', methods=['POST'])
def create_user():
    data = request.get_json()

    student = Student(
        firstname=data['firstname'],
        lastname = data['lastname'],
        email = data['email'],
        age = data['age'],
        bio = data['bio'],
    )
    
    db.session.add(student)
    db.session.commit()
    
    return {
        'id': student.id,
        'firstname': student.firstname,
        'lastname': student.lastname,
        'email': student.email,
        'age': student.age,
        'bio': student.bio
    }, 201
    
# @app.route('/students/<id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()
    student = Student.query.filter_by(id=id).first_or_404()
    student.lastname = data['lastname']
    db.session.commit()
    return jsonify({
        'firstname': student.firstname,
        'lastname': student.lastname,
        'email': student.email,
        'age': student.age,
        'bio': student.bio
    })
    
# @app.route('/students/<id>', methods=['DELETE'])
def delete_user(id):
    student = Student.query.filter_by(id=id).first_or_404()
    db.session.delete(student)
    db.session.commit()
    return jsonify({
        'message': 'Student deleted'
    })
