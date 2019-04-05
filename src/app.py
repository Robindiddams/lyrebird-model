from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
import boto3
import subprocess

s3 = boto3.resource('s3')

app = Flask(__name__)
CORS(app)
 
@app.route("/")
def runModel():
    task_id = request.args.get('task_id')
    child_id = os.fork()
    if (child_id == 0):
        subprocess.run(["python3", "LyreBird/Create_Music.py", task_id])
        print("done")
        return "OK"
    else:
        data={}
        data["success"]=True
        return jsonify(data)
        # for bucket in s3.buckets.all():
        #     print(bucket.name)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)