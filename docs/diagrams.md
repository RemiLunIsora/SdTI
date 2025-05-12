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
``` mermaid
sequenceDiagram
 Client di Gioco->>Client di Gioco: Interazione (Giocatore, nemico/Giocatore, giocatore) (Inzio combattimento)
 activate Client di Gioco
 Client di Gioco->>Gestore di Combattimento: Inizia Combattimento
 activate Gestore di Combattimento
 Client di Gioco->>Interfaccia: Mostra schermata combattimento
deactivate Client di Gioco
Client di Gioco->>Client di Gioco: Interazione (Giocatore, NPC/Giocatore, Giocatore) (Scambio/acquisto di items)
activate Client di Gioco
Client di Gioco->>Gestore Inventario: Seleziona items
activate Gestore Inventario
Client di Gioco->>Interfaccia: Mostra Inventario 
deactivate Client di Gioco
```

<h2><span style="font-weight: 400;">Diagramma Casi d'uso</span></h2>
``` mermaid

sequenceDiagram
  actor A as Giocatore
  participant C as Gestione Combattimento
  participant D as Gestione Quest
  participant E as Gestione Inventario
  participant F as Report Statistiche
  actor B as Sistema
  A ->> C:
  A ->> E:
  A ->> D:
  B ->> D:
  B ->> F:
```