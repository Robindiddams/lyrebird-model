FROM tensorflow/tensorflow:latest-py3

RUN mkdir -p /home/lyrebird
COPY src/LyreBird/requirements.txt /home/lyrebird
RUN pip install -r /home/lyrebird/requirements.txt
RUN pip install flask flask_cors boto3 waitress
COPY src /home/lyrebird/app
WORKDIR /home/lyrebird/app

ARG access_key=
ARG key_id=
ENV AWS_ACCESS_KEY_ID=$key_id
ENV AWS_SECRET_ACCESS_KEY=$access_key
EXPOSE 8080
CMD python3 /home/lyrebird/app/app.py