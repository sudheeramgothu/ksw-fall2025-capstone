from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # exposes /metrics endpoint

@app.route("/")
def home():
    return {"message": "Hello, KSW Capstone with Monitoring!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

------
After deployment, visit:
http://<app-service-ip>:5000/metrics
You should see metrics like request count, latency, and response codes.



Verify Metrics Collection:

Check in Prometheus:

kubectl port-forward svc/prometheus-kube-prometheus-prometheus -n monitoring 9090:9090


Then go to: http://localhost:9090
 → Status → Targets
You should see your flask-app endpoint listed as UP.
