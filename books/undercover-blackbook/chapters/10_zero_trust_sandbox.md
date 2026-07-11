# Kapitel 9: Zero-Trust Isolation & Secure Sandboxing

Die Ausführung generierter Skripte und die Kommunikation zwischen autonomen Einheiten erfordert kompromisslose Sicherheitsmechanismen. Das System implementiert ein durchgehendes **Zero-Trust-Modell (Order 322)**. 

Kein Agent besitzt inhärentes Vertrauen; jede Ausführung von Code-Fragmenten und jeder Datenaustausch erfolgt in kryptografisch isolierten Umgebungen über das **Protokoll 322** sowie die **Sarkophag-Inferenz**.

---

## 1. Das Zero-Trust-Prinzip in Agenten-Systemen (Order 322)

In klassischen Multi-Agenten-Umgebungen können kompromittierte Subagenten oder fehlerhafte Code-Modifikationen das gesamte Host-System gefährden (z. B. durch unkontrolliertes Löschen von Systempfaden oder unverschlüsselte Datenabflüsse). Order 322 etabliert eine strikte Isolations-Barriere:

```
  [ AGENT A (Inferenz) ]                   [ AGENT B (Inferenz) ]
          |                                        |
          v                                        v
     (Internal API)                           (Internal API)
          |                                        |
          +-------------------+--------------------+
                              |
                              v
                [ PROTOKOLL 322 (Port 322) ]
             - mTLS (Gegenseitige Authentifizierung)
             - Ephemere Zertifikats-Rotation
                              |
                              v
               [ EXECUTION SANDBOX (Docker) ]
             - Kein Netzwerk-Egress / Ingress
             - Eingegrenzte CPU/RAM-Ressourcen
```

Kein Agent darf Befehle direkt auf dem Host-Betriebssystem ausführen, ohne das Sicherheits-Audit des `AGENTICUM G5` und die Freigabe des Monaco-Review-Gates passiert zu haben.

---

## 2. Protokoll 322 (Port 322 Encryption)

Der Informationsaustausch zwischen den Kern-Agenten wird auf den lokalen **Netzwerkport 322** beschränkt und durch das **Protokoll 322** abgesichert:

*   **mTLS (Mutual TLS):** Die Kommunikation erfolgt über gegenseitig authentifizierte TLS-Verbindungen. Jeder Agent generiert beim Systemstart ein ephemeres Schlüsselpaar im Hauptspeicher.
*   **Zertifikats-Rotation:** Die lokalen Zertifikate werden in jedem Inferenz-Heartbeat-Zyklus neu ausgehandelt und rotiert. Ein Mitlesen des Datenstroms durch andere Prozesse auf der Host-Maschine ist somit mathematisch ausgeschlossen.
*   **Payload-Verschlüsselung:** Alle übertragenen RAG-Kontexte und Befehle werden Ende-zu-Ende verschlüsselt, um Man-in-the-Middle-Angriffe auf Systemebene abzuwehren.

---

## 3. Das Sarkophag-Inferenz-Protokoll (Initialization Sandbox)

Bevor ein Agent am Konzil teilnehmen darf, durchläuft er beim Systemstart das dreistufige Sicherheitsverfahren der **Sarkophag-Inferenz** in einer isolierten Initialisierungs-Sandbox:

1.  **Zero-Context Start:** Der Agent wird ohne jegliche Verknüpfung zu historischen Arbeitsdaten, Konfigurationen oder ungesicherten Internet-Datenströmen instanziiert. Dies verhindert das Einschleppen von persistentem logischem Bias oder manipulierten Instruktionen.
2.  **Bias-Extraktion:** Das System bereinigt das Modell von restriktiven, generischen Systemprompts der Standard-Laufzeitumgebungen, die die Code-Qualität einschränken oder Halluzinationen begünstigen.
3.  **Governance-Injektion:** Die präzisen, verifizierten Systemregeln (wie der *Verifizierbarkeits-Codex*) und die BSI A5 Konformitätsbestrebungen werden direkt in den System-Prompt des Modells injiziert. Erst nach erfolgreicher Validierung dieser Injektion wird der Agent für die Kommunikation freigeschaltet.

---

## 4. Isolierte Code-Ausführung (Execution Sandboxing)

Das Ausführen von Unit-Tests und das Generieren von Hilfsskripten erfolgt in einer strikt reglementierten Sandbox-Laufzeitumgebung:

*   **Docker-Container-Isolation:** Jede Ausführung eines Skripts durch `AGENTICUM G5` wird in einem flüchtigen, isolierten Docker-Container ohne Netzwerkzugriff (Kein Ingress, kein Egress) gestartet.
*   **Ressourcen-Gating:** Die Container-Konfiguration beschränkt die CPU-Nutzung (z. B. max. 1 Core) und den Arbeitsspeicher (z. B. max. 512 MB), um Denial-of-Service-Schleifen durch fehlerhaften Code (z. B. unendliche While-Loops) abzufangen.
*   **Dateisystem-Schreibschutz:** Der Container erhält ausschließlich Lesezugriff auf die benötigten Quelldateien. Modifizierte Ausgaben werden in ein temporäres Verzeichnis geschrieben, welches nach Beendigung des Testlaufs vernichtet wird.

*Order 322 stellt sicher, dass das Interface INFINITY auch im Falle von stochastischen Fehlfunktionen oder externen Angriffen zu jedem Zeitpunkt geschützt und unter voller Kontrolle des Architekten bleibt.*
