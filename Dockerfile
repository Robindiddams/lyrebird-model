FROM tensorflow/tensorflow:latest-gpu-py3

RUN mkdir -p /home/lyrebird
COPY src /home/lyrebird/app
RUN pip install -r /home/lyrebird/app/LyreBird/requirements.txt
RUN pip install flask flask_cors boto
WORKDIR /home/lyrebird/app
 
EXPOSE 8080
CMD python3 /home/lyrebird/app/app.py