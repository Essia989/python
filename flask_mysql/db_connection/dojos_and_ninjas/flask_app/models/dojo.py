from flask_app.config.mysqlconnection import connectToMySQL, DB 

class Dojo:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls,data):
        #query to insert user into database
        #print (data['first_name']) 
        query ="INSERT INTO dojos (name,created_at, updated_at)  VALUES(%(name)s,now(),now());"
        
        return connectToMySQL(DB).query_db(query,data)

    @classmethod 
    def get_dojos(cls):
        #query to retrieve users from database
        query ="SELECT * FROM dojos;"

        results = connectToMySQL(DB).query_db(query)
        dojos = []
        for item in results:
            dojo = cls(item)
            dojos.append(dojo)
        return dojos
    
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        dojo = None
        if result != []:
            dojo = cls(result[0])
        return dojo
