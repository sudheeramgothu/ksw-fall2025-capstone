from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)  # exposes /metrics endpoint

@app.route("/")
def home():
    return {"message": "Hello, KSW Capstone with Monitoring!"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
