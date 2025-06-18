# 🚀 Simple Flask Web App - Dockerized

## 👤 Author
Ravi Kiran

## 📝 Description
This is a simple web application built using Flask. It is containerized with Docker and designed to demonstrate the basic DevOps workflow: version control, Dockerization, and local deployment.

---

## 🔧 Features
- Displays a styled welcome message
- Route: `/` — HTML welcome page
- Route: `/howareyou` — plain text response

---

## 📂 Project Structure
simple-webapp/
├── app.py            # Flask application
├── Dockerfile        # Docker build instructions
└── README.md         # Project documentation
---

## 🐳 Docker Instructions

### ✅ Build Docker Image
```bash
docker build -t simple-webapp .