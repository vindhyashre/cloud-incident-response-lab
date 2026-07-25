Write-Host "🚨 Simulating Application Down Incident..."

docker stop flask-app

Write-Host "Application stopped."
Write-Host "Check Grafana/Prometheus alerts."