from flask import request
from flask_restful import Resource
from app.models import User
from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

class UserRegister(Resource):
    def post(self):
        data = request.get_json()
        if User.query.filter_by(username=data['username']).first():
            return {"message": "User already exists"}, 400

        new_user = User(
            username=data['username'],
            password=generate_password_hash(data['password'])
        )
        db.session.add(new_user)
        db.session.commit()
        return {"message": "User created successfully"}, 201

class UserLogin(Resource):
    def post(self):
        data = request.get_json()
        user = User.query.filter_by(username=data['username']).first()
        if user and check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity=user.id)
            return {"access_token": access_token}, 200
        return {"message": "Invalid credentials"}, 401
