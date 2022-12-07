from flask import Flask
from flask import jsonify
from flask_restful import Resource
import logging

log = logging.getLogger("tester.sub")

class Queens(Resource):
    results = []
    def isQueenSafe(self, n, board, row, col):
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

    def placeQueens(self, n, board, results, col):
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
            if self.isQueenSafe(n, board, i, col):
                board[i][col] = 1
                res = self.placeQueens(n, board, results, col + 1) or res
                board[i][col] = 0

        return res
        
    def solvePuzzle(self, n):
        results = []
        board = [[0 for j in range(n)]
			for i in range(n)]
        self.placeQueens(n, board, results, 0)
        results.sort()
        return results
    
    def get(self, n): 
        solutions = self.solvePuzzle(n)
        return jsonify(
            numberOfSolutions = len(solutions),
            solutions = solutions
        )
