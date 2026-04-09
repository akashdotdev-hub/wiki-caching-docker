# 🚀 Wikipedia Speeder (A Caching Demonstration)

Welcome to **Wikipedia Speeder**! This repository demonstrates a fundamental performance optimization technique used in modern web architecture: the **Cache-Aside** pattern.

Built with **Python 3.11**, **Redis**, and **Docker Compose**, this project serves as a practical, hands-on example of how in-memory caching can drastically reduce API latency and minimize redundant external service calls.

---

## 🎯 The Goal: The 'Cache-Aside' Pattern

The core objective of this project is to illustrate the **Cache-Aside** strategy:
1. **🔍 Cache Check**: When a request for a Wikipedia topic is made, the application first checks the Redis cache.
2. **⚡ Cache Hit**: If the data is found in Redis, it is returned immediately (lightning fast!).
3. **🐢 Cache Miss**: If the data is missing, the application falls back to querying the Wikipedia API. The retrieved data is then saved in Redis for future requests, ensuring subsequent calls are instantly fulfilled.

---

## 🌍 Why This Matters (Context)

While this is a lightweight demonstration, it serves as a critical stepping stone toward managing **enterprise caching in RHEL (Red Hat Enterprise Linux)** environments.

Understanding how to orchestrate containers, manage application-to-cache communication, and handle cache invalidation is foundational before introducing more complex layers, such as setting up **Reverse Proxies (e.g., Nginx)**. This project solidifies the principles required to build scalable, high-performance cloud infrastructure.

---

## 🛠️ How to Run

Running the project is straightforward, thanks to Docker Compose. Ensure you have Docker installed, then run the following command in the root of the repository:

```bash
docker-compose up --build
```

The script will automatically start the Redis container, build the Python environment, and execute the demonstration script. You'll see the terminal output clearly showing the initial **Cache Miss** (fetching from Wikipedia) and the immediate subsequent **Cache Hit** (fetching from Redis).

---

## 🧠 Key Concepts Learned

- **⏱️ TTL (Time to Live)**: Managing cache expiration. The cached Wikipedia summaries are assigned a TTL (e.g., 60 seconds) to ensure data remains fresh and system memory isn't consumed indefinitely.
- **🐳 Container Orchestration**: Using Docker Compose to define, link, and manage multi-container applications (Python application + Redis cache), ensuring seamless networking and dependency management.

---

## 🗺️ Future Roadmap

- [ ] **Nginx Layer**: Introduce Nginx as a reverse proxy to manage incoming traffic and potentially serve as a web frontend or caching layer.
- [ ] **RHEL Deployment**: Deploy this containerized application onto a Red Hat Enterprise Linux (RHEL) environment to practice enterprise-grade system administration and configuration.

---
*Created as part of a Cloud Infrastructure and Systems Administration learning journey.*
