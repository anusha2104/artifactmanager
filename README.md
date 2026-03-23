# Artifact Manager (DevOps Project)

**Student Name:** Anusha Mittal
**Registration No:** 23FE10CSE00771
**Course:** CSE3253 DevOps
**Semester:** VI

---

## 🚀 Project Overview

### 🔍 Problem Statement

In modern software development, managing build artifacts manually leads to:

* Version conflicts
* Deployment inconsistencies
* Lack of traceability

---

### 💡 Solution

This project implements a **centralized Artifact Manager** that:

* Stores build outputs
* Maintains version history
* Enables easy retrieval and deployment

---

## ✨ Key Features

* Upload artifacts with versioning
* Store metadata in PostgreSQL
* Download stored artifacts
* Checksum verification
* REST API support
* Containerized using Docker
* CI/CD pipeline using Jenkins

---

## 🧱 Architecture

User → Flask App → PostgreSQL → Storage
↑
Docker Containers
↑
Jenkins Pipeline

---

## 🛠️ Tech Stack

### Core Technologies

* Python (Flask)
* PostgreSQL

### DevOps Tools

* Git & GitHub
* Docker & Docker Compose
* Jenkins (CI/CD Pipeline)

---

## ⚙️ Setup Instructions

### Run using Docker

```bash
docker-compose up --build
```

Then open:
http://localhost:5000

---

## 🔗 API Endpoints

| Endpoint               | Method | Description     |
| ---------------------- | ------ | --------------- |
| `/`                    | GET    | Check server    |
| `/upload`              | POST   | Upload artifact |
| `/artifacts`           | GET    | List artifacts  |
| `/download/<filename>` | GET    | Download file   |
| `/health`              | GET    | Health check    |

---

## 🔁 CI/CD Pipeline

Pipeline stages:

1. Checkout Code
2. Install Dependencies
3. Build Docker Image
4. Run Containers
5. Test API

---

## 📦 Docker Setup

* Flask app container
* PostgreSQL container
* Volume for persistent storage

---

## 🔮 Future Scope

* Kubernetes deployment
* AWS S3 integration
* User authentication
* UI dashboard

---

## 🧠 Learnings

* CI/CD pipeline implementation
* Containerization using Docker
* Backend + database integration
* DevOps workflow
