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
