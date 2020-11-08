from DAOs.db import db
import csv
class RatingDAO(db):
    def __init__(self):
        super().__init__()
        self.table = "Review"

    def selectAllRatings(self,name):
        return self.query("*", "WHERE Name = %s",[name])

    def insertRating(self,params):
        query = "INSERT INTO " + self.table + "(Name, Rating) VALUES (%s,%s)"
        self.hardinsert(query,params)


