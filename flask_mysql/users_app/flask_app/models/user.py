from flask_app.config.mysqlconnection import connectToMySQL, DB 

class User:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        #query to insert user into database
        #print (data['first_name']) 
        query ="INSERT INTO users (first_name,last_name,email,created_at, updated_at)  VALUES(%(first_name)s,%(last_name)s,%(email)s,now(),now())"
        
        return connectToMySQL(DB).query_db(query,data)

    @classmethod 
    def get_users(cls):
        #query to retrieve users from database
        query ="SELECT * FROM users;"

        results = connectToMySQL(DB).query_db(query)
        users = []
        for item in results:
            user = cls(item)
            users.append(user)
        return users
    
    """@classmethod 
    def get_user(cls,data):
        # query to select a user from database by id
        
        query ="SELECT * FROM users WHERE id = %(data)s;"
        print (query)
        result = connectToMySQL(DB).query_db(query,data)
        print (result)
        user = None
        if result != []:
            user = cls(result[0])
        return result"""
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        user = None
        if result != []:
            user = cls(result[0])
        return user
    
    @classmethod
    def update(cls, data):
        print (data)
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)
    
    @classmethod
    def delete(cls, data):
        print (data)
        query = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query , data)