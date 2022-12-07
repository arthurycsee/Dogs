from flask_app.config.mysqlconnect import connectToMySQL
from flask_app import DATABASE

class Dog:
    def __init__(self,data) -> None:
        self.id = data['id']
        self.name = data['name']
        self.age = data['age']
        self.breed = data['breed']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = """
            SELECT * FROM dogs;
        
        """
        results = connectToMySQL("dog").query_db(query)
        print(results)
        all_dogs = []
        for one_row in results:
            this_dog_instance = cls(one_row) #this line creates the instance
            all_dogs.append(this_dog_instance)
        return all_dogs

    @classmethod
    def get_one(cls,data):
        query = """
            SELECT * FROM dog WHERE dogs.id = %(id)s;
        """
        results = connectToMySQL("dog").query_db(query,data)
        if results:
            return cls(results[0])
        return False

    @classmethod
    def create(cls,data):
        query = """
            INSERT INTO dogs (name,age,breed)
            VALUES (%(name)s,%(age)s,%(breed)s)
        """
        return connectToMySQL("dog").query_db(query,data)

    @classmethod
    def update(cls,data):
        query = """
            UPDATE dogs SET name = %(name)s,age = %(age)s, breed = %(breed)s
            WHERE dogs.id = %(id)s;
        """
        return connectToMySQL("dog").query_db(query,data)

    @classmethod
    def delete(cls,data):
        query = """
            DELETE FROM dogs where dogs.id = %(id)s;
        """
        return connectToMySQL("dog").query_db(query,data)