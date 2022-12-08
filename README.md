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

# Docker References: 
- https://docs.docker.com/desktop/install/mac-install/
- https://code.visualstudio.com/docs/containers/quickstart-python https://stackoverflow.com/questions/30323224/deploying-a-minimal-flask-app-in-docker-server-connection-issues/43015007#43015007 https://www.freecodecamp.org/news/how-to-dockerize-a-flask-app/
- https://betterprogramming.pub/how-to-dockerize-your-flask-api-cc95843ab625
- https://www.youtube.com/watch?v=VjIYcJVZCP0

# Flask References: 
- https://www.folkstalk.com/2022/09/how-to-return-json-response-in-flask-with-code-examples.html
- https://www.geeksforgeeks.org/how-to-run-two-async-functions-forever-python/
- https://www.ffnext.io/blog/python-backend-with-flask-for-beginners
- https://medium.com/globant/how-to-add-a-basic-unit-test-to-a-python-flask-app-using-pytest-79e61da76fc2
  
# Queens puzzle solution: 
- https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/?ref=lbp

# SQLAlchemy References:
- https://towardsdatascience.com/use-flask-and-sqlalchemy-not-flask-sqlalchemy-5a64fafe22a4
- https://medium.com/swlh/flask-sqlalchemy-basics-60d4f7f122
- https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_introduction.html
