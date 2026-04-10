# 🚀 Arcadex DevOps Project: Production-Grade CI/CD Pipeline

---
<img width="1536" height="1024" alt="ChatGPT Image Apr 10, 2026, 05_39_11 PM" src="https://github.com/user-attachments/assets/7662ebf5-ac92-45df-b8b5-958c375d2b4d" />


## 📌 Project Overview

This project demonstrates a **production-style DevOps pipeline** for a containerized Flask application using Jenkins, Docker, and Kubernetes.

The goal is to simulate a real-world environment where builds, testing, and deployments are **fully automated**, ensuring high availability, consistency, and faster delivery.

---

## 🏢 Company Scenario

Assume you are working as a **DevOps Engineer at Arcadex Studios**, a gaming company that builds and operates multiplayer online games.

Arcadex runs backend services responsible for:

- 🎮 Player sessions  
- ⚔️ Matchmaking  
- 🏆 Leaderboards  
- 📊 Analytics  

These services must be **highly available**, as downtime directly impacts user experience and revenue.

---

## 🎫 Task / Requirement

You were assigned the following task:

> Build a CI/CD pipeline for a lightweight backend service that exposes application health and version information.

This service will be used for:

- Deployment validation  
- Monitoring  
- Load balancer health checks  

---

## 🧠 Architecture

```
GitHub → Webhook → Jenkins → Docker Build → Docker Hub → Kubernetes → Live Application
```

---

## 🔄 CI/CD Workflow

1. Developer pushes code to GitHub  
2. GitHub Webhook triggers Jenkins pipeline  
3. Jenkins builds Docker image  
4. Docker image is pushed to Docker Hub  
5. Jenkins updates Kubernetes deployment  
6. Kubernetes pulls latest image  
7. Application is deployed automatically  

---

## ⚙️ Tech Stack

- **Cloud:** AWS EC2  
- **CI/CD:** Jenkins  
- **Containerization:** Docker  
- **Orchestration:** Kubernetes (KIND)  
- **Registry:** Docker Hub  
- **Version Control:** GitHub  
- **Language:** Python  
- **Framework:** Flask  

---

## ☸️ Kubernetes Deployment

- **Deployment:** Manages application pods  
- **Service:** Exposes application using NodePort  
- **Self-healing:** Pods automatically restart on failure  
- **Rolling updates:** Zero-downtime deployments  

---

## 🌐 Application Endpoints

- `/health` → Returns service health status  
- `/` → Returns basic application info  

---

## 🔥 Key Features

- Fully automated CI/CD pipeline  
- Dockerized Flask application  
- Multi-instance architecture (Jenkins + Kubernetes on separate EC2 instances)  
- Kubernetes-based deployment  
- Auto deployment on git push  
- Health-check based validation  
- Self-healing infrastructure  
- Versioned Docker image deployment  

---

## ⚠️ Challenges & Solutions

### 🔧 Docker permission issue in Jenkins
- Issue: Jenkins could not access Docker daemon  
- Fix: Added Jenkins container to Docker group  

### 🔧 Kubernetes ImagePullBackOff
- Issue: Incorrect image name/tag  
- Fix: Corrected Docker Hub repository and tags  

### 🔧 KIND networking issue
- Issue: Application not accessible externally  
- Fix: Configured extraPortMappings in KIND cluster  

### 🔧 Cross-instance communication
- Issue: Jenkins and Kubernetes running on different EC2 instances  
- Fix: Configured kubeconfig and kubectl access  

### 🔧 kubectl not found in Jenkins
- Issue: Jenkins pipeline failed during deployment  
- Fix: Installed kubectl inside Jenkins container  

---

## 📂 Project Structure

```
.
├── app.py
├── Dockerfile
├── Jenkinsfile
├── deployment.yaml
├── service.yaml
├── README.md
```

---

## 🚀 How to Run (High-Level)

1. Clone repository  
2. Set up Jenkins  
3. Configure Docker  
4. Deploy Kubernetes cluster (KIND)  
5. Configure webhook  
6. Push code to trigger pipeline  

---

## 🌍 Live Application

```
http://<YOUR-EC2-PUBLIC-IP>:30007/health
```

---

## 🧠 What is Flask?

Flask is a lightweight Python web framework used to build backend services and APIs.

It allows developers to:

- Create HTTP endpoints  
- Handle requests and responses  
- Build microservices quickly  

---

## 🎮 Flask in Arcadex (Use Case)

In Arcadex, Flask is used to build small backend services.

In this project, Flask is used to create a **Health Check Service**:

- Provides `/health` endpoint  
- Validates deployments in CI/CD  
- Helps load balancers route traffic  

---

## 🎯 Outcome

By completing this project, we achieved:

- A working Flask application  
- A Dockerized service  
- A fully automated CI/CD pipeline  
- Kubernetes-based deployment  
- Production-style DevOps workflow  

---

## 👨‍💻 Author

**Sarath V**  
DevOps Engineer | Cloud Enthusiast  

---
