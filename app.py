from flask import Flask, jsonify
from flask_restful import Api, Resource
from database.models import solutions
from database.database import SessionLocal, engine
from sqlalchemy.orm import scoped_session
import json
import logging
import sys

db = SessionLocal()
solutions.Base.metadata.create_all(bind = engine)

log = logging.getLogger("tester.sub")
app = Flask(__name__)
api = Api(app)


@app.route("/queens/<int:n>")
def queens(n):
    solutions = solvePuzzle(n)
    return jsonify(
        numberOfSolutions = len(solutions),
        solutions = solutions
    )

def isQueenSafe(n, board, row, col):
        for i in range(col):
            if board[row][i]:
                return False
        
        i = row 
        j = col 
        while i >= 0 and j >= 0:
            if board[i][j]:
                return False
            i -= 1
            j -= 1
        
        i = row
        j = col
        while j >= 0 and i < n:
            if board[i][j]:
                return False
            i += 1
            j -= 1
        
        return True

def placeQueens(n, board, results, col):
    if col == n: 
        v = []
        lines = ""
        for i in board:
            for j in range(len(i)):
                if i[j] == 1:
                    lines += " Q "
                    v.append(j + 1)
                else:
                    lines += " . "
            lines += "\n"
        results.append(v)
        log.warning(f"Board:\n{lines}")
        return True

    res = False

    for i in range(n):
        if isQueenSafe(n, board, i, col):
            board[i][col] = 1
            res = placeQueens(n, board, results, col + 1) or res
            board[i][col] = 0

    return res
        
def solvePuzzle(n):
    results = []
    cached_solution = db.query(solutions.Solutions).filter_by(number_of_queens = n).first()
    
    if cached_solution:
        log.warning("Cached solution")
        results = json.loads(cached_solution.solutions)
        return results

    board = [[0 for j in range(n)]
        for i in range(n)]
    placeQueens(n, board, results, 0)
    results.sort()
    newSolution = solutions.Solutions(
        solutions = json.dumps(results),
        number_of_queens = n
    )
    log.warning("Saving solution")
    db.add(newSolution)
    db.commit()
    db.close()

    return results

if __name__ == '__main__':
    app.run(debug=True)