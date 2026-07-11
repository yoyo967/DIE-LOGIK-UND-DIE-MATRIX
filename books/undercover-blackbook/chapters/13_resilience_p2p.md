# Kapitel 12: Decentralized System Resilience (P2P Mesh Replicas)

Zur Abwehr zentraler Infrastruktur-Ausfälle implementiert das System ein dezentrales, zensurresistentes P2P-Mesh. Die Code-Repositories und System-Zustände werden kontinuierlich über **IPFS (InterPlanetary File System)** und verschlüsselte **Nostr-Relays** gespiegelt:

*   **Selbstheilung:** Bei Zensur oder Löschung zentraler Cloud-Instanzen rekonstituiert sich das Monorepo über die dezentralen P2P-Knoten.
*   **Kryptografische Signatur:** Jedes Commit-Paket ist signiert und im Nostr-Protokoll verankert, was Manipulationen unmöglich macht.
