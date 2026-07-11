# Kapitel 11: Das Monaco-Review-Gate & Commit Gatekeeping

Die Schnittstelle für die menschliche Autorisierung von Codeänderungen bildet das **Monaco-Review-Gate** in `opus-deck`. Das Gating folgt dem Sledge-Hammer-Axiom: **\"Vertrauen Sie mir. Ich weiß, was ich tue.\"**

```
          [ MONACO-REVIEW-GATE: COMMIT-GATEKEEPING ]
                                 |
         Der Architekt (Freigabe über Monaco-Editor UI)
                                 |
           (Rotes Telefon: Autorisierung des Commits)
                                 |
            GCP / GitHub (Schnittstelle zur Git-Push-Pipeline)
```

Sobald der Architekt den Diff-Vergleich im Monaco-Editor verifiziert, sendet die Theia-Workbench das Freigabesignal an die FastAPI-Bridge. Erst nach dieser expliziten Autorisierung wird der Git-Commit-Push initiiert. Im Falle einer Blockade (roter Knopf) greift die algorithmische Apnoe — die sofortige Inaktivierung aller automatisierten Push-Prozesse.
