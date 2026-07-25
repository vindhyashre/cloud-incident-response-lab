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
```

# Start the Application

## Clone repository:

git clone https://github.com/vindhyashre/cloud-incident-response-lab.git

## Move into project:

cd cloud-incident-response-lab

## Start containers:

docker compose up --build
Access Services
Service	URL
Application	http://localhost
Prometheus	http://localhost:9090
Grafana	http://localhost:3000
Node Exporter	http://localhost:9100

# 📊 Monitoring Dashboard

## Grafana monitors:

Application Metrics
HTTP request count
Error rate
Application availability
Infrastructure Metrics
CPU usage
Memory usage
Disk usage
Network statistics

# 🚨 Alerting

## Prometheus alert rules detect:

Application Down

## Condition:

up{job="application"} == 0

## Action:

Alert triggered
Engineer investigates
Service recovery performed
High CPU Usage

## Condition:

CPU usage > 80%

# 🧪 Incident Simulation
Simulate Application Failure

## Stop application:

docker stop flask-app

## Check alert:

Prometheus → Alerts

## Recover:

docker start flask-app

## Verify health:

.\scripts\check_health.ps1

# 🔧 Troubleshooting Commands

## Check containers:

docker ps

## View logs:

docker logs flask-app

## Check resource usage:

docker stats

## Restart services:

docker compose restart

# 📁 Project Structure
cloud-incident-response-lab

├── app
│   ├── app.py
│   └── requirements.txt
│
├── nginx
│   └── nginx.conf
│
├── prometheus
│   ├── prometheus.yml
│   └── rules
│       └── alerts.yml
│
├── scripts
│   ├── check_health.ps1
│   ├── stop_application.ps1
│   └── collect_logs.ps1
│
├── incidents
│   └── application-down.md
│
├── .github
│   └── workflows
│       └── docker-build.yml
│
├── Dockerfile
└── docker-compose.yml

# 🎯 Skills Demonstrated
Cloud infrastructure monitoring
Linux/container troubleshooting
Docker operations
Prometheus metrics
Grafana visualization
Incident response workflow
Alert configuration
CI/CD automation
Production troubleshooting practices

# 👩‍💻 Author

Vindhya Shree

Cloud Support Engineer Portfolio Project

Save the file.

## Then commit it:

```powershell
git add README.md
git commit -m "Add professional project README"
```

## Push:

git push
