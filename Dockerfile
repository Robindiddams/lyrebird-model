FROM tensorflow/tensorflow:latest-py3

RUN mkdir -p /home/lyrebird
COPY src/LyreBird/requirements.txt /home/lyrebird
RUN pip install -r /home/lyrebird/requirements.txt
RUN pip install flask flask_cors boto3
COPY src /home/lyrebird/app
WORKDIR /home/lyrebird/app

EXPOSE 8080
CMD python3 /home/lyrebird/app/app.py