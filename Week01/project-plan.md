# Project Plan – Week 01 (KSW Fall 2025 Capstone)

## 1. Team & Roles
- **Team Name:** <!-- e.g., Cloud Ninjas -->
- **Members & Emails:**
  - Name A – role – email
  - Name B – role – email
  - Name C – role – email
  - Name D – role – email

### Role Ownership (Milestone 1)
- **CI/CD Lead (Jenkins):** <!-- Name -->
  - Pipeline design, Jenkinsfile ownership, build/test stages
- **Kubernetes/GitOps Lead:** <!-- Name -->
  - Manifests/Helm, ArgoCD/Flux setup, deployment strategy
- **Monitoring Lead (Prometheus/Grafana):** <!-- Name -->
  - Exporters/metrics, dashboards, alerts (later milestones)
- **Documentation/PM Lead:** <!-- Name -->
  - Weekly notes, diagrams, README, meeting minutes, deadlines

## 2. Scope (Week 1 → Week 12)
- **Goal:** Build a cloud-native CI/CD pipeline that automates build → containerize → deploy to Kubernetes via GitOps, with security & observability.
- **Week 1 Deliverables:** GitHub org/repos, role assignments, draft architecture diagram, 1–2 page plan (this doc).

## 3. Repositories & Branching
- **Org/Owner:** <!-- University org or link -->
- **Repos:**
  - `app` – sample application
  - `infra` – IaC / K8s manifests / Helm charts
  - `ops` – Jenkins pipeline config, scripts, docs
- **Branching Model:** `feature/*` → `dev` → `main`
- **PR Policy:** Min. 1 peer review, status checks must pass, squash merge

## 4. Tools & Versions (initial)
- **Source Control:** GitHub
- **CI:** Jenkins (LTS)  
- **Containers:** Docker
- **Kubernetes:** Minikube (local) or managed (EKS/GKE/AKS) later
- **GitOps:** ArgoCD **or** Flux (choose one by Week 5)
- **Registry:** Docker Hub / GHCR
- **Security:** Trivy (Week 6+), K8s RBAC
- **Observability:** Prometheus, Grafana (Weeks 7–10)
- **Diagrams:** Draw.io / Excalidraw / Mermaid

## 5. Initial Architecture (Draft)
High-level flow to refine in Week 3–6:

GitHub → Jenkins → Docker Registry → Kubernetes
↓ ↑
Tests ArgoCD/Flux (pull-based deploy)
→ Prometheus/Grafana (metrics/dashboards)

## 6. Approvals
- **Student Lead:** <!-- name & date -->
- **Mentor (Sudheer Amgothu):** <!-- date -->
