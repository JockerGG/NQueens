from db.models import solutions
from db.database import SessionLocal, engine
import logging
import json

log = logging.getLogger("tester.sub")


class DbRepository:
    db = SessionLocal()
    solutions.Base.metadata.create_all(bind=engine)

    def __init__(self):
        print("Address of self = ", id(self))

    def get_resolution(self, n):
        self.db.query(solutions.Solutions).filter_by(number_of_queens=n).first()

    def save_solution(self, results, n):
        new_solution = solutions.Solutions(
            solutions=json.dumps(results),
            number_of_queens=n
        )
        log.warning("Saving solution")
        self.db.add(new_solution)
        self.db.commit()
        self.db.close()
