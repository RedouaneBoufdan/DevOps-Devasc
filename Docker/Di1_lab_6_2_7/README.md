# Di1 – Lab 6.2.7 Microweb App in Docker

Goal: build a Docker image that runs a Flask microweb app with templates + static CSS.

Build:
docker build -t microweb_image .

Run:
docker run -d -p 5050:5050 --name microweb_container microweb_image

Test:
http://127.0.0.1:5050

Cleanup:
docker stop microweb_container
docker rm microweb_container
docker rmi microweb_image
