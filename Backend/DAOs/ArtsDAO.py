from DAOs.db import db
import csv
class ArtsDAO(db):
    def __init__(self):
        super().__init__()
        self.table = "Arts"

    def selectAll(self):
        return self.query("Name", "",[])






