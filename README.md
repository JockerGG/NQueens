# Eight queens challenge (For N queens).
The solution for the challeng of the N queens. 

# Requirements.

- [X] Determine all possible solutions for a given N where N ≥ 8 (within 10 mins on a laptop). Bonus points for a higher N where N is the size of the board / number of queens.
- [X] Iterate over N and store the solutions in postgres using SQLAlchemy (Not postgress, used sqlite)
- [X] Write basic tests that at least verify the number of solutions for a given N match what's online. I recommend using pytest.
- [ ] Docker-ize the solution, so that I can run the code and tests without any assumption of my local setup (including running a postgres instance in docker-compose)
- [X] Setup Travis CI (or similar) for your public GitHub repo to run the tests automatically.

# Github actions as a CI.
You can see the actions implemented here: https://github.com/JockerGG/NQueens/actions.
