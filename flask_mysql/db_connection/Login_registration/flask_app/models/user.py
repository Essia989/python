from flask_app.config.mysqlconnection import MySQLConnection, DB
from flask import flash
from flask_app import app
import re
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)
class User:
    def __init__(self, data):
        self.id          = data ['id']
        self.firstname   = data ['firstname']
        self.lastname    = data ['lastname']
        self.email       = data ['email']
        self.password    = data ['password']
        self.created_at  = data ['created_at']
        self.updated_at  = data ['updated_at']

    @classmethod
    def create(cls , data):
        #Hashing the password
        encrypted_password = bcrypt.generate_password_hash(data['password'])
        #converting the data to a dictionary 
        data = dict(data)
        print(f'before hasshing tha password', data)
        #saving the hashed password in data 
        data['password'] = encrypted_password
        print(f'after hasshing tha password', data)
        #inserting the new user into DB 
        query = "INSERT INTO users (firstname ,lastname, email, password, created_at, updated_at) VALUES (%(firstname)s,%(lastname)s,%(email)s,%(password)s,now(),now());"
        print(f'the query : ', query)
        result = MySQLConnection(DB).query_db(query, data)

        return result

    @staticmethod
    def validate_register(data):
        is_valid = True
        user_in_db = User.get_by_email(data)
        email_validate_pattern = r"^\S+@\S+\.\S+$"
        if len(data['firstname'])  < 2:
            flash("Register: First Name needs to be longer then 2 characters.")
            is_valid = False
        if len(data['lastname'])  < 2:
            flash("Register: Last Name needs to be longer then 2 characters.")
            is_valid = False
        if not re.match(email_validate_pattern,data['email']):
            flash("Register: Invalid email format.")
            is_valid = False
        if user_in_db:
            flash("Register: User email already exists.")
            is_valid = False
        if len(data['password']) < 8:
            flash("Register: Password needs to be at least 8 characters or more.")
            is_valid = False
        if data['password'] != data['confirm_password']:
            flash("Register: Passwords don't match!")
            is_valid = False
        return is_valid
    

    @staticmethod
    def validate_login(data):
        is_valid = True

        user_in_db = User.get_by_email(data)
        
        print(f'DATA:',data)
        email_validate_pattern = r"^\S+@\S+\.\S+$"
        """re.match(email_validate_pattern, "hello@uibakery.io")"""
        print(f'after hasshing tha password', data['password'])
        if not re.match(email_validate_pattern,data['email']):
            flash("Login: Invalid email format.")
            is_valid = False
        if user_in_db == False:
            flash("Login: User with this email doesn't exist.")
            is_valid = False
        elif len(data['password']) < 8:
            flash("Login: Password needs to be at least 8 characters or more.")
            is_valid = False
        elif not bcrypt.check_password_hash(user_in_db.password, data['password']):
            flash("Login: Incorrect Password")
            is_valid = False
        return is_valid
        
    @classmethod
    def get_by_email(cls, data):
        print(f'DATA to exract user from DB : ',data['email'])
        query = "SELECT * FROM users WHERE email = %(email)s;"

        result = MySQLConnection(DB).query_db(query , data)
        print (result)
        if result:
            # user_data = result[0]
            # user = cls(user_data)
            return cls(result[0])
        return False