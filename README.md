# ksw-fall2025-capstone
KSW University Fall 2025 Capstone – Cloud-Native CI/CD pipeline with Kubernetes, GitOps, DevSecOps, and Observability. Mentorship-driven academic–industry project guided by Sudheer Amgothu.

This repository documents the KSW University Fall 2025 Capstone Project, mentored by Sudheer Amgothu (Principal Cloud Operations Engineer).
Over 12 weeks, students will:

Build a CI/CD pipeline with Jenkins and GitHub.

Deploy applications on Kubernetes clusters using GitOps (ArgoCD/Flux).

Integrate DevSecOps practices (RBAC, vulnerability scans).

Implement monitoring & observability with Prometheus and Grafana.

Deliver a final demo, documentation, and presentation at Computing Showcase Day (Dec 2025).


# KSW University – Fall 2025 Capstone  
## Project: Cloud-Native CI/CD Pipeline with Kubernetes, GitOps, Security, and Observability  

👨‍🏫 **Mentor:** Sudheer Amgothu, Principal Cloud Operations Engineer  
🎓 **Teams:** KSW University Capstone Students (Fall 2025)  
📅 **Duration:** Sept – Dec 2025 (12 Weeks)  

---

## 🎯 Project Objectives
- Design and implement a **cloud-native CI/CD pipeline** using industry-standard tools.  
- Deploy a sample application to **Kubernetes clusters with GitOps automation**.  
- Integrate **DevSecOps practices** (RBAC policies, vulnerability scanning).  
- Enable **observability** with Prometheus and Grafana dashboards.  
- Deliver a **final demo + technical documentation** for Computing Showcase Day (C-Day).  

---

## 📅 Timeline & Milestones  

# 📅 Capstone Milestone Plan (KSW Fall 2025)

## Milestone 1 – Presentation of Plan  
🗓️ **Due: Sept 30 (Weeks 1–3)**  
🎯 **Goal:** Show project planning, repo setup, architecture, and initial CI pipeline.  

**Weeks Covered:**  
- **Week 1 – Kickoff & Planning**  
  - Team roles assigned  
  - GitHub org/repos created  
  - Draft architecture diagram (`diagram.png`)  
  - Project plan doc committed  

- **Week 2 – Application & Repo Setup (Flask)**  
  - Flask app added with minimal test  
  - Branch protections on `main`  
  - CONTRIBUTING.md + PR templates  
  - Starter Dockerfile + Jenkinsfile committed  
  - Updated architecture diagram (`diagram-v1-1.png`)  

- **Week 3 – Jenkins Setup & CI Basics**  
  - Jenkins server installed & configured  
  - Repo integrated with Jenkins (webhook or pollSCM)  
  - CI pipeline runs build + unit tests  
  - Test results archived in Jenkins  
  - Screenshot of working build committed  

**Deliverables for Milestone 1 (Sep 30):**  
- GitHub repos & standards in place  
- Project planning doc  
- Architecture diagram (v1.1)  
- Working Flask app with tests  
- Jenkins CI pipeline running & producing reports  

---

## Milestone 2 – Midpoint Progress Update  
🗓️ **Due: Oct 28 (Weeks 4–8)**  
🎯 **Goal:** Show working CI/CD pipeline with containerization, GitOps, and security integration.  

**Weeks Covered:**  
- **Week 4 – Containerization**  
  - Finalize Dockerfile for Flask app  
  - Jenkins pipeline builds & pushes image to registry  
  - Test image locally in Docker/Kubernetes  

- **Week 5 – GitOps Setup (Part 1)**  
  - Install ArgoCD or Flux on Kubernetes  
  - Connect app manifests to GitHub repo  
  - Auto-deploy on commit → cluster  

- **Week 6 – GitOps Setup (Part 2)**  
  - Add Helm charts or K8s manifests for configuration  
  - Document GitOps workflow  
  - Demo app auto-deployment  

- **Week 7 – DevSecOps Integration (Part 1)**  
  - Apply Kubernetes RBAC policies  
  - Run vulnerability scans with Trivy  
  - Add scanning stage to Jenkinsfile  

- **Week 8 – DevSecOps Integration (Part 2)**  
  - Refine RBAC roles  
  - Add secrets management (e.g., K8s secrets, Vault optional)  

**Deliverables for Milestone 2 (Oct 28):**  
- Working CI/CD pipeline (build → image push → GitOps → cluster)  
- Flask app running in Kubernetes  
- RBAC & security scans integrated  
- Architecture diagram updated to include GitOps + security  
- Documentation updated (Week 4–8 progress)  

---

## Milestone 3 – Final Presentation  
🗓️ **Due: Dec 2 (Weeks 9–11)**  
🎯 **Goal:** Finalize monitoring/observability, polish documentation, and rehearse for C-Day.  

**Weeks Covered:**  
- **Week 9 – Monitoring Setup (Part 1)**  
  - Install Prometheus + Grafana  
  - Collect app + infra metrics  

- **Week 10 – Monitoring Setup (Part 2)**  
  - Build dashboards (pipeline health, error rates, latency, CPU/memory)  
  - Save screenshots to repo  

- **Week 11 – Documentation & Prep**  
  - Finalize technical report (15–20 pages)  
  - Refined architecture diagrams  
  - Pitch deck + demo script  
  - Dry run of presentation  

**Deliverables for Milestone 3 (Dec 2):**  
- Monitoring dashboards (Grafana screenshots)  
- Documentation complete (report, diagrams, configs, troubleshooting)  
- Final repo structure clean & organized  
- Pitch deck ready  

---

## C-Day – Computing Showcase Day  
🗓️ **Dec 4, 2025 (Week 12)**  
- Students deliver **live demo + presentation**.  
- Submit final deliverables to faculty.  

---

## Final Review & Submission  
🗓️ **Dec 10, 2025**  
- Final repo + documentation delivered.  
- Mentor provides feedback.  


---

## 📂 Repo Structure  

```text
├── README.md # Overview (this file)
├── Week01/ # Week 1 tasks, diagrams, docs
├── Week02/
├── Week03/
├── ...
├── Week12/
└── resources/ # Shared resources (configs, diagrams, sample code)


---

## 🛠️ Tools & Technologies  

- **CI/CD:** Jenkins, GitHub Actions (optional)  
- **Containers:** Docker  
- **Kubernetes:** Minikube / EKS / GKE / AKS  
- **GitOps:** ArgoCD / Flux  
- **Monitoring:** Prometheus, Grafana  
- **Security:** Trivy, Kubernetes RBAC, Vault (optional)  
- **Collaboration:** GitHub, Teams  

---

## 🧑‍💻 Team Roles  

- **CI/CD Lead** – Jenkins & pipeline automation  
- **Kubernetes/GitOps Lead** – Cluster deployments & GitOps integration  
- **Monitoring Lead** – Observability dashboards (Prometheus/Grafana)  
- **Documentation/PM Lead** – Docs, reports, project tracking  

---

## 📌 Notes for Students  

- Follow weekly instructions under each `WeekXX/README.md`.  
- Use meaningful commit messages (e.g., `feat: add Dockerfile for app`).  
- Submit deliverables by the **end of each week** for mentor review.  
- These tasks build directly toward KSW’s official **3 milestones + C-Day**.  

---

## 🚀 Expected Outcomes  

By the end of Week 12, the teams will deliver:  
- ✅ A **working CI/CD pipeline** with Jenkins + Docker  
- ✅ Automated **GitOps deployments** to Kubernetes  
- ✅ Integrated **DevSecOps practices** (RBAC + vulnerability scanning)  
- ✅ Real-time **monitoring dashboards** with Grafana  
- ✅ A polished **final report + live demo** at Computing Showcase Day (Dec 4, 2025)  

---
