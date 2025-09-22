# Week 4 – Containerization (Flask App)

📅 **Timeline:** Oct 2025 (Week 4)  
🎯 **Objective:** Finalize Dockerfile for the Flask app, extend the Jenkins pipeline to build & push Docker images, and test the image locally in Docker or Kubernetes.

---

## ✅ This Week’s Focus
1. **Finalize Dockerfile**
   - Confirm `app/Dockerfile` is production-ready.  
   - Use **Gunicorn** (not `python app.py`) for serving Flask in containers.  
   - Confirm `requirements.txt` includes Flask + Gunicorn.

2. **Jenkins Pipeline – Build & Push**
   - Extend Jenkinsfile from Week03:  
     - Build Docker image.  
     - Tag image as `<REGISTRY>/<APP_NAME>:<BUILD_NUMBER>`.  
     - Push to a registry (Docker Hub or GitHub Container Registry).  
   - Secure registry credentials via Jenkins Credentials store.  

3. **Local/Kubernetes Testing**
   - Run container locally:
     ```bash
     docker run -p 5000:5000 <REGISTRY>/<APP_NAME>:<BUILD_NUMBER>
     ```
     Visit http://localhost:5000 → should return `{"message": "Hello, KSW Capstone!"}`.  

   - (Optional) Deploy to Kubernetes (Minikube or managed cluster):
     ```bash
     kubectl run flask-app --image=<REGISTRY>/<APP_NAME>:<BUILD_NUMBER> -p 5000
     kubectl expose pod flask-app --type=NodePort --port=5000
     minikube service flask-app
     ```

---

## 📦 Deliverables by End of Week 4
- ✅ Finalized Dockerfile using Gunicorn.  
- ✅ Jenkins pipeline builds & pushes Docker image successfully.  
- ✅ Image tested locally (`docker run`) or on Kubernetes (Minikube).  
- ✅ Screenshot of successful Jenkins build + Docker image push committed (`Week04/docker-build-screenshot.png`).  

---

## 📂 Suggested Structure for Week 4
```text
Week04/
├── README.md                     # Week 4 instructions
├── docker-build-screenshot.png   # Evidence of Jenkins build & push
├── k8s-test-commands.md          # Notes/screenshots of local or K8s test
└── snippets/
    ├── Dockerfile.gunicorn       # Production Dockerfile example
    └── Jenkinsfile.container     # Pipeline extended with build & push
