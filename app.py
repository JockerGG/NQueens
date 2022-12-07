from flask import Flask
from flask_restful import Api, Resource
from queens.Queens import Queens
import logging
import sys

app = Flask(__name__)
api = Api(app)

@app.route("/")
def home():
	return "Hello, world!"

api.add_resource(Queens, "/queens/<int:n>", methods=["GET"])

if __name__ == '__main__':
    app.run(debug=True)