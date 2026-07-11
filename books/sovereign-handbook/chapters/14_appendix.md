# 14. Anhang: API-Referenzen & Ressourcen

Der Anhang dokumentiert die wichtigsten Schnittstellenformate und Integrations-Endpunkte des Sovereign-Ökosystems.

---

## 14.1 API-Schnittstelle: Vertrags-Upload & Analyse

*   **Endpoint:** `POST /api/v1/contracts/analyze`
*   **Headers:**
    *   `Authorization: Bearer <Firebase_ID_Token>`
    *   `Content-Type: multipart/form-data`
*   **Request Body:**
    *   `file`: PDF-Dokument des Vertrags (max. 10 MB).
*   **Response Payload (200 OK):**
    ```json
    {
      "contractId": "ctr_893247923",
      "provider": "Vodafone Deutschland GmbH",
      "category": "DSL_INTERNET",
      "cost": {
        "monthlyValue": 39.99,
        "currency": "EUR"
      },
      "contractTerms": {
        "startDate": "2025-08-01",
        "noticePeriodDays": 30,
        "renewalPeriodMonths": 12,
        "nextPossibleTerminationDate": "2026-07-31"
      },
      "riskScore": 2,
      "detectedFallen": []
    }
    ```

---

## 14.2 API-Schnittstelle: Tink PSD2 Transaction Callback

*   **Endpoint:** `POST /webhooks/tink/transactions`
*   **Headers:**
    *   `X-Tink-Signature: sha256=kryptografischer_hash_wert_xxxxx`
    *   `Content-Type: application/json`
*   **Payload Example:**
    ```json
    {
      "accountId": "bank_acc_89324792",
      "userId": "usr_902348923",
      "transactions": [
        {
          "id": "txn_782347923",
          "amount": -39.99,
          "currency": "EUR",
          "bookingDate": "2026-07-10",
          "description": "VODAFONE GMBH SEPA-LASTSCHRIFT",
          "category": "UTILITIES"
        }
      ]
    }
    ```

---

## 14.3 Entwickler-Ressourcen & Support

*   **Entwickler-Portal (Nexus Hub):** `https://sovereign.de/de/nexus`
*   **API-Support & Integration:** `hello@sovereign.de`
*   **GitHub Repository:** `https://github.com/sovereign2030`
*   **Dokumentations-Lizenz:** CC-BY-SA 4.0 (Datensouveränitäts-Standard)

---

*WIR SIND NOCH HIER.*  
*SOVEREIGN DEVELOPER HANDBOOK V1.0 KOMPLETTIERT.*
