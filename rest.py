from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#Speichert den Score zu bestimmten Namen
name_score = []

class SimpleClass(Resource):
    def get(self):
        return name_score


class SimpleNameScore(Resource):
    def get(self, name):
        if name in name_score:
            return {name: name_score[name]}
        return {"Message" : "Nicht vorhanden"}

    def put(self, name):
        for arr in name_score:
            if arr[0] == name:
                if arr[1] == request.form['symbol']:
                    name_score.remove(arr)
        name_score.append([request.form['name'], request.form['symbol'], request.form['symbolanzahl']])

#Hier passiert das Mapping auf die Klasse
api.add_resource(SimpleClass, '/')
api.add_resource(SimpleNameScore, '/upload/<string:name>')

if __name__ == '__main__':
    app.run(debug=True)


#Aufrufe für SimpleNameScore
# curl http://localhost:5000/score/albert -d "score=100" -X PUT