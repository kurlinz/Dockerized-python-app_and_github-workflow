# TASK 1: Containers + CI/CD + Configuration Management

## PART 1
1. Build a container image, and push it into a registry
2. Create a Hello World Python Flask application with an endpoint (you can copy-paste example code from Flask documentation)
Prepare the Dockerfile, which can be used to build the container. Provide information how to build the image locally (with Docker/Podman) and run the container
3. Prepare CI process (GitHub Workflows/Gitlab CI), which builds the container image, and pushes it to a registry (e.g. Docker Hub, Quay.io, GitHub Container Registry). The CI should be run on push to main branch, and periodically on Saturday at 7 PM (push an image with the latest tag)


## STEPS
1. Create a remote repository on GitHub and clone to local machine
2. Python Flask Application
3. Build the docker image and push to Docker Hub
4. Deploy the application using Docker

## Requirements
1. VS code
2. Docker Hub account
3. GitHub account
4. Docker 


## Step 1: Create a remote repository and clone on local machine

Create a new repository on GitHub 

![Screenshot 2023-06-03 at 1 11 11 AM](https://github.com/kurlinz/python-app/assets/123019485/c2ae9a75-60df-4844-8983-54eedefa8ace)


Run the command below to clone to our host machine:

            git clone git@github.com:kurlinz/python-app.git


## Step 2: Python Flask Application Layout

cd into the cloned dicrectory and create the following files needed to dockerize our flask application. 

I. app.py

II. Dockerfile

We should have the files in python-app

      ls


### i. **app.py** - the Python script to build our Flask Application

Here is the code for the simple Flask App:

![Screenshot 2023-06-03 at 1 10 24 AM](https://github.com/kurlinz/python-app/assets/123019485/c08ae450-6030-48ec-bf59-ad4ea5d0fed8)

To containerize the application we use **app.run(host="0.0.0.0", port=80)** because the local port **127.0.0.1** cannot be captured inside a Docker container. Also, Flask uses port **5000** by default, so we change it to port **80**.


### ii. Create a Dockerfile

A Dockerfile will be used to create an image for our Flask App. It contains instructions on how to create the Flask App.

![Screenshot 2023-06-03 at 10 24 29 AM](https://github.com/kurlinz/python-app/assets/123019485/ad58424a-4ac8-45e7-a232-76156d55a5ab)

## Step 3: Build the Docker Image and push to Docker Hub

Next, we build the image from the Dockerfile and verify its created:

        docker build -t interview-test-app .


Then, view created image:

  
        docker images

##### Building the image

![Screenshot 2023-06-03 at 1 23 52 AM](https://github.com/kurlinz/python-app/assets/123019485/48bef4c0-2d1d-4384-a73f-89d2825e314d)

##### Verify the created image
 
![Screenshot 2023-06-03 at 1 24 50 AM](https://github.com/kurlinz/python-app/assets/123019485/a1b13d33-29e6-449b-ad47-f6d6c4fbee0e)

Next, we push the built image to Docker Hub. To do this, we need to log in to Docker Hub first.

Log in

              docker login

we create a tag, then push

              docker tag interview-test-app:1.0 kurlinz/interview-test-app:1.0
              Docker push kurlinz/interview-test-app:1.0

![Screenshot 2023-06-03 at 10 31 01 AM](https://github.com/kurlinz/python-app/assets/123019485/186412f8-2dc6-4061-a5c9-37818b5aca34)

![Screenshot 2023-06-03 at 2 48 41 AM](https://github.com/kurlinz/python-app/assets/123019485/834c41bf-7a2c-46c2-b88a-de42c072fe4f)


## Step 4: Deploy the application using Docker

Now we will run the container image and view the running container. Once this is done, we verify our deployed python-app by navigating to **http://localhost:80/** to access our Flask web application on a browser or on the terminal with the **curl** command to see the contents of the webpage.  

              docker run -d -p 80:80 --name python-app kurlinz/interview-test-app:1.0
              
Note that the **-p 80:80** parameter, maps the port 80 on the docker container to port 80 on the host. This shows that we are able to access the Flask app on port 80.

Verify the running container

              docker ps

View the web page




![Screenshot 2023-06-03 at 10 40 59 AM](https://github.com/kurlinz/python-app/assets/123019485/682c3f47-21e4-44d4-b332-04e62554ca46)


![Screenshot 2023-06-03 at 10 43 54 AM](https://github.com/kurlinz/python-app/assets/123019485/98733c18-1124-4cc6-9a4f-0381a0598c05)


Stop the running container

              docker stop <container name or ID>

Verify 

              docker ps









