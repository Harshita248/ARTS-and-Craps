from DAOs.db import db
import csv
class MaterialDAO(db):
    def __init__(self):
        super().__init__()
        self.table = "Material"

    def selectAllMaterial(self,name):
        return self.query("*", "WHERE Name = %s",[name])






