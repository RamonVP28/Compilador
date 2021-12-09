import flask
from flask.json import jsonify
from flask_cors import CORS, cross_origin
import main

Operaciones = {}

app = flask.Flask(__name__)
CORS(app, resources={r"/Code/*": {"origins": "http://localhost:3000"}})

#@cross_origin
@app.route('/Code', methods=['POST'])
def getDatos(): 
    input = flask.request.json['code']
    if input == "":
        Operaciones["Sintactico"] = "No se ha ingresado ningun codigo"
        Operaciones["Lexico"] = ""
        Operaciones["Semantico"] = ""
    else:
        output = main.run(input)
        Operaciones["Sintactico"] = output[output.index("<Inicio Sintactico>")+len("<Inicio Sintactico>"):output.index("<Fin Sintactico>")]
        Operaciones["Lexico"] = output[output.index("<Inicio Lexico>")+len("<Inicio Lexico>"):output.index("<Fin Lexico>")]
        Operaciones["Semantico"] = output[output.index("<Inicio Semantico>")+len("<Inicio Semantico>"):output.index("<Fin Semantico>")]
    return jsonify(Operaciones)

if __name__ == '__main__':
    app.run(debug=True)
