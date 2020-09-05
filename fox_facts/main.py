""" Main application. """

from flask import Flask
from flask_restx import Resource, Api

HOSTNAME = "127.0.0.1"

app = Flask(__name__)
api = Api(app)


@api.route("/hello")
class FoxFacts(Resource):
    """ Main class. """

    _hello = {"hello": "fox"}

    def get(self):
        """ GET method. """
        return self._hello


if __name__ == "__main__":
    app.run(host=HOSTNAME, port=8080, debug=True)
