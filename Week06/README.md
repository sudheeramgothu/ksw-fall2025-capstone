# Week 6 – GitOps Setup (Part 2)

📅 **Timeline:** Oct 2025 (Week 6)  
🎯 **Objective:** Introduce configuration management using **Helm (preferred)** or **Kustomize**, document the end-to-end GitOps workflow, and demonstrate **automated rollouts** triggered by a repo change (e.g., image tag, values).

---

## ✅ This Week’s Focus
1. **Add Helm Charts (or Kustomize)**
   - Create a **Helm chart** for the Flask app (`infra/helm/flask-app/`).
   - Parameterize common settings: image repo/tag, replicas, service type/port.
   - If not using Helm, use **Kustomize overlays** (`infra/kustomize/`).

2. **Document GitOps Workflow**
   - Write a concise **runbook** explaining:  
     - Where manifests/values live  
     - How changes flow from Git → ArgoCD/Flux → Cluster  
     - How to bump image tags or config safely (PR → auto-sync)  
     - Rollback procedure

3. **Demo Auto-Deployment**
   - Change something **configurable** (e.g., `values.yaml` image tag or replica count).  
   - Commit to `main` (or merge a PR) → **ArgoCD/Flux auto-synces** → rollout happens.  
   - Capture a screenshot of the successful sync **and** a `kubectl` result.

---

## 📦 Deliverables by End of Week 6
- ✅ **Helm chart** (or Kustomize overlays) committed under `infra/`.  
- ✅ **GitOps runbook** documenting workflow and rollback.  
- ✅ **Auto-deployment demo** completed (config change → rollout).  
- ✅ Screenshots committed:  
  - `Week06/gitops-helm-sync.png` (ArgoCD/Flux)  
  - `Week06/kubectl-rollout-status.png`

---

## 📂 Suggested Structure for Week 6
```text
Week06/
├── README.md
├── gitops-runbook.md                 # How GitOps works end-to-end (with rollback)
├── gitops-helm-sync.png              # Screenshot: ArgoCD/Flux sync after values change
├── kubectl-rollout-status.png        # Screenshot: rollout status/replicas updated
└── infra/
    ├── helm/
    │   └── flask-app/
    │       ├── Chart.yaml
    │       ├── values.yaml
    │       └── templates/
    │           ├── deployment.yaml
    │           └── service.yaml
    └── kustomize/                    # (optional alternative)
        ├── base/
        │   ├── deployment.yaml
        │   └── service.yaml
        └── overlays/dev/
            └── kustomization.yaml
