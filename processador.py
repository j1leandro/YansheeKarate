import time
import YanAPI

def executar_kata(coreografia):
    """
    Processa a lista de movimentos, enviando os comandos para a API do robô
    e gerenciando as pausas e respostas de sucesso.
    """
    print("Iniciando execução do Heian Shodan...")

    # Posição inicial (Yoi)
    YanAPI.sync_play_motion(name="Reset")
    time.sleep(2)

    for passo in coreografia:
        movimento = passo["movimento"]
        pausa = passo["pausa"]
        
        print("Executando: {}".format(movimento))
        
        # Dispara o movimento em velocidade normal da versão v1 da API
        sucesso = YanAPI.sync_play_motion(name=movimento, speed="normal", repeat=1, version="v1")
        
        if not sucesso:
            print("Aviso: Falha ao executar o passo {}.".format(movimento))
            
        # Pausa estratégica para controle de respiração/ritmo do kata
        if pausa > 0:
            time.sleep(pausa)

    print("Kata concluído.")