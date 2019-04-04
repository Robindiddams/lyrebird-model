FROM tensorflow/tensorflow

RUN mkdir -p /home/lyrebird
COPY src /home/lyrebird/app
RUN pip install -r /home/lyrebird/app/requirements.txt
RUN pip install flask flask_cors
WORKDIR /home/lyrebird/app
 
EXPOSE 8080
CMD python /home/lyrebird/app/app.py