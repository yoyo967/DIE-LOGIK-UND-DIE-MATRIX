# Kapitel 8: Global Swarm Observability (EYE OF GOD Telemetry)

Das allsehende Überwachungs- und Diagnoseorgan des Monorepos ist der fünfte Agent: **EYE OF GOD**. Er erzwingt die globale Observability des verteilten Systems:

*   **Dateisystem-Audits:** Überwachung jeglicher Drifts und unerlaubter Änderungen innerhalb der lokalen Sandbox (`FLOW_ROOT`).
*   **Agenten-Fabrik:** Autonome Instanziierung und Kompilierung von temporären Subagenten zur Bewältigung komplexer Review-Tasks. Nach der Validierung des Tasks werden diese Agenten rückstandslos deprovisioniert.
