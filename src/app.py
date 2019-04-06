from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve
import json
import os
import base64
import subprocess
import boto3
s3 = boto3.client('s3')
BUCKET = "lyrebird-sounds"
print(os.environ["AWS_ACCESS_KEY_ID"])
print(os.environ["AWS_SECRET_ACCESS_KEY"])
app = Flask(__name__)
CORS(app)
 
@app.route("/")
def runModel():
    task_id = request.args.get('task_id')
    if (task_id is None):
        data={}
        data["success"]=False
        data["message"]="missing task id"
        return jsonify(data)
    filepath = task_id + ".mid"
    cpid = os.fork()
    if cpid is 0:
        subprocess.run(["python3", "LyreBird/Create_Music.py", task_id])
        s3.upload_file(filepath, BUCKET, "task_"+task_id)
        os.remove(filepath)
        return "OK"
    else:
        data={}
        data["success"]=True
        return jsonify(data)
 
if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080)