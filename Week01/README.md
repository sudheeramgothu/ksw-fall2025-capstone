# Week 1 – Kickoff & Planning  

📅 **Timeline:** Sept 2025 (Week 1)  
🎯 **Objective:** Get organized, set up repositories, assign roles, and draft the initial CI/CD architecture.  

---

## ✅ This Week’s Focus
1. **GitHub Setup**  
   - Create GitHub **organization** & repositories.  
   - Branching structure: `main` → `dev` → `feature/*`.  
   - Define **commit message format** (example: `feat: add Jenkinsfile`, `fix: Docker build issue`).  
   - Establish **PR review process** (at least 1 peer review before merge).  

2. **Role Assignment**  
   Assign student leads for:  
   - **CI/CD (Jenkins)**  
   - **GitOps/Kubernetes**  
   - **Monitoring (Prometheus/Grafana)**  
   - **Documentation / Project Management**  

3. **Draft CI/CD Architecture Diagram**  
   - Rough flow to include:  
     ```
     GitHub → Jenkins → Docker Registry → Kubernetes → ArgoCD/Flux → Monitoring (Prometheus/Grafana)
     ```  
   - Use any diagramming tool (Lucidchart, Draw.io, Excalidraw, or Mermaid in Markdown).  
   - Save diagram in repo under `Week01/diagram.png`.  

4. **Project Planning Document (1–2 pages)**  
   - Team roles & responsibilities.  
   - Selected tools (CI/CD, registry, monitoring).  
   - Initial timeline (based on 12-week roadmap).  
   - Repo setup details.  

---

## 📦 Deliverables by End of Week 1
- GitHub org + repos created & shared with mentor.  
- Team roles finalized & documented.  
- Draft CI/CD architecture diagram uploaded.  
- Initial project planning document committed to repo.  

---

## 📂 Suggested Repo Structure
```text
Week01/
├── README.md # Weekly plan (this file)
├── diagram.png # Draft CI/CD architecture diagram
└── project-plan.md # Team roles, tools, timeline
