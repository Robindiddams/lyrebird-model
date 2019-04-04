from flask import Flask
from flask import jsonify
from flask_cors import CORS
# import commands
# import os
import json
import model.Main_Production.Create_Music as model
 
app = Flask(__name__)
CORS(app)
 
 
@app.route("/")
def runModel():
 
    model.generate()
    data={}
    data["text"]=text
    return jsonify(data)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)