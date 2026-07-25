Write-Host "Collecting container logs..."

docker logs flask-app > incidents\application_logs.txt

Write-Host "Logs saved."