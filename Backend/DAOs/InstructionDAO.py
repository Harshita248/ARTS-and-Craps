from DAOs.db import db
import csv

class InstructionDAO(db):
    def __init__(self):
        super().__init__()
        self.table = "Instruction"

    def selectAllInstructions(self,name):
        return self.query("*", "WHERE Name = %s ORDER BY StepNumber ASC",[name])






