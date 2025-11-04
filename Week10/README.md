# Week 10 – Monitoring Setup (Part 2)

📅 **Timeline:** Nov 2025 (Week 10)  
🎯 **Objective:** Create Grafana dashboards to visualize **pipeline health, error rates, latency, and system performance**. Configure Prometheus queries to track application and infrastructure metrics, and save dashboard screenshots for documentation.

---

## ✅ This Week’s Focus

1. **Build Grafana Dashboards**
   - Access Grafana (http://localhost:3000).
   - Create custom dashboards for:
     - **Pipeline Health:** track CI/CD job duration, success/failure counts.
     - **Application Metrics:** Flask request rate, latency, HTTP errors.
     - **Infrastructure Metrics:** CPU/memory usage, node status, pod restarts.
   - Use **PromQL queries** to populate panels.

   Example PromQL queries:
   - Request rate:
     ```
     rate(flask_http_request_total[1m])
     ```
   - Error rate:
     ```
     rate(flask_http_request_exceptions_total[1m])
     ```
   - CPU usage:
     ```
     sum(rate(container_cpu_usage_seconds_total{namespace="default"}[5m])) by (pod)
     ```
   - Memory usage:
     ```
     sum(container_memory_usage_bytes{namespace="default"}) by (pod)
     ```

2. **Add Alerting (Optional but Recommended)**
   - Create alert rules in Grafana or Prometheus for:
     - High CPU usage  
     - Frequent HTTP 5xx errors  
     - Pod restarts  
   - Configure notifications (e.g., email or webhook if available).

3. **Export Dashboards for Reuse**
   - Export dashboards as JSON files.
   - Save under `Week10/dashboards/` folder for version control.
   - Example file: `Week10/dashboards/flask-metrics-dashboard.json`.

4. **Capture Screenshots**
   - Take screenshots of dashboards showing:
     - Application metrics (request rate, latency, errors)
     - System performance (CPU/memory)
     - CI/CD or GitOps pipeline health (if applicable)
   - Save them as:
     - `Week10/grafana-dashboard-app.png`
     - `Week10/grafana-dashboard-system.png`
     - `Week10/grafana-dashboard-pipeline.png` (optional)

---

## 📦 Deliverables by End of Week 10
- ✅ Custom Grafana dashboards created.  
- ✅ Panels showing app and infra metrics.  
- ✅ (Optional) Alert rules configured in Grafana or Prometheus.  
- ✅ Dashboard JSON exports saved in `Week10/dashboards/`.  
- ✅ Screenshots of dashboards committed (`Week10/grafana-dashboard-app.png`, `Week10/grafana-dashboard-system.png`).  

---

## 📂 Suggested Structure for Week 10
```text
Week10/
├── README.md                           # Week 10 instructions
├── grafana-dashboard-app.png           # Application metrics dashboard
├── grafana-dashboard-system.png        # System performance dashboard
├── grafana-dashboard-pipeline.png      # CI/CD or GitOps pipeline dashboard (optional)
└── dashboards/
    ├── flask-metrics-dashboard.json
    ├── system-performance-dashboard.json
    └── pipeline-health-dashboard.json


====
Example Dashboard Panels

Panel 1 – Flask Request Rate

Query: rate(flask_http_request_total[1m])

Type: Time series

Title: Request Rate (req/sec)

Panel 2 – Error Rate

Query: rate(flask_http_request_exceptions_total[1m])

Type: Time series

Title: Error Rate (5xx per sec)

Panel 3 – CPU & Memory

CPU Query: sum(rate(container_cpu_usage_seconds_total{namespace="default"}[5m])) by (pod)

Memory Query: sum(container_memory_usage_bytes{namespace="default"}) by (pod)

Type: Combined graph

Title: Resource Utilization by Pod

Panel 4 – Pod Restarts

Query: sum(kube_pod_container_status_restarts_total) by (pod)

Type: Bar chart

Title: Pod Restarts Count
