# Message Queue Application

## Description

The **Message Queue Application** is a lightweight, containerized backend application built with FastAPI to efficiently handle and manage messaging queues. It demonstrates the use of modern containerization techniques with **Docker** and **Kubernetes** for deployment, scaling, and load balancing.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Features](#features)
- [Running the Application](#running-the-application)
  - [Local Setup](#local-setup)
  - [Using Docker](#using-docker)
  - [Using Kubernetes](#using-kubernetes)
- [Scaling the Application](#scaling-the-application)
- [Testing Load Balancing](#testing-load-balancing)
- [Technologies Used](#technologies-used)

---

## Getting Started

### Prerequisites

1. Install **Python 3.11+**.
2. Install **Docker**.
3. Install **Minikube**.
4. Install **kubectl** for Kubernetes cluster management.

---

## Features

1. **FastAPI Backend**:
   - Manage message queues with lightweight endpoints.

2. **Containerized Deployment**:
   - Fully containerized using Docker.

3. **Scalable Architecture**:
   - Leverages Kubernetes for horizontal scaling.

4. **Load Balancing**:
   - Automatic traffic distribution across multiple pods.

---

## Running the Application

### Local Setup

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd message-queue
   ```

2. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Run the application locally:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t message-queue:latest .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 message-queue:latest
   ```

### Using Kubernetes

1. Start Minikube and use the Docker driver:
   ```bash
   minikube start --driver=docker
   ```

2. Build the Docker image in Minikube's Docker environment:
   ```bash
   eval $(minikube docker-env)
   docker build -t message-queue:latest .
   ```

3. Apply Kubernetes configurations:
   ```bash
   kubectl apply -f kubernetes/deployment.yaml
   kubectl apply -f kubernetes/service.yaml
   ```

4. Get the Minikube service URL:
   ```bash
   minikube service message-queue-service --url
   ```

---

## Scaling the Application

To scale the application horizontally in Kubernetes:

1. Use the `kubectl scale` command:
   ```bash
   kubectl scale deployment message-queue --replicas=<desired-replicas>
   ```
   Replace `<desired-replicas>` with the desired number of pods (e.g., 3).

2. Verify the scaling:
   ```bash
   kubectl get pods
   ```

3. Ensure functionality by testing endpoints and observing traffic distribution (see Load Balancing section).

---

## Testing Load Balancing

1. Obtain the Minikube service URL:
   ```bash
   minikube service message-queue-service --url
   ```

2. Send multiple requests to the service URL:
   ```bash
   curl http://<minikube-url>
   ```

3. Monitor pod logs to confirm distributed requests:
   ```bash
   kubectl logs -f <pod-name>
   ```
   Replace `<pod-name>` with the names of different pods. Requests should be distributed across pods.

4. View the enabled pods:
   ```bash
   kubectl get pods
   ```
   This command lists all active pods in the cluster, showing their names, statuses, and other details.

---

## Technologies Used

- **FastAPI**: For the backend application.
- **SQLite**: Lightweight database for queue management.
- **Docker**: Containerization of the application.
- **Kubernetes**: Deployment, scaling, and load balancing.
- **Minikube**: Local Kubernetes cluster setup.

---
