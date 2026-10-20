import time
import YanAPI

# Inicializa a API localmente no Raspberry Pi do robô
YanAPI.yan_api_init("127.0.0.1")

# Sequência do Heian Shodan adaptada aos movimentos base do Yanshee
coreografia_heian_shodan = [
    ("Reset", 2),               # Yoi: Postura de atenção e preparação
    
    # --- Bloco 1: Esquerda ---
    ("OneStepTurnLeft", 1),     # Vira 90º à esquerda
    ("LeftTackle", 1),          # Simula Gedan Barai (defesa baixa) esquerdo
    ("OneStepForward", 1),      # Avança base (Zenkutsu Dachi)
    ("RightHitForward", 1),     # Oi Zuki (soco com passo) direito
    
    # --- Bloco 2: Direita ---
    ("TurnRight1", 1),          # Vira 180º à direita
    ("RightTackle", 1),         # Simula Gedan Barai direito
    ("OneStepForward", 1),      # Avança base
    ("LeftHitForward", 1),      # Oi Zuki esquerdo
    
    # --- Bloco 3: Frente (Caminho do I) ---
    ("OneStepTurnLeft", 1),     # Vira 90º à esquerda (para a frente)
    ("LeftTackle", 1),          # Simula Gedan Barai esquerdo
    ("OneStepForward", 0.5),    # Avança 1
    ("RightSidePunch", 0.5),    # Oi Zuki direito (simula Age Uke/soco alto)
    ("OneStepForward", 0.5),    # Avança 2
    ("LeftSidePunch", 0.5),     # Oi Zuki esquerdo
    ("OneStepForward", 0.5),    # Avança 3
    ("Fight_RHit", 1),          # Golpe forte com a direita - KIAI!
    
    # --- Bloco 4: Retorno e Conclusão ---
    ("TurnLeft1", 1),           # Vira 270º à esquerda pelas costas (grande rotação)
    ("LeftTackle", 1),          # Simula Gedan Barai esquerdo
    ("OneStepForward", 1),      # Avança base
    ("RightHitForward", 2),     # Oi Zuki direito
    
    ("Reset", 0)                # Yame: Retorno à posição inicial
]

print("Iniciando execução do Heian Shodan...")

# Yoi
YanAPI.sync_play_motion(name="Reset")
time.sleep(2)

for movimento, pausa in coreografia_heian_shodan:
    print("Executando: {}".format(movimento))
    
    # Dispara o movimento em velocidade normal da versão v1 da API
    sucesso = YanAPI.sync_play_motion(name=movimento, speed="normal", repeat=1, version="v1")
    
    if not sucesso:
        print("Aviso: Falha ao executar o passo {}.".format(movimento))
        
    # Pausa estratégica para controle de respiração/ritmo do kata
    if pausa > 0:
        time.sleep(pausa)

print("Kata concluído.")
