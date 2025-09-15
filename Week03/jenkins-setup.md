
---

# 📄 Week03/jenkins-setup.md  

```markdown
# Jenkins Setup Notes – Week 3

## Installation Options
- Local VM (Linux/Mac with Docker or native Jenkins install)  
- Cloud VM (AWS EC2, GCP VM, Azure VM)  
- Docker container:
  ```bash
  docker run -d -p 8080:8080 -p 50000:50000 \
    -v jenkins_home:/var/jenkins_home \
    jenkins/jenkins:lts
