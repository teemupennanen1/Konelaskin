´´´mermaid
sequenceDiagram
    main->>laite: Machine()
    laite->>tankki: FuelTank()
    laite->>tankki: fill(40)
    laite->>kone: Engine(tankki)
    main->>laite: drive()
    laite->>+kone: start()
    kone->>-tankki: consume(5)
    laite->>+kone: is_running()
    kone->>tankki: fuel_contents()
    tankki-->>kone: 35
    kone->>-laite: true
    laite->>+kone: use_energy()
    kone->>-tankki: consume(10)
´´´