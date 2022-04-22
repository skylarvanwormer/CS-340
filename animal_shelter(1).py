from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, user, password):
        # This initializes mongoclient to access the db
        self.client = MongoClient('mongodb://%s:%s@localhost:47383' % (user, password))
        self.database = self.client['AAC']
        
        #This creates the C in CRUD. A new document, takes in a dictionary and returns true if document is created and false if not
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert(data) # data should be dictionary
            #Store the results of the insert to variable
            insert_result = self.database.animals.insert(data) # data should be dictionary
            #If insert was successful, return True, else, return False
            if insert_result is not None:
                status = True
            else:
                status = False
                return status
        else:
            raise Exception("Nothing to save, because data parameter is empty")

                # Method to implement the R in CRUD.
    def read(self, data):
        #Verify that search criteria was provided, else raise an exception
        if data is not None:
            animalsCollection = self.database.animals.find(data)
            #return animalsCollection
            #print animalsCollection cursor
            for animals in animalsCollection:
                print(animals)
        else:
            raise Exception("No search criteria provided")

# Method to implement the U in CRUD
    def update(self, query, record):
        #Verify that the record exists; if so, update accordingly
        if record is not None:
            # update the documents matching the query criteria and print no. of documents updated in json format
            update_result = self.database.animals.update_many(query, record)
            result= "Documents updated: " + json.dumps(update_result.modified_count)
            #print("Documents updated ", json.dumps(update_result.modified_count))
            return result
        else:
            raise Exception("Record not found")

                # Method to implement the D in CRUD
    def delete(self, data):
        #Verify that the record to be deleted has been supplied
        if data is not None:
            # delete the documents matching data criteria and print no. of documents deleted in json format
            delete_result = self.database.animals.delete_many(data)
            result = "Documents deleted: "+ json.dumps(delete_result.deleted_count)
            #print("Documents deleted ", json.dumps(delete_result.deleted_count))
            return result
        else:
            raise Exception("No record provided")
