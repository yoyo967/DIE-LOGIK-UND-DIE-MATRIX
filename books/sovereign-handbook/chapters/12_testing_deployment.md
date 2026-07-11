# 12. Testing & Deployment (CI/CD)

Ein stabiles und verlässliches Testsystem ist die wichtigste Voraussetzung für autarke Software-Systeme, die im echten Leben finanzielle Transaktionen ausführen. Sovereign setzt auf eine zweigleisige Verifizierungs- und Deployment-Pipeline.

---

## 12.1 Testing-Strategie

Die Testpyramide von Sovereign gliedert sich in drei Stufen:

### 1. Unit & Integration Tests (JUnit 5 & MockK)
*   **Business-Logik:** Alle Use Cases der App (z. B. `GetSavingsUseCase`) werden isoliert getestet.
*   **Room Database Testing:** Lokale Datenzugriffe (DAOs) werden auf In-Memory-Instanzen der Room-Datenbank simuliert.
*   **Ktor Mock Engine:** API-Aufrufe an das Backend werden über eine Mock-Engine simuliert, um Netzwerklatenz und -ausfälle auszuschließen.
*   *Beispiel-Test:*
    ```kotlin
    @Test
    fun `GetSavingsUseCase returns success resource on repository response`() = runTest {
        val mockRepo = mockk<SavingRepository>()
        coEvery { mockRepo.getSavings() } returns flowOf(Resource.Success(listOf(mockSaving)))
        val useCase = GetSavingsUseCase(mockRepo)
        
        useCase().collect { result ->
            assert(result is Resource.Success)
        }
    }
    ```

### 2. UI-Tests (Compose UI Test Rule)
*   Die Interaktion mit dem Dashboard und insbesondere die Geste `SwipeToApprove` werden mithilfe der Android Compose UI-Testbibliothek automatisiert verifiziert (Semantics Testing).

### 3. Agent Evals
*   Das System evaluiert Inferenz-Prompts kontinuierlich gegen eine Testsuite aus hypothetischen E-Mails, um sicherzustellen, dass keine semantischen Drifts (z. B. fehlerhafte Fristerkennungen nach einem Update des LLMs) auftreten.

---

## 12.2 Deployment & CI/CD-Pipeline (GitHub Actions)

Das Deployment erfolgt automatisiert über GitHub Actions für beide Plattformen.

### 1. Android-Build-Pipeline (`.github/workflows/android.yml`)
*   **Trigger:** Push auf `main` oder Pull Request in `main`.
*   **Schritte:**
    1.  Setup JDK 17.
    2.  Verifizierung der Code-Formatierung (ktlint).
    3.  Ausführen aller Unit-Tests (`./gradlew testDebugUnitTest`).
    4.  Kompilieren und Signieren der Release-APK unter Verwendung verschlüsselter GitHub Secrets für den Keystore.
    5.  Upload der signierten APK in die Google Play Console (Internal Sharing Lane).

### 2. Backend-Build-Pipeline (`.github/workflows/backend.yml`)
*   **Trigger:** Push im Verzeichnis `backend/`.
*   **Schritte:**
    1.  Authentifizierung bei der Google Cloud Platform (GCP).
    2.  Erstellung eines Docker-Containers über Cloud Build.
    3.  Upload des Containers in die Google Artifact Registry.
    4.  Deployment des Containers auf **GCP Cloud Run** (`sovereign-api` und Sub-Agent-Dienste) in der Region `europe-west1` mit minimalen Berechtigungen (IAM Service Accounts).
