# 5. Backend-Architektur (GCP / Firebase)

### 5.1 Service-Übersicht

```
┌─────────────────────────────────────────────────────┐
│              SOVEREIGN BACKEND (GCP)                 │
├─────────────────────────────────────────────────────┤
│                                                      │
│  Cloud Run Services (europe-west1):                  │
│  ┌───────────────────────────────────────────────┐  │
│  │ sovereign-api          (Main API Gateway)      │  │
│  │ sovereign-orchestrator (Agent Brain)           │  │
│  │ sovereign-negotiator   (E-Mail Agent)          │  │
│  │ sovereign-switcher     (Provider Switching)    │  │
│  │ sovereign-claimer      (Flight Claims)         │  │
│  │ sovereign-billing      (Stripe Webhooks)       │  │
│  └───────────────────────────────────────────────┘  │
│                                                      │
│  Cloud Scheduler (Cron Jobs):                        │
│  ┌───────────────────────────────────────────────┐  │
│  │ scan-emails        (alle 6h)                   │  │
│  │ scan-bank-txns     (täglich 03:00)             │  │
│  │ check-contracts    (wöchentlich Mo 08:00)      │  │
│  │ check-flights      (alle 12h)                  │  │
│  │ billing-reconcile  (täglich 00:00)             │  │
│  └───────────────────────────────────────────────┘  │
│                                                      │
│  Firestore (europe-west3):                           │
│  ┌───────────────────────────────────────────────┐  │
│  │ users/                                         │  │
│  │ contracts/                                     │  │
│  │ agent_actions/                                 │  │
│  │ approvals/                                     │  │
│  │ savings/                                       │  │
│  │ claims/                                        │  │
│  │ billing_events/                                │  │
│  │ boundary_conditions/                           │  │
│  └───────────────────────────────────────────────┘  │
│                                                      │
│  Pub/Sub Topics:                                     │
│  ┌───────────────────────────────────────────────┐  │
│  │ agent-tasks          → Orchestrator            │  │
│  │ agent-results        → API / Billing           │  │
│  │ approval-requests    → FCM Push                │  │
│  │ billing-events       → Stripe Integration      │  │
│  └───────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────┘
```

---

### 5.2 API-Gateway (Cloud Run — Kotlin/Ktor)

```kotlin
// backend/sovereign-api/src/main/kotlin/com/sovereign/api/Application.kt
package com.sovereign.api

import io.ktor.server.application.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.server.routing.*
import io.ktor.server.auth.*
import io.ktor.server.plugins.contentnegotiation.*
import io.ktor.serialization.kotlinx.json.*
import com.sovereign.api.routes.*
import com.sovereign.api.plugins.*

fun main() {
    embeddedServer(Netty, port = 8080, host = "0.0.0.0") {
        configureAuth()           // Firebase Auth Verification
        configureSerialization()  // JSON
        configureRouting()
    }.start(wait = true)
}

fun Application.configureRouting() {
    routing {
        get("/health") { /* 200 OK */ }

        authenticate("firebase") {
            route("/api/v1") {
                get("/dashboard") { /* DashboardController */ }
                get("/savings/summary") { /* SavingsSummaryController */ }

                route("/contracts") {
                    get { /* ListContractsController */ }
                    get("/{id}") { /* GetContractController */ }
                }

                route("/approvals") {
                    get { /* ListPendingApprovalsController */ }
                    get("/{id}") { /* GetApprovalDetailController */ }
                    post("/{id}/approve") { /* ApproveActionController */ }
                    post("/{id}/reject") { /* RejectActionController */ }
                }

                route("/claims") {
                    get { /* ListClaimsController */ }
                    get("/{id}") { /* GetClaimController */ }
                }

                get("/actions") { /* ListAgentActionsController */ }

                route("/settings") {
                    get("/boundaries") { /* GetBoundaryConditionsController */ }
                    put("/boundaries") { /* UpdateBoundaryConditionsController */ }
                    get("/connected-accounts") { /* ListConnectedAccountsController */ }
                    post("/connected-accounts") { /* AddConnectedAccountController */ }
                    delete("/connected-accounts/{id}") { /* RemoveAccountController */ }
                }

                route("/onboarding") {
                    post("/connect-email") { /* ConnectEmailController (OAuth2) */ }
                    post("/connect-bank") { /* ConnectBankController (PSD2) */ }
                    post("/setup-payment") { /* SetupStripeController */ }
                }
            }
        }

        route("/webhooks") {
            post("/stripe") { /* StripeWebhookController */ }
            post("/agent-results") { /* AgentResultsController */ }
        }
    }
}
```

---

### 5.3 Firebase Auth Verification Middleware

```kotlin
// backend/sovereign-api/src/main/kotlin/com/sovereign/api/plugins/Auth.kt
package com.sovereign.api.plugins

import com.google.firebase.auth.FirebaseAuth
import io.ktor.server.application.*
import io.ktor.server.auth.*
import io.ktor.server.request.*
import io.ktor.http.*
import io.ktor.server.response.*

data class FirebaseUser(val uid: String, val email: String?)

fun Application.configureAuth() {
    install(Authentication) {
        bearer("firebase") {
            authenticate { tokenCredential ->
                try {
                    val decodedToken = FirebaseAuth.getInstance()
                        .verifyIdToken(tokenCredential.token)
                    FirebaseUser(
                        uid = decodedToken.uid,
                        email = decodedToken.email
                    )
                } catch (e: Exception) {
                    null
                }
            }
        }
    }
}
```
