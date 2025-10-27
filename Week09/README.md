# Week 9 – Monitoring Setup (Part 1)

📅 **Timeline:** Nov 2025 (Week 9)  
🎯 **Objective:** Introduce monitoring and observability by installing **Prometheus** and **Grafana** on your Kubernetes cluster. Begin collecting **application and infrastructure metrics** to gain visibility into system health and performance.

---

## ✅ This Week’s Focus

1. **Install Prometheus**
   - Install **Prometheus** using Helm or YAML manifests.
   - Recommended Helm chart: [kube-prometheus-stack](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack)
   - Verify installation:
     ```bash
     kubectl get pods -n monitoring
     kubectl port-forward svc/prometheus-kube-prometheus-prometheus -n monitoring 9090:9090
     ```
   - Access Prometheus UI → http://localhost:9090  

2. **Install Grafana**
   - Installed automatically with kube-prometheus-stack (if using Helm).
   - Retrieve Grafana admin password:
     ```bash
     kubectl get secret --namespace monitoring grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
     ```
   - Port forward and open Grafana:
     ```bash
     kubectl port-forward svc/prometheus-grafana -n monitoring 3000:80
     ```
     URL → http://localhost:3000 (username: admin)

3. **Collect App & Infra Metrics**
   - Confirm Prometheus is scraping metrics from Kubernetes components.
   - Add **Flask app metrics endpoint** using the `prometheus_flask_exporter` library.
   - Update your Flask app (`app/app.py`) to include:
     ```python
     from prometheus_flask_exporter import PrometheusMetrics
     metrics = PrometheusMetrics(app)
     ```
   - Rebuild and deploy the app — Prometheus should auto-discover it via `kubelet` service discovery.

---

## 📦 Deliverables by End of Week 9
- ✅ Prometheus + Grafana installed and running (`monitoring` namespace).  
- ✅ Flask app instrumented with Prometheus metrics.  
- ✅ Prometheus scraping app and infra metrics successfully.  
- ✅ Screenshot(s) of Prometheus targets and Grafana dashboards committed:
  - `Week09/prometheus-targets.png`
  - `Week09/grafana-dashboard.png`

---

## 📂 Suggested Structure for Week 9
```text
Week09/
├── README.md                       # Week 9 instructions
├── prometheus-targets.png           # Screenshot of Prometheus targets page
├── grafana-dashboard.png            # Screenshot of Grafana UI with metrics
└── app/
    └── app.py                       # Updated Flask app with Prometheus metrics integration
