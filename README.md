
# Logging & Monitoring API (FastAPI)

## 📌 Project Overview

This project demonstrates **structured logging and basic application monitoring** using **FastAPI**.
It exposes system-level endpoints to check application **health** and **performance metrics**, and uses **middleware** to log every HTTP request in a structured (JSON) format.

## 🎯 Objectives

* Implement **structured logging** (JSON logs)
* Track request behavior using **middleware**
* Expose monitoring endpoints:

  * `/health` – application health
  * `/metrics` – application performance
* Follow clean backend architecture

---

## 🛠 Tech Stack

* **Python**
* **FastAPI**
* **Uvicorn**
* **Standard Python Logging**

---

## 📂 Project Structure

```
monitoring_api/
│
├── app/
│   ├── main.py                # Application entry point
│   ├── logging_config.py      # JSON structured logging setup
│   ├── middleware.py          # Request logging & metrics middleware
│   ├── routes/
│   │   ├── health.py          # /health endpoint
│   │   ├── metrics.py         # /metrics endpoint
│   │  
│
├── requirements.txt
└── README.md
```

---

## 🔍 Key Concepts Used

### 1️⃣ Structured Logging

* Logs are generated in **JSON format**
* Each log contains:

  * HTTP method
  * Request path
  * Status code
  * Response time

Example log:

```json
{
  "event": "http_request",
  "method": "GET",
  "path": "/health",
  "status_code": 200,
  "duration_ms": 2.4
}
```

---

### 2️⃣ Middleware

Middleware is used to:

* Log **every request automatically**
* Measure response time
* Count total requests

This avoids repeating logging logic inside every route and follows **industry best practices**.

---

### 3️⃣ Health Endpoint

**Endpoint:** `GET /health`

Purpose:

* Check if the application is running
* Used by load balancers and monitoring systems

Response:

```json
{
  "status": "ok",
  "service": "monitoring-api"
}
```

---

### 4️⃣ Metrics Endpoint

**Endpoint:** `GET /metrics`

Purpose:

* Expose application performance data

Response:

```json
{
  "uptime_seconds": 120.45,
  "total_requests": 18
}
```

