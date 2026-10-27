# Módulo responsável por armazenar os dados de entrada (a coreografia do Heian Shodan)

coreografia_heian_shodan = [
    {"movimento": "Reset", "pausa": 2},              # Yoi: Postura de atenção e preparação
    
    # --- Bloco 1: Esquerda ---
    {"movimento": "OneStepTurnLeft", "pausa": 1},    # Vira 90º à esquerda
    {"movimento": "LeftTackle", "pausa": 1},         # Simula Gedan Barai (defesa baixa) esquerdo
    {"movimento": "OneStepForward", "pausa": 1},     # Avança base (Zenkutsu Dachi)
    {"movimento": "RightHitForward", "pausa": 1},    # Oi Zuki (soco com passo) direito
    
    # --- Bloco 2: Direita ---
    {"movimento": "TurnRight1", "pausa": 1},         # Vira 180º à direita
    {"movimento": "RightTackle", "pausa": 1},        # Simula Gedan Barai direito
    {"movimento": "OneStepForward", "pausa": 1},     # Avança base
    {"movimento": "LeftHitForward", "pausa": 1},     # Oi Zuki esquerdo
    
    # --- Bloco 3: Frente (Caminho do I) ---
    {"movimento": "OneStepTurnLeft", "pausa": 1},    # Vira 90º à esquerda (para a frente)
    {"movimento": "LeftTackle", "pausa": 1},         # Simula Gedan Barai esquerdo
    {"movimento": "OneStepForward", "pausa": 0.5},   # Avança 1
    {"movimento": "RightSidePunch", "pausa": 0.5},   # Oi Zuki direito (simula Age Uke/soco alto)
    {"movimento": "OneStepForward", "pausa": 0.5},   # Avança 2
    {"movimento": "LeftSidePunch", "pausa": 0.5},    # Oi Zuki esquerdo
    {"movimento": "OneStepForward", "pausa": 0.5},   # Avança 3
    {"movimento": "Fight_RHit", "pausa": 1},         # Golpe forte com a direita - KIAI!
    
    # --- Bloco 4: Retorno e Conclusão ---
    {"movimento": "TurnLeft1", "pausa": 1},          # Vira 270º à esquerda pelas costas (grande rotação)
    {"movimento": "LeftTackle", "pausa": 1},         # Simula Gedan Barai esquerdo
    {"movimento": "OneStepForward", "pausa": 1},     # Avança base
    {"movimento": "RightHitForward", "pausa": 2},    # Oi Zuki direito
    
    {"movimento": "Reset", "pausa": 0}               # Yame: Retorno à posição inicial
]