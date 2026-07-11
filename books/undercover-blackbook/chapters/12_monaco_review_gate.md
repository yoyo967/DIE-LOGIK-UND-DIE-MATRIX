# Kapitel 11: Das Monaco-Review-Gate & Commit Gatekeeping

Die Schnittstelle für die menschliche Autorisierung von Codeänderungen und Systemzuständen bildet das **Monaco-Review-Gate** in der `opus-deck`-Workbench. Das Gating folgt dem Sledge-Hammer-Axiom: **\"Vertrauen Sie mir. Ich weiß, was ich tue.\"** 

Um die Latenz der autopoietischen Schleife zu minimieren und dem Architekten eine standortunabhängige Kontrolle zu ermöglichen, wird das Gating um eine mobile Push- und Remote-Control-Ebene erweitert.

---

## 1. Die Architektur des allgegenwärtigen Gatekeepings (FCM-Pipeline)

Traditionelle Commit-Prüfungen erfordern die physische Anwesenheit des Entwicklers am Arbeitsplatz. Dieses System löst diese Fessel auf, indem es eine asynchrone, mobile Autorisierungs-Pipeline implementiert:

```
            [ AUTOMATISIERTER INFERENZ- & COMPILER-LAUF ]
                                  |
                                  v
                    [ Gating: Commit Blocked ]
                                  |
                                  v
                   [ Google Cloud Function / FCM ]
                                  |
            +---------------------+---------------------+
            |                                           |
            v (Push-Signal)                             v (Zweites Signal)
    [ Smartphone des Architekten ]              [ Remote-Terminal (SSH) ]
  - Diffs & Test-Logs als JSON               - Telemetriedaten live
  - Freigabe via Biometrie (MFA)             - Eingriffs-Möglichkeit
```

1.  **Event Trigger:** Sobald ein Agenten-Konzil einen Task beendet und Code staged, blockiert `opus-flow` den Push-Prozess und triggert einen Webhook.
2.  **Firebase Cloud Messaging (FCM):** Google Cloud Functions serialisieren den Git-Diff, den Unit-Test-Report und die prognostizierten Token-Kosten in ein verschlüsseltes JSON-Payload und senden es via FCM als hochpriore Push-Nachricht an das registrierte Mobilgerät des Operators.
3.  **Mobile Payload Ingestion:** Die mobile Applikation decodiert die Payload lokal und bereitet die Diffs übersichtlich auf.

---

## 2. Der mobile Monaco-Diff-Editor und kryptografische Freigabe

Die Freigabe von Änderungen auf dem Smartphone erfolgt unter Einhaltung strengster Sicherheitsstandards:

*   **Responsive Monaco Diff:** Über einen abgesicherten, verschlüsselten Tunnel (WireGuard-VPN oder TLS-gesichertes WebSocket-Reverse-Proxy) rendert das Smartphone eine mobile-optimierte Ansicht des Monaco Diff Editors. Der Architekt kann Zeile für Zeile vergleichen und bei Bedarf Textkorrekturen direkt im Browser-Editor eingeben.
*   **Biometrische Multi-Faktor-Authentifizierung (MFA):** Um den Git-Commit-Push freizuschalten, muss sich der Architekt biometrisch (FaceID, TouchID oder WebAuthn) auf dem Mobilgerät authentifizieren.
*   **Kryptografische Signatur (GPG/SSH):** Nach erfolgreicher biometrischer Validierung signiert der lokale Schlüsselträger auf dem Smartphone (z. B. ein im Secure Enclave hinterlegter privater Schlüssel) den Commit kryptografisch. Das Freigabesignal wird an die API-Schnittstelle von `opus-flow` übermittelt, und der Git-Push wird auf dem Host-Server autorisiert ausgeführt.

---

## 3. Remote Control & Telemetrie-Streaming (TeamViewer & Remote Desktop)

Für tiefgreifende Diagnosen, manuelle Systemeingriffe oder die visuelle Überwachung des kognitiven Substrats im laufenden Betrieb stehen dezentrale Remote-Control-Protokolle bereit:

*   **Headless Remote Access:** Wenn der Architekt komplexe Debugging-Szenarien ausführen muss, ohne am Arbeitsplatz zu sitzen, kann er über **TeamViewer APIs** oder **Chrome Remote Desktop** eine verschlüsselte Verbindung zur Eclipse Theia Workbench (`opus-deck`) herstellen. Dies erlaubt das Ausführen von Terminals, das Rekalibrieren von Agenten-Gewichten und das direkte Einsehen der BigQuery-Ledger in Echtzeit.
*   **Notfall-Abschaltung (Algorithmic Apnoe):** Sollte der Architekt über sein Mobilgerät oder Remote-Verbindung unautorisierte Operationen oder kritische System-Drifts feststellen, reicht ein einziger SSH-Remote-Befehl, um die gesamte Inferenz-Engine auf dem Host-Server augenblicklich zu suspendieren und in den sicheren Offline-Zustand (Sarkophag-Zustand) zu versetzen.

*Die Integration von Remote-Control-Technologien macht das Monaco-Review-Gate zu einem allgegenwärtigen Kontrollorgan. Sie verbindet die Flexibilität des mobilen Zeitalters mit der unerbittlichen Sicherheit kryptografischer Git-Architekturen.*
