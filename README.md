# SupplyGuard-Tools
# SupplyGuard - supply-chain-collab-security

SupplyGuard is the first Microsoft 365 security layer designed to protect organisations
against a rapidly-emerging blind spot: **external Microsoft 365 tenants** used during
supplier collaboration.

While enterprises invest heavily in MFA, Conditional Access, DLP and Zero Trust inside
their own tenant, those controls disappear the moment a user opens a Teams meeting,
SharePoint folder or shared chat that belongs to a supplier’s tenant.

SupplyGuard changes that — by giving security and procurement teams:

- **One-click supplier onboarding**  
- **Automated permissions & governance**  
- **External tenant risk scoring (0–100)**  
- **Alerts when supplier posture becomes dangerous**
- **Auto-expiry and revocation controls**

This repository contains the open-source components, community documentation, example automation scripts, and integration foundations for the SupplyGuard product line.

---

##  What's Inside

| Component | Description |
|----------|------------|
| `/scripts` | Microsoft Graph automation scripts for onboarding, permissions, DLP and monitoring 🚀 |
| `/docs` | Product background, research, use cases and public technical insights |
| `/api` | OpenAPI model and integration specification |
| `/sample-data` | Example JSON responses and supplier metadata files |
| `/website` | GitHub Pages-ready documentation site |

---

## Try the MVP Scripts

> Requires: Microsoft Graph PowerShell SDK + Security / Global Admin role.

```pwsh
cd scripts
./Connect-Graph.ps1
./Create-Supplier-EntraInvite.ps1 -SupplierName "Acme Logistics"

# SupplyGuard.Tools

Secure supplier onboarding & external tenant visibility for Microsoft 365 — powered by Microsoft Graph.

This repository contains the **open-source tools** that inspired the [SupplyGuard](https://example.com) SaaS platform.

### Features
- One-click supplier onboarding to Teams/SharePoint
- External tenant discovery + CSV reporting
- Sensitivity label + DLP (optional)

📦 Install via PowerShell Gallery *(coming soon)*  
📚 Full documentation: [`/docs`](docs/)

Contributions welcome!

