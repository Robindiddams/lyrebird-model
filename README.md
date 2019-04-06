# lyrebird model

the container for running the lyrebird music generation model

## Building
* clone the model into `src/LyreBird`
* building might look something like this:
```
docker build --build-arg key_id=$AWS_ACCESS_KEY_ID --build-arg access_key=$AWS_SECRET_ACCESS_KEY -t lyrebird-model:1.0.1 .
```
**NOTE:** its **not** a good idea to put the credentials in at build time like this, and you should **never** pass root/admin credentials into your microservices. See [here](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) for how to properly auth in a task.

push it to your ecs cluster and then hit it like this:
```
curl http://YOURTASKPUBLICIP:8080/?task_id=whatever
```
 and itll start a process and dump the output in the bucket set in `app.py`