# Week 8 – DevSecOps Integration (Part 2)

📅 **Timeline:** Oct 2025 (Week 8)  
🎯 **Objective:** Strengthen cluster and pipeline security by refining **RBAC roles**, implementing **secrets management**, and ensuring that sensitive data (e.g., credentials, tokens, passwords) are stored and used securely.

---

## ✅ This Week’s Focus

1. **Refine RBAC Roles**
   - Review and update your existing RBAC configuration from Week 7 (`infra/security/rbac.yaml`).
   - Ensure separation of duties between:
     - **Application service account** (for pod access)
     - **GitOps service account** (for ArgoCD/Flux)
   - Add namespace scoping if your cluster has multiple namespaces.
   - Remove unnecessary permissions and verify access with:
     ```bash
     kubectl auth can-i list pods --as=system:serviceaccount:default:flask-app-sa
     ```

2. **Add Secrets Management**
   - Create Kubernetes **Secrets** to store sensitive values such as:
     - Database credentials
     - API keys or tokens
     - Docker registry credentials (if not already in Jenkins)
   - Mount or inject these secrets into your application deployment securely.
   - Save manifests under `infra/security/secrets.yaml`.

   Example:
   ```bash
   kubectl create secret generic flask-secrets \
     --from-literal=DB_USER=flaskuser \
     --from-literal=DB_PASS=flaskpass
   kubectl get secrets

3. **Integrate Secrets into Deployment**

- Reference secrets in your infra/helm/flask-app/values.yaml or deployment manifest.
- Ensure secrets are never stored directly in Git in plain text.
- (Optional) If possible, explore integrating HashiCorp Vault or Sealed Secrets for advanced encryption.

  **Deliverables by End of Week 8**

✅ Updated and verified RBAC configuration (infra/security/rbac.yaml).

✅ Kubernetes secrets created and used by application (infra/security/secrets.yaml).

✅ Application deployment successfully reading secrets at runtime.

✅ Screenshot of secret usage or verification (Week08/k8s-secrets-screenshot.png).

'''
Week08/
├── README.md                        # Week 8 instructions
├── k8s-secrets-screenshot.png       # Screenshot showing secret creation or usage
└── infra/
    └── security/
        ├── rbac.yaml                # Refined roles & bindings
        └── secrets.yaml             # K8s Secrets manifest (base64 encoded)

'''
