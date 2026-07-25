# Cloud Incident Response Lab 🚀

A production-style Cloud Support Engineer project that demonstrates application monitoring, infrastructure monitoring, alerting, and incident response using Docker, Prometheus, and Grafana.

## 📌 Project Overview

This project simulates a real-world cloud support environment where an engineer monitors a containerized application, detects incidents, investigates issues, and restores services.

The lab includes:

- Flask application
- Docker containerization
- Nginx reverse proxy
- Prometheus monitoring
- Grafana dashboards
- Node Exporter infrastructure monitoring
- Alert rules
- Incident response automation scripts
- GitHub Actions CI/CD

---

# 🏗️ Architecture

                User
                 |
                 v
              Nginx
            Port: 80
                 |
                 v
        Flask Application
            Port: 5000
                 |
      +----------+----------+
      |                     |
      v                     v
 Prometheus            Node Exporter
  Metrics              System Metrics
      |
      v
   Grafana
 Dashboards
      |
      v
   Alerts

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Docker | Containerization |
| Docker Compose | Multi-container deployment |
| Flask | Application service |
| Nginx | Reverse proxy |
| Prometheus | Metrics collection |
| Grafana | Monitoring dashboards |
| Node Exporter | Server metrics |
| GitHub Actions | CI/CD automation |
| PowerShell | Incident automation scripts |

---

# 🚀 Setup Instructions

## Requirements

Install:

- Docker Desktop
- Git
- Python 3.x

Verify:

```bash
docker --version
docker compose version
git --version
