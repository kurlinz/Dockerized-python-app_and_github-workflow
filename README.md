# python-app
Part of assessment for interview

#TASK 1:
I. Build a container image, and push it into a registry
II. Create a Hello World Python Flask application with an endpoint (you can copy-paste example code from Flask documentation)
Prepare the Dockerfile, which can be used to build the container. Provide information how to build the image locally (with Docker/Podman) and run the container
III. Prepare CI process (GitHub Workflows/Gitlab CI), which builds the container image, and pushes it to a registry (e.g. Docker Hub, Quay.io, GitHub Container Registry). The CI should be run on push to main branch, and periodically on Saturday at 7 PM (push an image with the latest tag)

#STEPS:
Create a remote repository on GitHub and clone to local machine
Python Flask Application
Build the docker image and push to Docker Hub
Deploy the application using Docker
