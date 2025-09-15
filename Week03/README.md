# Week 3 – Jenkins Setup & CI Basics (Python/Flask)

📅 **Timeline:** Sept 2025 (Week 3)  
🎯 **Objective:** Install and configure Jenkins, connect it with the Flask app repository, and implement a basic CI pipeline (build + unit tests).  

---

## ✅ This Week’s Focus
1. **Jenkins Installation & Setup**
   - Install Jenkins locally or on a VM/cloud instance.  
   - Install required plugins: GitHub, Pipeline, Docker, JUnit.  
   - Configure Jenkins global tools: Python 3.x, Git, Docker.  

2. **GitHub → Jenkins Integration**
   - Connect Flask repo (`app/`) with Jenkins job.  
   - Use either:  
     - **Webhook (preferred)** → Trigger build on push/PR.  
     - **pollSCM** (temporary) → Check repo every 5 mins.  

3. **Pipeline Basics**
   - Use the starter `Jenkinsfile` from Week02 (`ops/`).  
   - Pipeline stages this week:  
     - Checkout  
     - Install dependencies (`requirements.txt`)  
     - Run unit tests (`pytest`)  

4. **Artifacts & Reports**
   - Store test reports using JUnit plugin.  
   - Archive test results in Jenkins for review.  

---

## 📦 Deliverables by End of Week 3
- ✅ Jenkins server up and running.  
- ✅ Flask repo connected to Jenkins (via webhook or pollSCM).  
- ✅ Basic CI pipeline working (checkout → install → tests).  
- ✅ Test results visible in Jenkins UI.  
- ✅ Pipeline log screenshot saved in repo (`Week03/jenkins-build-screenshot.png`).  

---

## 📂 Suggested Structure for Week 3
```text
Week03/
├── README.md                     # Week 3 instructions
├── jenkins-setup.md              # Notes: install steps, plugins, config screenshots
├── jenkins-build-screenshot.png  # Evidence of successful build
└── ops/
    └── Jenkinsfile.ci            # CI-only pipeline (build + test stages)
