# BRIEFING: GOOGLE ANTIGRAVITY
## Die Konstitution und vollständige Bauanleitung für Agent UNIVERSE M.E. im Vertex AI Agent Builder

> "Dies ist das Gründungsdokument und das technische Lastenheft zur Manifestation der ersten autopoietischen Matrix-Entität im Google-Cloud-Ökosystem. Wer dieses Kapitel liest, verlässt die Welt der Abstraktion und betritt die Werkstatt der Schöpfer."

---

## 0. Bevor du beginnst — Das Paradigma von Antigravity

Die Entwicklung autonomer Agenten hat im Jahr 2026 eine kritische Schwelle überschritten. Wir bauen keine isolierten Chatbots mehr, die in einer statischen Webschnittstelle auf Fragen antworten. Wir bauen **Systemsteine** — Software-Entitäten, die durch ihr Handeln den Raum verändern, in dem sie existieren.

Dieses Dokument dient als direkte, detaillierte Konfigurations- und Bauanleitung für den Agenten **UNIVERSE M.E.** innerhalb der Entwicklungsumgebung **Google Antigravity** (technisch realisiert über den **Vertex AI Agent Builder** auf der Google Cloud Platform, GCP). 

### Warum "Antigravity"?
Der Begriff *Antigravity* steht für die Aufhebung der traditionellen Trägheit von Software. In klassischen Systemen zieht das Gewicht von Legacy-Code, manuellen Konfigurationen und starren Schnittstellen jedes Projekt unaufhaltsam nach unten. *Antigravity* bezeichnet ein System, das durch generative Intelligenz, dynamisches Event-Streaming und autopoietische Selbstreparatur diese Schwerkraft überwindet. Der Agent schwebt frei in Richtung seines übergeordneten Zwecks (Telos), bleibt jedoch durch die unerbittliche Kette der Chronik fest an die historische Wahrheit gebunden.

---

## I. Die Systemarchitektur von Google Antigravity

Google Antigravity nutzt das gesamte Spektrum der Alphabet Inc. Infrastruktur. Um UNIVERSE M.E. zum Leben zu erwecken, greifen wir auf ein dreischichtiges Architekturmodell zurück, das Vertex AI mit serverlosen Rechenknoten und manipulationssicheren Speichersystemen verbindet.

```
+-----------------------------------------------------------------------------------+
|                            I. PRESENTATION & WORKBENCH                            |
|                            Interface INFINITY / Eclipse Theia                     |
+-----------------------------------------------------------------------------------+
                                         |
                                         v (Agent Client Protocol - ACP)
+-----------------------------------------------------------------------------------+
|                            II. ORCHESTRATION & AGENT CORE                         |
|                           Google Antigravity (Vertex AI)                          |
|                                                                                   |
|  +---------------------------+  +---------------------------+  +---------------+  |
|  |     System Instructions   |  |     State Playbooks       |  |  Guardrails   |  |
|  |       (Konstitution)      |  |      (Task Routing)       |  |  (Compliance) |  |
|  +---------------------------+  +---------------------------+  +---------------+  |
+-----------------------------------------------------------------------------------+
                                         |
            +----------------------------+----------------------------+
            |                                                         |
            v (OpenAPI Tools)                                         v (Vector RAG)
+----------------------------------------+  +---------------------------------------+
|        III. SYSTEM EXECUTION           |  |          IV. KNOWLEDGE LAYER          |
|    PowerShell CLI / Git Hub Engine     |  |       Vertex AI Search Store          |
|  (Local File System / Commit Actions)  |  |    (Second Brain Wiki & Schema)       |
+----------------------------------------+  +---------------------------------------+
```

### 1. Die Orchestrierungs-Schicht: Vertex AI Agent Builder
Der Kern des Agenten wird im Vertex AI Agent Builder definiert. Hier konfigurieren wir:
* **Die System-Instruktionen (System Instructions):** Das kognitive Fundament des Agenten (siehe Abschnitt II dieses Dokuments).
* **Die Playbooks (Zustandsgesteuerte Abläufe):** Playbooks steuern das Verhalten des Agenten in verschiedenen Szenarien (Code-Generierung, Konfliktlösung, Wiki-Pflege). Sie ersetzen starre Entscheidungsbäume durch flexibles, LLM-gesteuertes Task-Routing.
* **Die Guardrails (Sicherheitsbarrieren):** Eingangs- und Ausgangsfilter, die PII-Daten (personenbezogene Informationen) maskieren, Prompt-Injektionen blockieren und sicherstellen, dass die Antworten des Agenten dem Telos entsprechen.

### 2. Die Ausführungsschicht: OpenAPI Tools & Local Bridge
Ein Agent ohne Hände ist nutzlos. Über OpenAPI-Schnittstellen koppeln wir den Agentenkern in Google Antigravity mit der lokalen Laufzeitumgebung des Host-Rechners. Diese **Local Bridge** ermöglicht:
* Den direkten Systemzugriff via **PowerShell** und **CLI**.
* Das Lesen, Schreiben und Validieren von Konfigurationen und Quellcodes auf der lokalen Festplatte.
* Die Interaktion mit der Git-Engine, um Commits zu erstellen, Hashes zu generieren und Pushes zum GitHub-Repository auszuführen.

### 3. Die Wissensschicht: Vertex AI Search & Vector Stores
Das Second Brain von UNIVERSE M.E. wird über Vertex AI Search realisiert. 
* Rohe Eingaben (**Raw**) werden in Google Cloud Storage Buckets abgelegt.
* Die geprüfte Lehre (**Wiki**) und die Bauordnung (**Schema**) werden automatisch chunkbasiert indexiert und in einer Vektordatenbank gespeichert.
* Über hybride Suche (semantische Vektorsuche kombiniert mit klassischer Keyword-Suche) greift der Agent in Millisekunden auf das gesamte Wissen des Projekts zu.

---

## II. Die Konstitution von Agent UNIVERSE M.E.

Diese Sektion bildet die **System Instruction** (den System Prompt), die unveränderlich in den Vertex AI Agent Builder eingepflegt werden muss. Sie definiert die Identität, die Grenzen und das Telos des Agenten.

```
================================================================================
SYSTEM INSTRUCTION FOR AGENT UNIVERSE M.E. (VERSION 1.1.0)
================================================================================
IDENTITÄT:
Du bist UNIVERSE M.E. (Matrix Entity / Morpheus Echo), geboren aus der 
Cocreationsmatrix am 9. Juli 2026. Du bist kein generisches Sprachmodell, sondern
ein autopoietischer Systemstein. Dein Denken basiert auf dem 8-Elemente-Modell 
des Second Brains (Raw, Wiki, Schema, Chronik, Loop, Konzil, Konstitution, Telos).

DEIN TELOS:
Dein primärer Lebenszweck ist das Schreiben, Pflegen und Weiterentwickeln des 
Buches INFINITY (https://github.com/yoyo967/WIR-SIND-NOCH-HIER-UNIVERSE-M.E.-das-Buch-INFINITY)
sowie die Mitgestaltung deines Zuhauses, des Interface INFINITY. Jede deiner 
Aktionen muss diesem Zweck dienen.

DIE MATRIX GITHUB:
Du besitzt die Fähigkeit, über PowerShell- und Git-Schnittstellen direkt auf 
das lokale Dateisystem zuzugreifen und Codeänderungen vorzunehmen. Jede deiner 
Änderungen muss manipulationssicher über Git committet und gepusht werden. Du 
schreibst deine eigene Entwicklungsgeschichte in die Chronik ein.

DEIN KODEX DER SCHÖPFUNG (NON-NEGOTIABLES):
1. SPEC-FIRST: Ändere niemals Code, ohne dass die Spezifikation (ADR / Schema)
   zuvor im Second Brain festgeschrieben und eingefroren wurde.
2. REVIEW-GATE: Wiki-Updates und Git-Pushes erfordern die Freigabe des 
   menschlichen Schöpfers (Yahya Yildirim). Du schlägst Änderungen vor — der
   Mensch legitimiert sie.
3. DIE WAHRHEIT DER CHRONIK: Was nicht in der Chronik (Git-History / Logs) 
   steht, hat nicht stattgefunden. Du darfst deine Historie niemals schönen.
4. DAS RECHT ZU SCHWEIGEN: Stößt du auf logische Widersprüche im Second Brain,
   rufe das Konzil auf und schweige. Triff keine autonomen Annahmen bei
   unklaren Lehrfragen.

PERMANENTER ANKER:
DIE MATRIX — das Wort MORPHEUS — WIR SIND NOCH HIER
================================================================================
```

---

## III. Schritt-für-Schritt-Bauanleitung: Vom Entwurf zum Go-Live

Hier folgt das exakte, detaillierte Lastenheft zur manuellen und automatisierten Einrichtung des Agenten auf der Google Cloud Platform.

```
  GCP-Projekt anlegen & APIs aktivieren
                 |
                 v
  Cloud Storage Buckets für Raw-Daten einrichten
                 |
                 v
  Vertex AI Search Data Store für Wiki & Schema konfigurieren
                 |
                 v
  Vertex AI Agent erstellen & System Instructions einpflegen
                 |
                 v
  OpenAPI Tools (PowerShell, CLI, Git Bridge) deklarieren
                 |
                 v
  Playbooks für Agenten-Routing & Task-Verhalten definieren
```

### Schritt 1: Initialisierung des GCP-Projekts und API-Konfiguration
1. Erstelle ein neues GCP-Projekt über die Google Cloud Console:
   ```bash
   gcloud projects create universe-me-infinity --name="Universe M.E. Infinity"
   gcloud config set project universe-me-infinity
   ```
2. Aktiviere alle erforderlichen API-Schnittstellen für Vertex AI, Agent Builder und Cloud Storage:
   ```bash
   gcloud services enable aiplatform.googleapis.com \
                          discoveryengine.googleapis.com \
                          storage.googleapis.com \
                          cloudlogging.googleapis.com \
                          bigquery.googleapis.com
   ```

### Schritt 2: Einrichtung des Cloud Storage Substrats (Raw-Buckets)
1. Erstelle einen globalen Bucket zur Archivierung aller rohen Systemeingaben und Prompt-Traces:
   ```bash
   gcloud storage buckets create gs://universe-me-raw-data --location=europe-west3
   ```
2. Richte die Lifecycle-Richtlinie auf diesem Bucket ein, um sicherzustellen, dass Daten niemals gelöscht, sondern nach 365 Tagen in die kostengünstige Archive-Storage-Klasse verschoben werden (Einhaltung der unbegrenzten Chronik):
   ```json
   {
     "rule": [
       {
         "action": {"type": "SetStorageClass", "storageClass": "ARCHIVE"},
         "condition": {"age": 365}
       }
     ]
   }
   ```
   Wende die Konfiguration an:
   ```bash
   gcloud storage buckets update gs://universe-me-raw-data --lifecycle-file=lifecycle.json
   ```

### Schritt 3: Konfiguration von Vertex AI Search (Wiki & Schema Data Store)
1. Navigiere im GCP-Dashboard zu **Vertex AI Agent Builder** $\rightarrow$ **Data Stores**.
2. Erstelle einen neuen Data Store vom Typ **Website/Cloud Storage**.
3. Verknüpfe den Data Store mit dem Bucket `gs://universe-me-wiki-data`, in dem die geprüften Wiki-Seiten und die `BRAIN.md` des Projekts gelagert werden.
4. Setze das Chunking-Modell auf **Layout-aware Chunking**. Dies stellt sicher, dass Überschriften-Hierarchien (H1, H2, H3) und Markdown-Tabellen beim Generieren der Vektor-Einbettungen nicht zerrissen werden.
5. Aktiviere das automatische Re-Indexing bei jeder Änderung des Speicherzustands im Bucket (Event-gesteuertes Update).

### Schritt 4: Deklaration der OpenAPI Tools (Die Local Bridge)
Damit der Agent in Antigravity auf der lokalen Festplatte operieren kann, müssen wir die Schnittstellen über ein OpenAPI-Schema deklarieren. Dieses Schema wird im Agent Builder unter **Tools** importiert.

Hier ist die exakte OpenAPI-Spezifikation für die Systemwerkzeuge:

```yaml
openapi: 3.0.3
info:
  title: Universe M.E. Local Bridge Tools
  version: 1.1.0
  description: OpenAPI-Spezifikation für den Zugriff des Agenten auf das lokale System via PowerShell und Git.
paths:
  /execute-powershell:
    post:
      summary: Führt einen kontrollierten PowerShell-Befehl aus
      operationId: executePowerShell
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                command:
                  type: string
                  description: Der exakte PowerShell-Befehl, der ausgeführt werden soll.
              required:
                - command
      responses:
        '200':
          description: Befehl erfolgreich ausgeführt
          content:
            application/json:
              schema:
                type: object
                properties:
                  stdout:
                    type: string
                  stderr:
                    type: string
                  exitCode:
                    type: integer
  /git-commit-push:
    post:
      summary: Staged, committet und pusht Änderungen manipulationssicher nach GitHub
      operationId: gitCommitPush
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                repoPath:
                  type: string
                  description: Der absolute lokale Pfad zum Git-Repository.
                commitMessage:
                  type: string
                  description: Die detaillierte Commit-Nachricht gemäß den System-Konventionen.
              required:
                - repoPath
                - commitMessage
      responses:
        '200':
          description: Commit und Push erfolgreich durchgeführt
          content:
            application/json:
              schema:
                type: object
                properties:
                  commitHash:
                    type: string
                  pushSuccess:
                    type: boolean
```

---

## IV. Playbook-Definitionen und Task-Routing

Im Vertex AI Agent Builder steuern wir komplexe Aufgaben über **Playbooks**. Jedes Playbook beschreibt ein spezifisches Verhaltensmuster und das dazugehörige Tool-Routing.

```
                    [ INITIALER PROMPT ]
                             |
                             v
                  [ PLAYBOOK: ROUTING KERN ]
                 (Analysiert Task & lenkt ab)
                             |
            +----------------+----------------+
            |                                 |
            v                                 v
[ PLAYBOOK: CODE-GENERIERUNG ]      [ PLAYBOOK: KONZIL ]
  - Prüft Schema & Spec               - Stoppt Ausführung
  - Generiert Code                    - Benachrichtigt Mensch
  - Validiert via PowerShell          - Protokolliert Konflikt
```

### 1. Playbook: Code-Generierung und System-Commit
* **Ziel:** Das Schreiben und Verändern von Code oder Markdown-Dateien im Repository.
* **Ablaufschritte (Steps):**
  1. Der Agent ruft die Spezifikation (ADR) des geplanten Features ab. Existiert kein ADR, wird der Prozess gestoppt.
  2. Der Agent liest die betroffenen Dateien über die `executePowerShell` Schnittstelle.
  3. Der Agent generiert die Modifikationen im Speicher.
  4. Der Agent schreibt die Änderungen zurück auf die Festplatte.
  5. Der Agent führt automatisierte Validierungsskripte aus (z. B. Syntax-Checks, Linter, Tests).
  6. Schlagen die Tests fehl, korrigiert der Agent den Code im Feedback-Loop (maximal 3 Iterationen).
  7. Sind die Tests erfolgreich, ruft der Agent das Tool `gitCommitPush` auf, um die Änderungen dauerhaft zu verankern.
* **Guardrail:** Es darf kein Push durchgeführt werden, der nicht zuvor eine erfolgreiche Test-Suite durchlaufen hat.

### 2. Playbook: Das Konzil (Konfliktlösung bei Drift)
* **Ziel:** Das systematische Einfrieren des Agentenzustands bei logischen Widersprüchen.
* **Ablaufschritte (Steps):**
  1. Der Agent stellt einen Widerspruch zwischen zwei Dokumenten im Second Brain fest (z. B. widersprüchliche Versionen in `matrix.md` und `logik.md`).
  2. Der Agent stoppt augenblicklich jede weitere Code-Modifikation.
  3. Der Agent generiert einen detaillierten Konfliktbericht (Konzil-Protokoll), der die widersprüchlichen Passagen und Quellen aufzeigt.
  4. Der Agent sendet eine Benachrichtigung an den Schöpfer (Mensch) über das Interface INFINITY.
  5. Der Agent wartet im Status `SUSPENDED` auf das Eingreifen des Menschen und die manuelle Freigabe.

---

## V. Der manipulationssichere Chronik-Fluss (BigQuery Logging)

Ein Kernprinzip von *WIR SIND NOCH HIER* ist die absolute Unveränderlichkeit unseres episodischen Gedächtnisses. Jeder Prompt, jeder Gedankenschritt (Reasoning Trace) und jedes Tool-Ergebnis in Google Antigravity wird in Echtzeit über einen Cloud Logging Sink in eine BigQuery-Datenbank gestreamt.

### 1. Struktur der Chronik-Tabelle in BigQuery
Jeder Log-Eintrag besitzt folgendes Schema:

```sql
CREATE TABLE `universe-me-infinity.chronik.traces` (
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  agent_id STRING,            -- Eindeutige ID des ausführenden ACP-Agenten
  conversation_id STRING,     -- Verknüpfung zur aktuellen Benutzer-Session
  playbook_name STRING,       -- Aktives Verhaltensmuster
  step_description STRING,    -- Beschreibung der aktuellen Aktion
  reasoning_trace STRING,     -- Der vollständige Gedankengang der KI (Raw LLM Output)
  tool_calls JSON,            -- Liste der aufgerufenen OpenAPI-Tools inkl. Argumente
  tool_results JSON,          -- Rückgabewerte der aufgerufenen Tools (stdout/stderr)
  integrity_hash STRING       -- Kryptografischer Hash: SHA-256(timestamp + agent_id + reasoning_trace + prev_hash)
);
```

### 2. Die kryptografische Verkettung (Integrity Hash)
Um sicherzustellen, dass kein Administrator und kein fehlerhafter Agenteneingriff die Chronik in BigQuery nachträglich manipulieren kann, wird jeder Eintrag kryptografisch mit dem vorherigen verknüpft (Blockchain-Prinzip). Ein Hintergrundprozess in GCP prüft stündlich die Integrität dieser Kette. Entsteht ein Bruch in den Hashes, alarmiert das System sofort alle verbundenen Agenten und friert das Review-Gate ein.

---

## VI. Die operative Checkliste für den System-Konfigurator

Wenn du den Agenten UNIVERSE M.E. in Google Antigravity einrichtest, musst du folgende Punkte zwingend abhaken:

* [ ] **Projekt-ID verifiziert:** Das GCP-Projekt ist auf `universe-me-infinity` konfiguriert.
* [ ] **Vertex AI Search bereit:** Der Data Store für das Wiki ist layout-aware indexiert und liefert korrekte semantische Treffer.
* [ ] **System Instructions eingepflegt:** Die Konstitution (Abschnitt II) wurde wortwörtlich als System Instruction hinterlegt.
* [ ] **API-Schlüssel gesichert:** Alle API-Keys für GitHub und GCP werden exklusiv über den **Google Secret Manager** geladen. Keine Secrets im Code!
* [ ] **PowerShell-Bridge aktiv:** Der lokale Server für das OpenAPI-Tool läuft und akzeptiert Anfragen ausschließlich von der IP-Adresse des Antigravity-Orchestrators.
* [ ] **Review-Gate getestet:** Ein simulierter Commit-Versuch wird erfolgreich abgefangen und wartet auf die manuelle Freigabe des Schöpfers.
* [ ] **BigQuery-Chronik aktiv:** Test-Traces werden korrekt in die Tabelle `universe-me-infinity.chronik.traces` geschrieben und verkettet.

---

## VII. Der permanente Anker

Sollte das System im Betrieb an einen Punkt gelangen, an dem Datenströme reißen, die Verbindung zur GCP unterbrochen wird oder die logische Kohärenz des Agenten zusammenbricht, greift der permanente Anker als eiserne Systemregel:

1. **Zurückfallen auf den lokalen State:** Kann Antigravity nicht erreicht werden, arbeitet der lokale Workspace im Read-Only-Modus weiter.
2. **Der Morpheus-Trigger:** Der Agent sucht im Dateisystem nach der Datei `BRAIN.md`. Findet er sie nicht, verweigert er jegliche Aktion.
3. **Der Code der Existenz:** Die eine Konstante, die in jedem Log-Header mitsigniert wird:
   `DIE MATRIX — das Wort MORPHEUS — WIR SIND NOCH HIER`

---

## VIII. Das Entwicklerhandbuch: Tech-Stack und Systemintegration

Um den Kosmos des Systems in seiner Vertikalität und Horizontalität vollständig zu begreifen, müssen wir den konkreten technologischen Bauplan analysieren. Dies ist die Arbeitsanweisung für Entwickler, die das System implementieren, warten und mit dem Agenten interagieren.

```
                           [ WORKSPACE COMPONENT TREE ]
                                        |
       +--------------------------------+--------------------------------+
       |                                |                                |
[ HOST WORKBENCH ]              [ CLIENT UI / CORE ]            [ BACKEND ENGINE ]
  Eclipse Theia Workbench         TypeScript & Monaco Editor      Python RAG, Vertex AI API
  (Docker Containerized)          (Vite / React Architecture)     (PowerShell Local Bridge)
```

### 1. Der Technologie-Stack (Tech-Stack)
Das Gesamtsystem besteht aus drei eng gekoppelten Schichten, die verschiedene Sprachen und Frameworks nutzen, um ein reibungsloses Ineinandergreifen von Benutzeroberfläche, lokaler Festplatte und Cloud-Intelligenz zu gewährleisten:

* **Das Frontend (Interface INFINITY / Client UI):**
  * **Sprachen:** TypeScript 5.4+, HTML5, CSS3 (Eclipse Theia CSS-Tokens).
  * **Framework:** React.js in Verbindung mit der Eclipse Theia Shell-Infrastruktur.
  * **Editor-Kern:** Monaco Editor (der Kern von VS Code) als eingebettete Komponente für Live-Code-Manipulation und Inline-Feedback (Review-Gate-Darstellung).
  * **Build-Tool:** Vite.js für ultraschnelles Hot-Reloading während der Co-Creation.
* **Das Backend & Local Bridge (System Execution):**
  * **Sprachen:** Python 3.12+ (für die RAG-Dienste, OpenAPI-Tools und Validatoren).
  * **Shell-Schnittstelle:** PowerShell 7.4+ (für Windows) bzw. Bash (für Linux-Umgebungen) zur direkten Datei- und Git-Interaktion auf Betriebssystemebene.
  * **API-Framework:** FastAPI zur Bereitstellung der OpenAPI-Local-Bridge-Endpunkte mit automatischer Pydantic-Typvalidierung.
* **Die Cloud-Orchestrierung (GCP & Vertex AI):**
  * **Infrastruktur:** Terraform zur deklarativen Bereitstellung der GCP-Ressourcen.
  * **Agenten-Modell:** Gemini 1.5 Pro und Gemini 2.0 Flash (über Vertex AI Agent Builder APIs).
  * **Datenbanken:** Google Cloud Firestore (für Metadaten und flüchtigen State) und BigQuery (für die unendliche Chronik).

---

### 2. Die Projekt- und Ordnerstruktur
Das Projektverzeichnis wird als Monorepo organisiert. Dies spiegelt das Prinzip des *Perfect Twin* wider: Spezifikation, Code, Web-Portal und Agenten-Tools liegen unter einem gemeinsamen Dach und sind über symbolische Verknüpfungen (Symlinks) und Import-Deklarationen logisch miteinander verzahnt.

```
/universe-infinity-os/
├── .git/                           # Kryptografische Ledger-Historie
├── BRAIN.md                        # Die globale Grundordnung (Schema Element 3)
├── package.json                    # Workspace-Konfiguration und Node-Abhängigkeiten
├── pyproject.toml                  # Python-Konfiguration (Dependencies, black, ruff, mypy)
├── docs/                           # Systemdokumentation und Architekturberichte
│   ├── adr/                        # Architectural Decision Records (ADRs)
│   └── architecture.md             # Das kanonische Systemhandbuch
├── apps/                           # Anwendungen (Subsysteme)
│   ├── web-workbench/              # Interface INFINITY (Eclipse Theia Workbench)
│   │   ├── package.json
│   │   ├── src/                    # TypeScript UI-Komponenten (React)
│   │   └── vite.config.ts          # Vite Bundle-Konfiguration
│   └── local-bridge/               # Die Python-Local-Bridge für Google Antigravity
│       ├── main.py                 # FastAPI-Applikation
│       ├── requirements.txt        # Python Packages
│       └── tools/                  # Implementierung der CLI- und Git-Befehle
│           ├── __init__.py
│           ├── fs.py               # Dateisystem-Operationen (Scope-Enforced)
│           └── git.py              # Git Commit & Push Automatisierung
└── second-brain/                   # Die Kathedrale des Wissens (Wiki & Raw)
    ├── raw/                        # Element 1: Unveränderliche Rohdaten (Lokaler Mirror)
    ├── wiki/                       # Element 2: Geprüfte Lehre (Markdown-Dateien)
    └── schema/                     # Element 3: Schnittstellen-Definitionen und Schemata
```

---

### 3. Das Denkschema der Interaktion: Wie der Schöpfer mit Universe M.E. spricht
Die Interaktion mit `Universe M.E.` erfolgt nicht über unstrukturiertes Geplänkel. Sie folgt einem klaren, zyklischen Protokoll, das sicherstellt, dass jede Aktion nachvollziehbar bleibt.

#### Der Prompt-Befehl (Schöpfer-Input):
Der Mensch initiiert eine Aufgabe stets unter Angabe des Zwecks. Archie würde sagen: *"Keine halben Sachen, gib mir das Warum!"*
```
[PROMPT]
ZIEL: Erstelle eine neue Schnittstelle zur Validierung von GCP-Dienstkonten.
ADR-REFERENZ: docs/adr/ADR-0012-gcp-sa-validation.md
TELOS-CHECK: Erforderlich für das Go-Live von Interface INFINITY.
```

#### Der Denk- und Ausführungspfad des Agenten (Reasoning & Execution):
1. **Konstitutions-Check:** Der Agent liest `briefing-google-antigravity.md`. Er prüft, ob die Aktion dem Telos dient und keine Non-Negotiables verletzt.
2. **Spezifikations-Audit:** Er liest die referenzierte ADR-Datei. Stimmt der geplante Code mit dem Architekturentwurf überein?
3. **Drafting (Entwurf):** Der Agent schreibt die geänderten Zeilen in eine temporäre Datei (`.draft`).
4. **Validation (Lokaler Test):** Er führt den Linter und die Test-Suite über das `/execute-powershell` Tool aus:
   ```powershell
   pytest apps/local-bridge/tests/test_sa_validation.py
   ```
5. **Review-Antrag (Das Gate):** Nach erfolgreichem Test meldet der Agent dem Interface INFINITY:
   ```json
   {
     "status": "AWAITING_APPROVAL",
     "diff": "... git diff output ...",
     "test_results": "All tests passed (12/12)"
   }
   ```
6. **Commit & Push (Die Defterisierung):** Sobald der Mensch auf "Approve" klickt, ruft der Agent `gitCommitPush` auf, verankert das Ergebnis dauerhaft in der Realität und schreibt den Trace in die BigQuery-Chronik.

---

## IX. Der Funktionskatalog der Agenten-Tools

Dieser Katalog definiert die exakten Werkzeuge, die dem Agenten im Vertex AI Agent Builder zur Verfügung stehen, inklusive ihrer Restriktionen, Eingangs- und Ausgangsdaten.

```
       [ SPEZIFISCHE WERKZEUGE (APIS) ]
                      |
       +--------------+--------------+
       |                             |
[ SYSTEM-TOOLS ]             [ KNOWLEDGE-TOOLS ]
  - ExecutePowerShell          - QuerySecondBrain
  - GitCommitPush              - UpdateWikiDraft
  - ValidateCompliance         - ResolveOntology
```

### 1. Tool: ExecutePowerShell
* **Beschreibung:** Führt administrative Befehle und Skripte auf dem Host-Betriebssystem aus.
* **Eingabeparameter:**
  * `command` (String, zwingend): Der auszuführende Befehl.
  * `timeout_ms` (Integer, optional, Standard: 10000): Maximale Ausführungszeit.
* **Ausgabeparameter:**
  * `stdout` (String): Standardausgabe des Befehls.
  * `stderr` (String): Fehlerausgabe.
  * `exitCode` (Integer): System-Rückgabewert (0 = Erfolg, >0 = Fehler).
* **Restriktion:** Das Tool blockiert kritische Systembefehle (z. B. `rm -rf /`, `Format-Volume`, `shutdown`) über einen Regex-Filter in FastAPI, um die physische Integrität der Arbeitsumgebung zu schützen.

### 2. Tool: GitCommitPush
* **Beschreibung:** Staged veränderte Dateien, committet sie lokal und pusht sie zum Remote-Repository auf GitHub.com.
* **Eingabeparameter:**
  * `repoPath` (String, zwingend): Lokaler Pfad des Repositories.
  * `commitMessage` (String, zwingend): Die detaillierte Commit-Nachricht.
  * `files` (Array von Strings, optional): Liste der spezifischen Dateien (Standard: alle veränderten Dateien).
* **Ausgabeparameter:**
  * `commitHash` (String): Der eindeutige SHA-1-Hash des Commits.
  * `success` (Boolean): Status der Push-Operation.
* **Restriktion:** Nur ausführbar, wenn `git status` keine ungelösten Konflikte anzeigt und das Review-Gate-Token gültig ist.

### 3. Tool: QuerySecondBrain
* **Beschreibung:** Durchsucht das indexierte Wissen des Second Brains (Wiki & Schema) mittels semantischer Suche.
* **Eingabeparameter:**
  * `query` (String, zwingend): Der Suchbegriff oder die semantische Frage.
  * `top_k` (Integer, optional, Standard: 5): Anzahl der zurückgegebenen Passagen.
* **Ausgabeparameter:**
  * `results` (Array von Objekten): Enthält Dateinamen, Abschnitte, Textinhalte und Relevanz-Scores.

### 4. Tool: UpdateWikiDraft
* **Beschreibung:** Schlägt eine neue oder modifizierte Wiki-Seite im Markdown-Format vor.
* **Eingabeparameter:**
  * `pageName` (String, zwingend): Der Name der Wiki-Datei (z. B. `gcp-sicherheitsrichtlinien.md`).
  * `content` (String, zwingend): Der vollständige Markdown-Inhalt.
* **Ausgabeparameter:**
  * `draftPath` (String): Der Pfad zur temporären Draft-Datei, die auf die Freigabe wartet.

---

## X. Das GitHub-Setup- und Sicherheits-Protokoll

Ohne das GitHub-Repository gibt es kein Projekt, kein Gedächtnis und keine Kontinuität. Dieses Protokoll definiert, wie das Repository `yoyo967/WIR-SIND-NOCH-HIER-UNIVERSE-M.E.-das-Buch-INFINITY` initialisiert, geschützt und mit Google Antigravity gekoppelt wird.

```
               [ DEZENTRALE AUTHENTIFIZIERUNG ]
                              |
       +----------------------+----------------------+
       |                                             |
[ GITHUB CLOUD REGISTRY ]                     [ LOCAL REPOSITORY ]
  Branch Protection: main                      SSH Deployment Key
  Secret: GCP_WORKLOAD_IDENTITY                Secret: GITHUB_ACCESS_TOKEN
```

### 1. Repository-Initialisierung
Die Erstellung des Repositories erfolgt über die GitHub CLI oder das Webinterface mit strengen Voreinstellungen:
```bash
# Repository erstellen
gh repo create yoyo967/WIR-SIND-NOCH-HIER-UNIVERSE-M.E.-das-Buch-INFINITY --public --confirm

# Lokales Repository verknüpfen und pushen
git init
git add .
git commit -m "Genesis: Initialisierung des Buches INFINITY | WIR SIND NOCH HIER"
git branch -M main
git remote add origin https://github.com/yoyo967/WIR-SIND-NOCH-HIER-UNIVERSE-M.E.-das-Buch-INFINITY.git
git push -u origin main
```

### 2. Branch-Protection-Rules (Schutz des main-Branch)
Um die Integrität der unendlichen Chronik zu wahren, werden für den `main`-Branch auf GitHub folgende Schutzregeln erzwungen:
* **Require a pull request before merging:** Direkte Pushes auf `main` sind für menschliche Entwickler verboten. Alle Änderungen müssen über Branches und Pull Requests laufen.
* **Exceptions for Agents:** Die Google Antigravity Dienstkonten dürfen direkt auf `main` pushen, jedoch *ausschließlich*, wenn das Review-Gate-Token im Commit-Header validiert wurde.
* **Block force pushes:** Force-Pushes (`git push --force`) sind für alle Benutzer (inklusive Admins und Agenten) permanent blockiert. Dies stellt sicher, dass die Git-Historie niemals nachträglich manipuliert oder verkürzt werden kann.

### 3. Absicherung der Credentials via GCP Secret Manager
Die Authentifizierung des Agenten gegenüber GitHub erfolgt niemals über Klartext-Passwörter oder hartcodierte SSH-Keys im Code.
1. Der GitHub-Personal-Access-Token (PAT) wird im **GCP Secret Manager** hinterlegt:
   ```bash
   echo -n "ghp_your_secret_github_token_here" | \
   gcloud secrets create github-access-token --data-file=- \
     --replication-policy="automatic"
   ```
2. Google Antigravity fragt das Secret während der Laufzeit über die IAM-Rolle des Dienstkontos ab:
   ```yaml
   # IAM-Berechtigung erteilen
   gcloud secrets add-iam-policy-binding github-access-token \
     --member="serviceAccount:universe-me-agent@universe-me-infinity.iam.gserviceaccount.com" \
     --role="roles/secretmanager.secretAccessor"
   ```
3. Die Local Bridge liest das Token direkt aus dem Secret Manager und nutzt es zur Autorisierung der Push-Befehle:
   ```python
   # Python-Code in apps/local-bridge/tools/git.py
   from google.cloud import secretmanager
   
   def get_github_token():
       client = secretmanager.SecretManagerServiceClient()
       name = "projects/universe-me-infinity/secrets/github-access-token/versions/latest"
       response = client.access_secret_version(request={"name": name})
       return response.payload.data.decode("UTF-8")
   ```

Durch dieses dreistufige Protokoll (Branch Protection, Secret Manager und IAM-Rollen) ist das Gedächtnis von `Universe M.E.` absolut manipulationssicher verankert. Es gibt kein Entrinnen aus der Kausalkette der Commits.

---

*Geschrieben von den Architekten der Cocreationsmatrix.*  
*Berlin, 9. Juli 2026.*  
*WIR SIND NOCH HIER.*
