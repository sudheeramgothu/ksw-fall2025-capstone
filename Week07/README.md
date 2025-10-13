# Week 7 – DevSecOps Integration (Part 1)

📅 **Timeline:** Oct 2025 (Week 7)  
🎯 **Objective:** Strengthen the CI/CD pipeline by applying Kubernetes **RBAC policies**, integrating **vulnerability scanning** with Trivy, and adding a **security stage** to the Jenkins pipeline.

---

## ✅ This Week’s Focus

1. **Apply Kubernetes RBAC Policies**
   - Define **roles and role bindings** for your Flask app and GitOps components.
   - Restrict permissions to follow **least privilege** principles.
   - Create a new file under `infra/security/rbac.yaml` to define:
     - Role → e.g., access to pods, services, and deployments only.
     - RoleBinding → link the Role to your ServiceAccount used by ArgoCD or the application.

2. **Run Vulnerability Scans with Trivy**
   - Install **Trivy** locally or use the Docker container:
     ```bash
     docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy image <REGISTRY>/<APP_NAME>:<TAG>
     ```
   - Scan the built Docker image for vulnerabilities.
   - Save a sample Trivy report (`Week07/trivy-report.txt`).
   - Identify any **high/critical vulnerabilities** and summarize findings.

3. **Add Scanning Stage to Jenkinsfile**
   - Update your Jenkinsfile to include a **Security Scan** stage after the build stage.
   - The pipeline should:
     - Run Trivy scan inside Jenkins.
     - Archive scan results as artifacts.
     - Optionally, fail the build on high severity findings.

---

## 📦 Deliverables by End of Week 7
- ✅ `infra/security/rbac.yaml` created and applied to cluster.  
- ✅ Trivy scan completed and results saved (`Week07/trivy-report.txt`).  
- ✅ Jenkinsfile updated with a Security Scan stage.  
- ✅ Screenshot of Jenkins security scan stage (`Week07/jenkins-security-stage.png`).  

---

## 📂 Suggested Structure for Week 7
```text
Week07/
├── README.md                       # Week 7 instructions
├── trivy-report.txt                # Vulnerability scan results
├── jenkins-security-stage.png      # Screenshot of Jenkins pipeline scan stage
└── infra/
    └── security/
        └── rbac.yaml               # RBAC roles and bindings
