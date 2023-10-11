from flask_app.config.mysqlconnection import connectToMySQL, DB 
from flask_app.models.dojo import Dojo


class Ninja:
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo = None

    @classmethod
    def create(cls,data):
        #query to insert user into database
        #print (data['first_name']) 
        query ="INSERT INTO ninjas (first_name,last_name,age,created_at, updated_at,dojo_id)  VALUES(%(first_name)s,%(last_name)s,%(age)s,now(),now(),%(dojo_id)s);"
        return connectToMySQL(DB).query_db(query,data)
    
    @classmethod
    def get_dojo_by_id(cls, data):
        #Select all Ninjas that are enrolled in the same Dojo 
        query = "SELECT * FROM ninjas JOIN dojos ON ninjas.dojo_id = dojos.id WHERE ninjas.dojo_id = %(id)s;"
        result = connectToMySQL(DB).query_db(query, data)
        #ninjas is the list of ninjas
        ninjas = []
        if result:
            #retreiving the dojo data
            dojo_data = {
                    'id': result[0]['dojos.id'],
                    'name': result[0]['first_name'],
                    'created_at': result[0]['dojos.created_at'],
                    'updated_at': result[0]['dojos.updated_at']
                }
            #each item is a ninja enrolled in the Dajo
            for item in result :
                ninja = cls(item)
                ninja.dojo = Dojo(dojo_data)
                ninjas.append(ninja)
        return ninjas
