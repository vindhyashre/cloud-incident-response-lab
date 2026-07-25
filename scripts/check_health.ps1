Write-Host "Checking application health..."

$response = Invoke-WebRequest http://localhost/health -UseBasicParsing

if ($response.StatusCode -eq 200) {
    Write-Host "✅ Application Healthy"
}
else {
    Write-Host "❌ Application Problem Detected"
}