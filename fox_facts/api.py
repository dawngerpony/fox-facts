""" Main application. """

from flask import Flask
from flask_restx import Resource, Api

HOSTNAME = "0.0.0.0"

app = Flask(__name__)
api = Api(app)


@api.route("/hello")
class FoxFacts(Resource):
    """ Main class. """

    _hello = {"hello": "world"}

    def get(self):
        """ GET method. """
        return self._hello


if __name__ == "__main__":
    app.run(host=HOSTNAME, debug=True)
