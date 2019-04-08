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
app = Flask(__name__)
CORS(app)
 
@app.route("/")
def runModel():
    task_id = request.args.get('task_id')
    seed = request.args.get('seed')
    if ( (task_id is None) or (seed is None) ):
        data={}
        data["success"]=False
        data["message"]="missing task id or seed"
        return jsonify(data)
    filepath = task_id + ".mid"
    cpid = os.fork()
    if cpid is 0:
        subprocess.run(["python3", "LyreBird/Create_Music.py", task_id, seed])
        s3.upload_file(filepath, BUCKET, "task_"+task_id)
        os.remove(filepath)
        return "OK"
    else:
        data={}
        data["success"]=True
        return jsonify(data)
 
if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=8080)