# Message Queue Application

This is a message queue system based on Docker and Kubernetes, developed for learning and demonstration purposes. It uses Python FastAPI for the backend and includes a setup for Kubernetes deployment using Minikube.

## Features

- FastAPI-based API to manage messages.
- SQLite database for message storage.
- Scalable deployment in Kubernetes with load balancing.

---

## Requirements

- Docker
- Minikube
- Kubernetes CLI (`kubectl`)
- Python 3.10 or higher
- Dependencies listed in `requirements.txt`

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-user/message-queue.git
   cd message-queue
   ```

2. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate  # Windows
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

---

## Build and Run with Docker

1. Build the Docker image:

   ```bash
   docker build -t message-queue:latest .
   ```

2. Run the container on a specific port:

   ```bash
   docker run -d -p 8000:8000 message-queue:latest
   ```

3. (_Optional_) To expose the container on multiple ports for different access points (e.g., 8001 and 8002):

   ```bash
   docker run -d -p 8000:8000 -p 8001:8001 -p 8002:8002 message-queue:latest
   ```

   Ensure that FastAPI is configured to respond on multiple ports if necessary.

---

## Deploy with Minikube

1. Start Minikube:

   ```bash
   minikube start --driver=docker
   ```

2. Enable the local Docker environment for Minikube:

   ```bash
   eval $(minikube docker-env)
   ```

3. Build the Docker image within the Minikube context:

   ```bash
   docker build -t message-queue:latest .
   ```

4. Apply the Kubernetes manifests:

   ```bash
   kubectl apply -f kubernetes/deployment.yaml
   kubectl apply -f kubernetes/service.yaml
   ```

5. Check the pods and services:

   ```bash
   kubectl get pods
   kubectl get services
   ```

6. Get the service URL and test:

   ```bash
   minikube service message-queue-service --url
   ```

---

## Project Structure

```
message-queue/
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   └── main.py
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
├── tests/
├── venv/
├── .dockerignore
├── .gitignore
├── Dockerfile
├── messages.db
└── requirements.txt
```

---

