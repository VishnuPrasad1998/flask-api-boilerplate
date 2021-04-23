# Copyright 2014 SolidBuilds.com. All rights reserved
#
# Authors: Ling Thio <ling.thio@gmail.com>


from app.db import db
from flask import jsonify
from flask_restful import Resource, reqparse
from app.models.user_models import UserModel
from app.models.student import StudentModel
from app.resources.serializers import student_schema

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()


        user = UserModel(data['username'], data['password'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201



class StudentRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )
    parser.add_argument('course',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = StudentRegister.parser.parse_args()


        student = StudentModel(data['name'], data['course'])
        student.save_to_db()

        return {"message": "Student created successfully."}, 201


    def get(self):
        stu = StudentModel.query.all()
        return student_schema.jsonify(stu)