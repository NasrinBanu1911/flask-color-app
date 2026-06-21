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
