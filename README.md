# Flask Color App

A simple Flask application that changes its background color based on the APP_COLOR environment variable.

## Prerequisites

- Python 3.x
- Flask

## Installation

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
py app.py
```

Open:

```text
http://localhost:5000
```

## Environment Variable

APP_COLOR

Example:

```powershell
$env:APP_COLOR="blue"
py app.py
```

Change `blue` to `green`, `red`, or any valid CSS color name.

If APP_COLOR is not set, the application uses a default color.

## Docker

### Build the image

```bash
docker build -t flask-color-app .
```

### Run the container

```bash
docker run -p 5000:5000 -e APP_COLOR=green flask-color-app
```

### Access the application

Open:

http://localhost:5000


## AWS Deployment

### AWS Services Used

* Amazon EC2
* Amazon ECR (Elastic Container Registry)
* IAM User
* AWS CLI

### Steps Performed

1. Created an ECR repository.
2. Built and pushed the Docker image to ECR.
3. Launched an Amazon Linux 2023 EC2 instance.
4. Installed Docker on EC2.
5. Logged in to ECR from EC2.
6. Pulled the Docker image from ECR.
7. Ran the container on port 80.

### Application URL

http://13.61.25.175

### Docker Image

Stored in Amazon ECR:

728393074808.dkr.ecr.eu-north-1.amazonaws.com/flask-color-app

### Result

The Flask Color App is successfully deployed on AWS EC2 and accessible through a public IP address.


## CI/CD Automation with GitHub Actions

### Objective

Automate the build and deployment process whenever code is pushed to the main branch.

### Tools Used

* GitHub Actions
* Docker
* Amazon ECR
* Amazon EC2
* AWS IAM

### Workflow

1. Developer pushes code to the GitHub repository.
2. GitHub Actions automatically starts the workflow.
3. Docker image is built.
4. Docker image is pushed to Amazon ECR.
5. EC2 server pulls the latest image from ECR.
6. Existing container is stopped and removed.
7. A new container is started automatically.

### Pipeline Architecture

VS Code → GitHub → GitHub Actions → Amazon ECR → Amazon EC2 → Live Application

### Result

The application is automatically redeployed whenever changes are pushed to the main branch.

### Verification

A test change was made to the Flask application:

APP_COLOR = green - CI/CD Working!

After pushing the code, GitHub Actions successfully rebuilt and redeployed the application without manual intervention.


## Architecture Diagram

```text
Developer (VS Code)
        |
        v
     GitHub
        |
        v
 GitHub Actions
        |
        v
   Amazon ECR
        |
        v
   Amazon EC2
        |
        v
 Docker Container
        |
        v
 Flask Application
```

## Project Reflection

During this project, I learned the complete DevOps lifecycle, from application development to cloud deployment and CI/CD automation.

The first challenge was understanding Docker and containerization. I learned how to create a Dockerfile, build images, and run containers while passing environment variables to control application behavior.

The next challenge was deploying the application on AWS. I worked with Amazon ECR to store Docker images and Amazon EC2 to host the application. Configuring security groups and troubleshooting SSH connectivity helped me understand AWS networking concepts and access control.

The most valuable learning experience was implementing a CI/CD pipeline using GitHub Actions. I configured GitHub Secrets to securely manage credentials and automated the process of building Docker images, pushing them to ECR, and deploying updates to EC2. I verified the pipeline by making code changes and observing automatic deployment without manual intervention.

Through this project, I gained practical experience with Git, GitHub, Docker, Linux, AWS, and CI/CD practices. I also learned the importance of automation, security, documentation, and troubleshooting in modern DevOps workflows.
