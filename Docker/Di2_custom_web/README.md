# Di2 – Custom Docker Web Image

## Task name
Docker – Custom Web Image (Di2)

## Task preparation
- Docker Desktop installed
- Basic Flask application created
- Project structured with templates and static folders

## Task implementation
- Created a custom Dockerfile based on python:3.10-slim
- Copied Flask app, templates and static files into the image
- Installed Flask via pip inside the container
- Exposed port 8080
- Built the image and ran a container with port mapping (8081 → 8080)

## Task troubleshooting
- Docker build initially failed because the Dockerfile had a `.txt` extension
- Fixed by renaming `Dockerfile.txt` to `Dockerfile`

## Task verification
- `docker ps` shows the running container
- Web application accessible via http://localhost:8081
- Docker logs confirm Flask server is running
