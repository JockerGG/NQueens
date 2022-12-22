from flask import Flask
from flask_restful import Api
from routes.queens.queens import Queens
import sys


app = Flask(__name__)
api = Api(app)

api.add_resource(Queens, "/queens/<int:n>")

if __name__ == '__main__':
    app.run(debug=True)