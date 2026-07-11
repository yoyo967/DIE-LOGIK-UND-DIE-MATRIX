# 2. Systemarchitektur-Überblick

### 2.1 High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    SOVEREIGN SYSTEM ARCHITECTURE                 │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐     ┌──────────────────────────────────────┐  │
│  │  Android App  │◄───►│   Firebase / GCP Backend             │  │
│  │  (Kotlin/     │     │                                      │  │
│  │   Compose)    │     │  ┌────────────────────────────────┐  │  │
│  │              │     │  │   ORCHESTRATOR (The Brain)      │  │  │
│  │  • Dashboard  │     │  │   Cloud Run (europe-west1)     │  │  │
│  │  • Approvals  │     │  │                                │  │  │
│  │  • Settings   │     │  │  ┌──────┐ ┌──────┐ ┌───────┐  │  │  │
│  │  • History    │     │  │  │Negot.│ │Switch│ │ Claim │  │  │  │
│  │              │     │  │  │Node  │ │Node  │ │ Node  │  │  │  │
│  └──────────────┘     │  │  └──┬───┘ └──┬───┘ └──┬────┘  │  │  │
│                       │  │     │        │        │       │  │  │
│                       │  └─────┼────────┼────────┼───────┘  │  │
│                       │        │        │        │          │  │
│  ┌──────────────┐     │  ┌─────▼────────▼────────▼───────┐  │  │
│  │ SENSING      │     │  │   EXECUTION LAYER             │  │  │
│  │ LAYER        │     │  │   • E-Mail-Dispatch (SMTP)    │  │  │
│  │              │     │  │   • Form Submission APIs      │  │  │
│  │ • Gmail API  │────►│  │   • Provider Switching APIs   │  │  │
│  │ • PSD2/Open  │     │  │   • Claim Filing APIs         │  │  │
│  │   Banking    │     │  └───────────────┬───────────────┘  │  │
│  │ • Calendar   │     │                  │                   │  │
│  └──────────────┘     │  ┌───────────────▼───────────────┐  │  │
│                       │  │   MONETIZATION LAYER          │  │  │
│  ┌──────────────┐     │  │   • Stripe Metered Billing    │  │  │
│  │ PAYMENT      │     │  │   • Affiliate Network APIs    │  │  │
│  │ LAYER        │     │  │   • Treuhand-Konto (Solaris)  │  │  │
│  │              │     │  │   • Mastercard Agent Pay      │  │  │
│  │ • Stripe     │◄───│  └───────────────────────────────┘  │  │
│  │ • MC AgentPay│     │                                      │  │
│  │ • Solaris    │     │  ┌───────────────────────────────┐  │  │
│  └──────────────┘     │  │   DATA LAYER                  │  │  │
│                       │  │   • Firestore (europe-west3)  │  │  │
│                       │  │   • Cloud Storage (Dokumente) │  │  │
│                       │  │   • BigQuery (Analytics)      │  │  │
│                       │  └───────────────────────────────┘  │  │
│                       └──────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

### 2.2 Die vier APEX-Schichten

1.  **DATA LAYER (AgentMemory / Personal Data Warehouse):**  
    Ein composable Customer Data Platform (CDP) als isolierte Datenkapsel. Alle Verträge, Finanztransaktionen und Identitätsdaten werden auf lokalen Geräten und verschlüsselten Cloud-Instanzen gehalten — ohne Lock-in oder unkontrollierte Weitergabe.
2.  **PROTECTION LAYER (Privacy Guardian):**  
    Der Consent & Boundary Gatekeeper. Verhindert unberechtigte LLM-Zugriffe. boundaries-definierte Filter prüfen jeden API-Call auf Einhaltung der Datenschutzparameter.
3.  **CONTROL LAYER (Execution Center):**  
    Das HITL/HOTL-Steuerungsorgan. Bestimmt, wann Aktionen vollautomatisch ablaufen (Human-on-the-Loop) und wann zwingend eine Nutzerentscheidung erforderlich ist (Human-in-the-Loop).
4.  **TRUST LAYER (Audit Trail):**  
    Die Transparenz-Engine. Protokolliert jede Kündigung, jede Verhandlung und jeden API-Austausch revisionssicher in einem fälschungssicheren Ledger zur Einhaltung von EU AI Act & DSGVO.

---

### 2.3 Technologie-Stack

| Schicht | Technologie | Version / Stand 2026 |
| :--- | :--- | :--- |
| **Frontend** | Kotlin + Jetpack Compose | Kotlin 2.2 / Compose 1.11.x |
| **UI-Toolkit** | Material Design 3 | Material3 1.3.x |
| **State Management** | ViewModel + StateFlow | Lifecycle 2.8.x |
| **DI** | Hilt (Dagger) | 2.52 |
| **Networking** | Ktor Client | Ktor 3.x |
| **Local DB** | Room | 2.7.x |
| **Backend** | Cloud Run (Kotlin/Ktor) | europe-west1 |
| **Database** | Cloud Firestore | europe-west3 |
| **AI/LLM** | Gemini 2.5 Flash / Pro | Vertex AI Client |
| **Banking** | PSD2/XS2A Integration | finAPI / Tink |
| **Agent Payment** | Mastercard Agent Pay Framework | 2026 GA |

---

### 2.4 GCP-Projekt-Konfiguration

```
Project ID:          sovereign-mvp
Region (Compute):    europe-west1 (Belgien)
Region (Data):       europe-west3 (Frankfurt)
Billing Account:     DACH-Operations
Firebase Plan:       Blaze (Pay-as-you-go)
```
