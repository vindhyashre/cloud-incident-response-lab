from flask import Flask, jsonify
import socket
from datetime import datetime
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Enable Prometheus metrics
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return """
    <h1>Cloud Incident Response Lab</h1>
    <p>Application Status: Running ✅</p>
    <p><a href="/health">Health Check</a></p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "hostname": socket.gethostname(),
        "timestamp": datetime.now().isoformat()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)