# Week 5 – GitOps Setup (Part 1)

📅 **Timeline:** Oct 2025 (Week 5)  
🎯 **Objective:** Install and configure a GitOps tool (ArgoCD or Flux) on Kubernetes, connect the app manifests to the GitHub repo, and enable automated deployments to the cluster whenever code changes are committed.  

---

## ✅ This Week’s Focus
1. **Install GitOps Tool**
   - Choose **ArgoCD (preferred)** or **Flux**.  
   - Install on your Kubernetes cluster (Minikube or managed service).  
   - Expose the ArgoCD UI or verify Flux controllers are running.  

2. **Create Kubernetes Manifests**
   - Write basic manifests (`Deployment`, `Service`) for the Flask app.  
   - Store them in a dedicated repo folder: `infra/`.  
   - Example path: `infra/flask-app/`  

3. **Connect GitHub Repo to GitOps Tool**
   - Configure ArgoCD Application (or Flux Kustomization) to watch the `infra/` repo.  
   - Point it to `main` branch.  
   - Sync mode: **Automatic** (deploy new images/manifests without manual approval).  

4. **Test Auto-Deployment**
   - Commit updated manifest (e.g., image tag).  
   - Verify ArgoCD/Flux auto-syncs and deploys updated app to Kubernetes cluster.  
   - Validate using `kubectl get pods` and test app endpoint.  

---

## 📦 Deliverables by End of Week 5
- ✅ ArgoCD or Flux installed on Kubernetes cluster.  
- ✅ App manifests committed under `infra/`.  
- ✅ GitOps Application/Kustomization configured.  
- ✅ Successful auto-deployment triggered by a commit.  
- ✅ Screenshot(s) of ArgoCD/Flux dashboard showing sync status (`Week05/gitops-sync-screenshot.png`).  

---

## 📂 Suggested Structure for Week 5
```text
Week05/
├── README.md                     # Week 5 instructions
├── gitops-setup.md               # Notes: install steps, commands, screenshots
├── gitops-sync-screenshot.png    # ArgoCD/Flux sync success evidence
└── infra/
    └── flask-app/
        ├── deployment.yaml       # Flask Deployment manifest
        └── service.yaml          # Service manifest
