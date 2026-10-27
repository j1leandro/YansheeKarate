# Módulo principal (Entrypoint do projeto Grau A)
import YanAPI
from movimentos import coreografia_heian_shodan
from processador import executar_kata

def main():
    # Inicializa a API localmente no Raspberry Pi do robô
    YanAPI.yan_api_init("127.0.0.1")
    
    # Executa o processamento da coreografia
    executar_kata(coreografia_heian_shodan)

if __name__ == "__main__":
    main()