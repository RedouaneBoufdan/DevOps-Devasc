#!/bin/bash
set -e

# 1) Create temp folders
rm -rf tempdir
mkdir -p tempdir/templates tempdir/static

# 2) Copy app files
cp flask_app.py tempdir/
cp -r templates/* tempdir/templates/
cp -r static/* tempdir/static/

# 3) Create Dockerfile (like the lab does with echo)
cat > tempdir/Dockerfile <<'EOF'
FROM python:latest
RUN pip install flask
WORKDIR /home/microweb_app
COPY ./static /home/microweb_app/static
COPY ./templates /home/microweb_app/templates
COPY flask_app.py /home/microweb_app/flask_app.py
EXPOSE 5050
CMD ["python3", "/home/microweb_app/flask_app.py"]
EOF

# 4) Build image
cd tempdir
docker build -t di1-micro-web .

# 5) Run container
docker rm -f di1-running 2>/dev/null || true
docker run -t -d -p 8080:5050 --name di1-running di1-micro-web

# 6) Show status
docker ps -a
