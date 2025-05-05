<h1><span style="font-weight: 400;">Diagrammi</span></h1>
<h2><span style="font-weight: 400;">Diagramma Attività</span></h2>
``` mermaid
graph TD
    circleId(("`Start`")) --> A
    A(["Apro l'app"]) --> B{"Collegamento ad una rete"}
    B --> K@{ shape: fork, label: "Fork or Join" } & D["Errore"]
    K --> C["Collegamento a GPS"] & L[Collegamengo all'account personale]
    C & L--> F@{ shape: fork, label: "Fork or Join" }
    F --> E[Utilizzo l'app]
    F --> G[Tracciamento del GPS]
    E & G --> H@{ shape: fork, label: "Fork or Join" }
    H --> J[Chiudo l'app]
    J --> I@{ shape: framed-circle, label: "Stop" }
```
<h2><span style="font-weight: 400;">Diagramma di Sequenza</span></h2>