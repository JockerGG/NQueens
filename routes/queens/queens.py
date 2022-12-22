from flask_restful import Api, Resource
from flask import jsonify
from repository import DbRepository
import json
import logging

log = logging.getLogger("tester.sub")


class Queens(Resource):
    db_repo = DbRepository()

    def get(self, n):
        solutions = self.solve_puzzle(n)
        return jsonify(
            numberOfSolutions=len(solutions),
            solutions=solutions
        )

    @staticmethod
    def is_queen_safe(n, board, row, col):
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

    def place_queens(self, n, board, results, col):
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
            if self.is_queen_safe(n, board, i, col):
                board[i][col] = 1
                res = self.place_queens(n, board, results, col + 1) or res
                board[i][col] = 0

        return res

    def solve_puzzle(self, n):
        results = []
        cached_solution = self.db_repo.get_resolution(n=n)

        if cached_solution:
            log.warning("Cached solution")
            results = json.loads(cached_solution.solutions)
            return results

        board = [[0 for j in range(n)]
                 for i in range(n)]
        self.place_queens(n, board, results, 0)
        results.sort()
        self.db_repo.save_solution(results=results, n=n)

        return results
