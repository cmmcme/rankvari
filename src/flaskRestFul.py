from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
from dbMongo import Collect

app = Flask(__name__)
api = Api(app)


@app.route('/')
def hello_world():
    return 'Hello World'


class RegistUser(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', type = str)
        parser.add_argument('language', type = str)
        args = parser.parse_args()

        url = args['url']
        language = args['language']

        url
        Collect(url, language)
        return {'url' : url, 'language' : language}


api.add_resource(RegistUser, '/user')


if __name__ == '__main__':
    app.run(debug = True)