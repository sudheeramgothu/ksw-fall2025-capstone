# Week 2 – Application & Repo Setup (Python/Flask)

📅 **Timeline:** Sept 2025 (Week 2)  
🎯 **Objective:** Select the sample Flask application, finalize repository structure/branch protections, and establish coding/PR standards. Prepare initial CI/CD and Docker scaffolding.

---

## ✅ This Week’s Focus
1. **Sample App Selection**
   - Use a simple **Flask web application** (Hello World starter or similar).
   - Ensure it has at least one test (we’ll use `pytest`).
   - Repo name suggestion: `flask-app`.

2. **Repository Structure & Protections**
   - Repos: `app` (Flask code), `infra` (K8s manifests/Helm) (NOT RECOMMENDED FOR YOU GUYS), `ops` (pipelines/config).
   - Branch model: `feature/*` → `dev` → `main`.
   - **Protect `main`** (require PR, 1 reviewer, status checks).

3. **Standards & Templates**
   - Add `CONTRIBUTING.md` (commit style, branching, PR rules).
   - Add `.github/PULL_REQUEST_TEMPLATE.md` and `ISSUE_TEMPLATE.md`.
   - Create a **Projects board** or use GitHub Issues with labels (`ci`, `k8s`, `docs`, `security`).

4. **Initial Scaffolding**
   - Place a **starter `Jenkinsfile`** in `ops/` (for Flask app build/test/package).
   - Place a **starter `Dockerfile`** in `app/`.
   - Create a `requirements.txt` file with Flask, Gunicorn, and Pytest.
   - Update the Week01 diagram to **v1.1** (include app repo + branch protections).

---

## 📦 Deliverables by End of Week 2
- ✅ Flask app repo created and available in org.  
- ✅ Branch protections enabled on `main`.  
- ✅ `CONTRIBUTING.md`, PR & Issue templates committed.  
- ✅ Starter `Jenkinsfile`, `Dockerfile`, and `requirements.txt` added.  
- ✅ Updated architecture diagram saved as `Week02/diagram-v1-1.png`.

---
## 📂 Suggested Structure for Week 2

```text
Week02/
├── README.md                # Week 2 instructions
├── app-repo-setup.md        # Links, decisions, screenshots
├── diagram-v1-1.png         # Updated CI/CD diagram (exported)
├── diagram-v1-1.mmd         # (optional) Mermaid source for edits
├── app/                     # Flask sample application
│   ├── app.py               # Minimal Flask app
│   ├── test_app.py          # Pytest unit test
│   ├── requirements.txt     # Flask, Gunicorn, Pytest
│   └── Dockerfile           # Flask container image definition
└── ops/
    └── Jenkinsfile          # Pipeline (install deps, tests, build & push image)
