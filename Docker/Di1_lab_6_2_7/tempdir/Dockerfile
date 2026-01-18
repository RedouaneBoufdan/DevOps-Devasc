FROM python:latest
RUN pip install flask
WORKDIR /home/microweb_app
COPY ./static /home/microweb_app/static
COPY ./templates /home/microweb_app/templates
COPY flask_app.py /home/microweb_app/flask_app.py
EXPOSE 5050
CMD ["python3", "/home/microweb_app/flask_app.py"]
