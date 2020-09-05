from flask import Flask
from flask_restx import Resource, Api

HOSTNAME = '0.0.0.0'

app = Flask(__name__)
api = Api(app)

@api.route('/hello')
class FoxFacts(Resource):

    def get(self):
        return {'hello': 'world'}

if __name__ == "__main__":
    app.run(host=HOSTNAME, debug=True)
