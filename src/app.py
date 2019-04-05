from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import os
import boto3
import LyreBird.Create_Music as model

s3 = boto3.resource('s3')

app = Flask(__name__)
CORS(app)
 
@app.route("/")
def runModel():
    task_id = request.args.get('task_id')
    newpid = os.fork()
    if newpid == 0:
        data={}
        data["success"]=True
        return jsonify(data)
    else:
        model.generate()
        print("done")
        for bucket in s3.buckets.all():
            print(bucket.name)
        return "OK" # this is a throwaway lol!
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)