# 11. Datenmodell & Push-Notification-System

Die Datenhaltung von Sovereign ist hybrid aufgebaut: Lokale Cache-Daten liegen verschlüsselt in einer Room-Datenbank auf dem Android-Gerät des Nutzers, während der geteilte Systemstatus in Cloud Firestore synchronisiert wird.

---

## 11.1 Firestore-Datenschema

Firestore-Sammlungen (Collections) liegen in der Region `europe-west3` (Frankfurt, Deutschland).

### 1. `/users/{userId}` (Nutzerprofil)
```json
{
  "uid": "usr_902348923",
  "email": "user@sovereign.de",
  "createdAt": "2026-07-11T11:00:00Z",
  "subscriptionTier": "PRO",
  "connectedAccounts": {
    "bankConnected": true,
    "emailConnected": true
  }
}
```

### 2. `/users/{userId}/boundary_conditions/config` (Boundary Conditions)
```json
{
  "maxMonthlyBudgetElectricity": 120.0,
  "maxMonthlyBudgetGas": 150.0,
  "preferredProviders": ["e.on", "vattenfall"],
  "blockedProviders": ["shell_energy"],
  "autoApproveThresholdEuro": 10.0,
  "minSavingToTriggerSwitchEuro": 50.0
}
```

### 3. `/users/{userId}/contracts/{contractId}` (Vertragsdaten)
```json
{
  "id": "ctr_892347923",
  "provider": "Vodafone Deutschland GmbH",
  "type": "DSL",
  "monthlyCost": 39.99,
  "contractStart": "2025-08-01",
  "noticePeriodMonths": 1,
  "nextRenewalDate": "2026-08-01",
  "status": "ACTIVE"
}
```

### 4. `/users/{userId}/approvals/{approvalId}` (Human-in-the-Loop Freigaben)
```json
{
  "id": "appr_7893247923",
  "title": "Strom-Anbieterwechsel freigeben",
  "description": "Wechsel von Vattenfall zu E.ON Strom. Ersparnis: 180 €/Jahr.",
  "status": "PENDING",
  "agentType": "SWITCHING_NODE",
  "targetContractId": "ctr_98234792",
  "proposedContractDelta": {
    "newProvider": "E.ON Energie",
    "newCost": 65.00,
    "savingsFirstYear": 180.00
  },
  "createdTimestamp": "2026-07-11T11:15:00Z"
}
```

---

## 11.2 Push-Notification-System (Firebase Cloud Messaging)

Das Push-Notification-System informiert den Nutzer in Echtzeit über ausstehende Aktionen. Um Latenzen zu minimieren, wird das Payload-Format standardisiert.

### FCM JSON Payload (High-Priority):
```json
{
  "message": {
    "token": "android_device_registration_token_xxxxx",
    "android": {
      "priority": "HIGH",
      "ttl": "86400s",
      "notification": {
        "title": "Freigabe erforderlich",
        "body": "Sovereign hat eine Ersparnis von 180 € gefunden. Jetzt freigeben.",
        "icon": "ic_sovereign_logo",
        "color": "#00D4AA"
      }
    },
    "data": {
      "click_action": "FLUTTER_NOTIFICATION_CLICK",
      "type": "PENDING_APPROVAL",
      "approvalId": "appr_7893247923",
      "timestamp": "2026-07-11T11:15:05Z"
    }
  }
}
```

Auf dem Endgerät parst der `SovereignFirebaseMessagingService` die `data`-Payload und navigiert den Nutzer nach Klick direkt auf den `ApprovalDetailScreen` des Navigations-Graphen.
