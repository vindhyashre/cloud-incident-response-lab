# Cloud Incident Response Lab 🚀

A production-style **Cloud Support Engineer / SRE portfolio project** that demonstrates application monitoring, infrastructure monitoring, alerting, troubleshooting, and incident response using Docker, Prometheus, Grafana, and automation scripts.

---

# 📌 Project Overview

This project simulates a real-world cloud support environment where an engineer:

- Deploys a containerized application
- Monitors application health
- Tracks infrastructure metrics
- Detects incidents through alerts
- Investigates failures
- Performs recovery actions
- Documents incidents

The goal is to demonstrate practical Cloud Support Engineer skills.

---

# ✨ Features

✅ Flask web application  
✅ Docker containerization  
✅ Docker Compose orchestration  
✅ Nginx reverse proxy  
✅ Prometheus metrics collection  
✅ Grafana monitoring dashboards  
✅ Node Exporter infrastructure monitoring  
✅ Prometheus alert rules  
✅ Incident simulation scripts  
✅ Health check automation  
✅ Incident documentation  
✅ GitHub Actions CI/CD pipeline  

---

# 🏗️ Architecture

```text
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
             +-------------+-------------+
             |                           |
             v                           v
       Prometheus                 Node Exporter
        Metrics                  System Metrics
             |
             v
          Grafana
        Dashboards
             |
             v
          Alerts
```

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Docker | Application containerization |
| Docker Compose | Multi-container management |
| Flask | Backend application |
| Nginx | Reverse proxy |
| Prometheus | Metrics collection and alerting |
| Grafana | Monitoring dashboards |
| Node Exporter | Server resource monitoring |
| GitHub Actions | CI/CD automation |
| PowerShell | Incident response scripts |
| Git | Version control |

---

# 📂 Project Structure

```text
cloud-incident-response-lab

│
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
├── docker-compose.yml
└── README.md
```

---

# 🚀 Installation and Setup

## Prerequisites

Install:

- Docker Desktop
- Git
- Python 3.x

Verify installation:

```bash
docker --version
docker compose version
git --version
python --version
```

---

# Clone Repository

```bash
git clone https://github.com/vindhyashre/cloud-incident-response-lab.git
```

Move into project:

```bash
cd cloud-incident-response-lab
```

---

# Start Application Stack

Build and start containers:

```bash
docker compose up --build
```

The following services will start:

- Flask Application
- Nginx
- Prometheus
- Grafana
- Node Exporter

---

# 🌐 Access Services

| Service | URL |
|---|---|
| Application | http://localhost |
| Prometheus | http://localhost:9090 |
| Grafana | http://localhost:3000 |
| Node Exporter | http://localhost:9100 |

---

# 📊 Monitoring Dashboard

Grafana dashboards monitor:

## Application Metrics

- HTTP request count
- Request rate
- Error rate
- Application availability

## Infrastructure Metrics

- CPU utilization
- Memory usage
- Disk usage
- Network statistics
- System performance

---

# 📈 Prometheus Metrics

Example application metric:

```promql
flask_http_request_total
```

Application availability:

```promql
up{job="application"}
```

---

# 🚨 Alerting System

Prometheus monitors system health and triggers alerts.

## Application Down Alert

Condition:

```promql
up{job="application"} == 0
```

Severity:

```
critical
```

Action:

1. Alert is triggered
2. Engineer investigates
3. Logs are collected
4. Service is restored
5. Health is verified

---

## High CPU Usage Alert

Condition:

```text
CPU usage > 80%
```

Severity:

```
warning
```

---

# 🧪 Incident Simulation

## Simulate Application Failure

Stop the application:

```powershell
docker stop flask-app
```

Prometheus detects:

```text
ApplicationDown - FIRING
```

---

## Investigate Issue

Check running containers:

```powershell
docker ps
```

View logs:

```powershell
docker logs flask-app
```

Check application health:

```powershell
.\scripts\check_health.ps1
```

---

## Recover Application

Restart service:

```powershell
docker start flask-app
```

Verify recovery:

```powershell
.\scripts\check_health.ps1
```

Expected:

```text
Application Healthy
```

---

# 🔧 Troubleshooting Commands

## Check Containers

```bash
docker ps
```

---

## View Application Logs

```bash
docker logs flask-app
```

---

## Check Resource Usage

```bash
docker stats
```

---

## Restart Services

```bash
docker compose restart
```

---

# 🤖 Automation Scripts

## Health Check

File:

```
scripts/check_health.ps1
```

Purpose:

- Verify application availability
- Reduce manual checks

---

## Stop Application Simulation

File:

```
scripts/stop_application.ps1
```

Purpose:

- Simulate production outage
- Test monitoring alerts

---

## Log Collection

File:

```
scripts/collect_logs.ps1
```

Purpose:

- Collect container logs during incidents

---

# 🔄 CI/CD Pipeline

GitHub Actions automatically:

- Checks out code
- Builds Docker image
- Verifies application build

Workflow:

```
Developer Push
       |
       v
GitHub Actions
       |
       v
Docker Build Test
       |
       v
Success / Failure
```

---

# 📝 Incident Response Example

Incident:

```
Flask Application Down
```

Detection:

```
Prometheus Alert: ApplicationDown
```

Investigation:

```
docker ps
docker logs flask-app
```

Resolution:

```
docker start flask-app
```

Verification:

```
Health Check Passed
```

Documentation:

```
incidents/application-down.md
```

---

# 🎯 Skills Demonstrated

- Cloud infrastructure monitoring
- Container troubleshooting
- Docker operations
- Prometheus configuration
- Grafana dashboard creation
- Alert management
- Incident response process
- Log investigation
- Automation scripting
- CI/CD fundamentals
- Production troubleshooting

---

# 🔮 Future Improvements

Planned enhancements:

- Add Alertmanager notifications
- Add Slack/Email alert integration
- Add Kubernetes deployment
- Add Terraform infrastructure
- Add AWS deployment
- Add centralized logging with Loki
- Add automated recovery

---

# 👩‍💻 Author

**Vindhya Shree**

Cloud Support Engineer Portfolio Project

---

⭐ If you find this project useful, consider giving it a star!
