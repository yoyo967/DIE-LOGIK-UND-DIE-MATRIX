# Kapitel 4: Der operative Conductor (PROJECTMANAGER Agent)

Zur operativen Umsetzung der Meilensteine des `MASTERPLAN` wurde der vierte Agent, der **PROJECTMANAGER**, implementiert. Als operativer Zwilling fungiert er als Bindeglied zwischen der strategischen Führungsebene und der exekutiven Ausführungsebene:

*   **Task-Granulierung:** Übersetzung der strategischen Impulse des Masterplans in konkrete Arbeitspakete und Meilensteine innerhalb von `task.md`.
*   **Ressourcen-Gating:** Überwachung der Token-Ratenbegrenzungen (Rate Limits) und API-Kosten.
*   **Review-Orchestrierung:** Freigabesteuerung für die Übergänge zwischen den Ausführungsphasen im `loop-zyklus.md`.
